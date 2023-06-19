import cv2
import os
import shutil
import zipfile
import subprocess

class Decoder:
    def __init__(self) -> None:
        pass

    def get_file_sha256(self,file_path):
        command = f"Get-FileHash -Path '{file_path}' -Algorithm SHA256 | Select-Object -ExpandProperty Hash"
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        output = result.stdout.strip()
        return output

    def decode_file(self,x):
        self.args = x
        if self.args.decode!=None:
            if self.args.output==None:
                self.args.output = os.getcwd()
            if not os.path.exists(self.args.decode):
                print("Path does not exist")
                exit()
            hash = input("enter KEY  : ")
            print("file : ",self.args.decode)
            print("output : ",self.args.output)
            try:
                os.mkdir('images_extract')
            except:
                pass
            Frame_skip = False
            if self.args.interval!=None:
                self.args.interval = int(self.args.interval)
                Frame_skip = True
            if self.args.resize!=None:
                self.args.resize = int(self.args.resize)

            video = cv2.VideoCapture(self.args.decode)
            frame_count = 0
            output_index = 0
            while True:
                ret, frame = video.read()

                if not ret:
                    break

                frame_count+=1
                if Frame_skip:
                    if frame_count % self.args.interval != 0:
                        continue
                
                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(f'./images_extract/pic{output_index:d}.png', frame_gray)
                output_index += 1
            
            video.release()
            s = len(os.listdir('./images_extract'))
            data = b''
            for i in range(s):
                decoded_image_data = cv2.imread("./images_extract/pic{}.png".format(str(i)), cv2.IMREAD_GRAYSCALE)
                if self.args.resize:
                    decoded_image_data = cv2.resize(decoded_image_data, (1024, 1024), interpolation=cv2.INTER_NEAREST)
                decoded_data = decoded_image_data.ravel()
                try:
                    data += decoded_data.tobytes()
                except:
                    pass

            with open('generated.zip','wb') as f1:
                f1.write(data)

            
            
            sha256 = self.get_file_sha256("generated.zip")
            if sha256 == hash:
                print('\033[94m'+"File verified")
                with zipfile.ZipFile("generated.zip", 'r') as zip_ref:
                    zip_ref.extractall(self.args.output)
                os.chdir(self.args.output)
                os.remove('padding.bin')
            
            else:
                print('\033[91m'+"File corrupted")
                #os.remove('generated.zip')
            
            os.remove("generated.zip")
            shutil.rmtree('images_extract')
            print('\033[0m'+"\n")