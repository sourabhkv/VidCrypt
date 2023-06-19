# VidCrypt
Convert any file to encrypted video , get file file from encrypted video

Every file is made of bytes , bytes range from 0-255 . These values are saved to greyscale images and losless video is made.
Decoding is done by reading each frame of video.

## Requirements
Needs ffmpeg installed in path

## Commands
```
usage: YT storage [-h] [--version] [--encode ENCODE] [--decode DECODE] [--output OUTPUT] [--size SIZE] [--fps FPS]
                  [--yt YT] [--keep KEEP] [--interval INTERVAL] [--resize RESIZE]

Turn files to encrypted video

optional arguments:
  -h, --help            show this help message and exit
  --version, -v         Current program version
  --encode ENCODE, -e ENCODE
                        file to to encoded
  --decode DECODE, -d DECODE
                        file to be decoded
  --output OUTPUT, -o OUTPUT
                        output of generated file
  --size SIZE           size of frame
  --fps FPS, -fps FPS   fps
  --yt YT, -yt YT       store encoded video online (t/F)
  --keep KEEP, -k KEEP  do not delete images folder
  --interval INTERVAL   decode video skipping frames
  --resize RESIZE, -rs RESIZE
                        resize and decode video

Developed by sourabhkv
```

## Example
This image is being converted to video
![IMG_20230304_105501](https://github.com/sourabhkv/VidCrypt/assets/55890376/ff6b44d6-b341-47b2-aab8-640fd0155636)



https://github.com/sourabhkv/VidCrypt/assets/55890376/59112465-e423-4b56-81ab-d10b3972bb30

### command
#### encoding
```powershell
VidCrypt.exe -e "E:\phone\DCIM\Camera\IMG_20230304_105501.jpg" --fps 6 --size 800
file :  E:\phone\DCIM\Camera\IMG_20230304_105501.jpg
output :  output.mp4
size :  640000
fps :  6.0
zip is complete

KEY  :  BC6684E81AE7C1C23BB5D5310015679D815956A2598E2F512AAA5B370E9909F6




ffmpeg version N-109920-gac6eec1fc2-20230224 Copyright (c) 2000-2023 the FFmpeg developers
  built with gcc 12.2.0 (crosstool-NG 1.25.0.90_cf9beb1)
  configuration: --prefix=/ffbuild/prefix --pkg-config-flags=--static --pkg-config=pkg-config --cross-prefix=i686-w64-mingw32- --arch=i686 --target-os=mingw32 --enable-gpl --enable-version3 --disable-debug --disable-w32threads --enable-pthreads --enable-iconv --enable-libxml2 --enable-zlib --enable-libfreetype --enable-libfribidi --enable-gmp --enable-lzma --enable-fontconfig --enable-libvorbis --enable-opencl --disable-libpulse --enable-libvmaf --disable-libxcb --disable-xlib --enable-amf --enable-libaom --enable-libaribb24 --enable-avisynth --enable-chromaprint --enable-libdav1d --disable-libdavs2 --disable-libfdk-aac --enable-ffnvcodec --enable-cuda-llvm --enable-frei0r --enable-libgme --enable-libkvazaar --enable-libass --enable-libbluray --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librist --enable-libssh --enable-libtheora --enable-libvpx --enable-libwebp --enable-lv2 --disable-libmfx --enable-libvpl --enable-openal --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenh264 --enable-libopenjpeg --enable-libopenmpt --disable-librav1e --enable-librubberband --enable-schannel --enable-sdl2 --enable-libsoxr --enable-libsrt --disable-libsvtav1 --enable-libtwolame --disable-libuavs3d --disable-libdrm --disable-vaapi --enable-libvidstab --enable-vulkan --enable-libshaderc --enable-libplacebo --enable-libx264 --enable-libx265 --disable-libxavs2 --enable-libxvid --enable-libzimg --enable-libzvbi --extra-cflags=-DLIBTWOLAME_STATIC --extra-cxxflags= --extra-ldflags=-pthread --extra-ldexeflags= --extra-libs=-lgomp --extra-version=20230224
  libavutil      58.  3.100 / 58.  3.100
  libavcodec     60.  4.100 / 60.  4.100
  libavformat    60.  4.100 / 60.  4.100
  libavdevice    60.  2.100 / 60.  2.100
  libavfilter     9.  4.100 /  9.  4.100
  libswscale      7.  2.100 /  7.  2.100
  libswresample   4. 11.100 /  4. 11.100
  libpostproc    57.  2.100 / 57.  2.100
Input #0, image2, from './images/pic%d.png':
  Duration: 00:00:01.83, start: 0.000000, bitrate: N/A
  Stream #0:0: Video: png, gray(pc), 800x800, 6 fps, 6 tbr, 6 tbn
Stream mapping:
  Stream #0:0 -> #0:0 (png (native) -> h264 (libx264))
Press [q] to stop, [?] for help
[libx264 @ 077dcac0] using cpu capabilities: MMX2 SSE2Fast SSSE3 SSE4.2 AVX FMA3 BMI2 AVX2
[libx264 @ 077dcac0] profile High 4:4:4 Predictive, level 3.1, 4:0:0, 8-bit
[libx264 @ 077dcac0] 64 - core 164 - H.264/MPEG-4 AVC codec - Copyleft 2003-2023 - http://www.videolan.org/x264.html - options: cabac=1 ref=3 deblock=1:0:0 analyse=0x3:0x113 me=hex subme=7 psy=0 mixed_ref=1 me_range=16 chroma_me=0 trellis=0 8x8dct=1 cqm=0 deadzone=21,11 fast_pskip=0 chroma_qp_offset=0 threads=18 lookahead_threads=3 sliced_threads=0 nr=0 decimate=1 interlaced=0 bluray_compat=0 constrained_intra=0 bframes=0 weightp=2 keyint=250 keyint_min=6 scenecut=40 intra_refresh=0 rc=cqp mbtree=0 qp=0
Output #0, mp4, to 'output.mp4':
  Metadata:
    encoder         : Lavf60.4.100
  Stream #0:0: Video: h264 (avc1 / 0x31637661), gray(pc, gbr/unknown/unknown, progressive), 800x800, q=2-31, 6 fps, 12288 tbn
    Metadata:
      encoder         : Lavc60.4.100 libx264
    Side data:
      cpb: bitrate max/min/avg: 0/0/0 buffer size: 0 vbv_delay: N/A
frame=   11 fps=0.0 q=-1.0 Lsize=    6566kB time=00:00:01.66 bitrate=32271.8kbits/s speed=10.5x
video:6565kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.013953%
[libx264 @ 077dcac0] frame I:11    Avg QP: 0.00  size:611077
[libx264 @ 077dcac0] mb I  I16..4..PCM:  5.3%  0.0%  0.0% 94.7%
[libx264 @ 077dcac0] 8x8 transform intra:0.0%
[libx264 @ 077dcac0] coded y intra: 94.8%
[libx264 @ 077dcac0] i16 v,h,dc,p: 100%  0%  0%  0%
[libx264 @ 077dcac0] i8c dc,h,v,p: 100%  0%  0%  0%
[libx264 @ 077dcac0] kb/s:29331.71
Video created
```
#### Decoding
```powershell
VidCrypt.exe -d "output.mp4"
enter KEY  : BC6684E81AE7C1C23BB5D5310015679D815956A2598E2F512AAA5B370E9909F6
file :  output.mp4
output :  E:\ytdrive\enhance
File verified
```
![image](https://github.com/sourabhkv/VidCrypt/assets/55890376/25835e3c-9e9c-491f-8e71-950b1b54e39a)
![image](https://github.com/sourabhkv/VidCrypt/assets/55890376/65f62aed-d202-4841-bb85-a4676ffade75)

## Application
- Zip files with passwords can be cracked without passwords but encrypted video cant be cracked
- Infinity storage i.e. upload encrypted video to video platform since video platform don't have size limit and decode it whenever file is needed. Brutal YouTube compression wont let even Greyscale image exist in original format , for now Vimeo will be better.
- Multiple files can be converted to 1 video , for now make a zip and encode zip.
