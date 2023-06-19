import argparse
from src.encoder import Encode
from src.decoder import Decoder

class Parse:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(prog='YT storage',description='Turn files to encrypted video',epilog='Developed by sourabhkv')
        self.parser.add_argument('--version',"-v",dest='version',action='version', version='%(prog)s 1.0',help="Current program version")
        self.parser.add_argument('--encode','-e',dest='encode' ,help='file to to encoded')
        self.parser.add_argument('--decode','-d',dest='decode' ,help='file to be decoded')
        self.parser.add_argument('--output','-o',dest='output' ,help='output of generated file')
        self.parser.add_argument('--size',dest='size' ,help='size of frame')
        self.parser.add_argument('--fps','-fps',dest='fps' ,help='fps')
        self.parser.add_argument('--yt','-yt',dest='yt' ,help='store encoded video online (t/F)')
        self.parser.add_argument('--keep','-k',dest='keep' ,help='do not delete images folder')
        self.parser.add_argument('--interval',dest='interval' ,help='decode video skipping frames')
        self.parser.add_argument('--resize','-rs',dest='resize' ,help='resize and decode video')
        self.args = self.parser.parse_args()

        
        
        if self.args.encode:
            self.enc_inst = Encode()
            self.enc_inst.encode_file(self.args)
        if self.args.decode:
            self.dec_inst = Decoder()
            self.dec_inst.decode_file(self.args)


if __name__=='__main__':
    Parse()