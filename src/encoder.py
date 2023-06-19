import os
import zipfile
import shutil
import cv2
import numpy as np
import subprocess
class Encode:
    def __init__(self) -> None:
        pass

    def get_file_sha256(self,file_path):
        command = f"Get-FileHash -Path '{file_path}' -Algorithm SHA256 | Select-Object -ExpandProperty Hash"
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        output = result.stdout.strip()
        return output
        
        
    def encode_file(self,x):
        self.args = x
        if self.args.encode!=None:
            if self.args.output==None:
                self.args.output = "output.mp4"
            if self.args.size!=None and int(self.args.size)**2 > 3800**2:   #libx264 cant render above 3800x3800
                self.args.size = 3800**2
            if self.args.size!=None:
                self.args.size = int(self.args.size)**2
            if self.args.size==None:
                self.args.size = 1024**2
            if self.args.fps==None:
                self.args.fps = 30
            if self.args.fps!=None:
                self.args.fps = float(self.args.fps)
                
            print("file : ",self.args.encode)
            print("output : ",self.args.output)
            print("size : ",self.args.size)
            print("fps : ",self.args.fps)
            #shutil.copyfile(self.args.encode,os.getcwd())
            file_path = os.path.basename(self.args.encode)
            destination_path = os.path.join(os.getcwd(), file_path)
            if file_path not in os.listdir(os.getcwd()):
                shutil.copy(self.args.encode,destination_path)

            #---------padding-----------
            zip_file_path = "gen.zip"
            
            with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.write(file_path, arcname=file_path)
            os.remove(file_path)
            org = zip_file_path
            dest="sorted.zip"
            shutil.copy(org,dest)
            
            factor = self.args.size
            zip_file_size = os.path.getsize(dest)
            padding_size = factor - (zip_file_size % factor)
            with zipfile.ZipFile(dest, 'a') as zip_file:
                padding_data = b'\0' * padding_size
                zip_file.writestr('padding.bin', padding_data)
            
            zip_file_size = os.path.getsize(dest)
            while os.path.getsize(dest) % factor !=0:
                os.remove(dest)
                shutil.copy(org,dest)
                zip_file_size = os.path.getsize(dest)
                padding_size -=1
                with zipfile.ZipFile(dest, 'a') as zip_file:
                    padding_data = b'\0' * padding_size
                    zip_file.writestr('padding.bin', padding_data)
            
            os.remove(org)
            os.rename(dest,org)
            print("zip is complete")
            sha256 = self.get_file_sha256(org)
            print('\033[93m'+"\nKEY  :  "+sha256+"\n\n")
            print('\033[0m'+"\n")
            #print("\nKEY : ",sha256,"\n\n")


            #-----------video maker--------------
            h = int(self.args.size**0.5)
            with open(org,'rb') as file:
                data_file = file.read()
            
            try:
                os.mkdir('images')
            except:
                pass
            size = factor
            num=0
            data = np.frombuffer(data_file, dtype=np.uint8)
            for i in range(0,len(data),size):
                temp = data[i:i+size]
                if len(temp)==size:
                    image_data = temp.reshape((h, h)).astype(np.uint8)
                    cv2.imwrite("./images/pic{}.png".format(str(num)), image_data)
                    num+=1
            os.system("ffmpeg -framerate {} -i ./images/pic%d.png -c:v libx264 -crf 0 {}".format(self.args.fps,self.args.output))
            print('\033[94m'+"Video created")
            print('\033[0m'+"\n")
            os.remove("gen.zip")
            shutil.rmtree('images')