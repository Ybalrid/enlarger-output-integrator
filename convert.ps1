Remove-Item -Path .\output -Recurse -Force
mkdir output
ffmpeg -i highspeed.mov "output/%04d.png"
