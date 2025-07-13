# Enlarger short exposure estimation

This is in an attempt of using a regular darkroom enlarger as a makeshift sensitometer.

"highspeed.mov" is a trimmed clip recored by an iPhone of the flash of the bulb at 240 FPS.

(The enlarger timer was set to 0.9 seconds)

Scripts:

- `convert.ps1` calls `ffmpeg` to convert the mov file into an image sequence
- `analyze.py` find the brightest pixel around the center of the frame, and output a CSV file with the frame number and brightness value
- `plot.py` simply display the CSV on screen as a graph
- `compute_expousure.py` attempt to give you a lx.s (lux seconds) exposure estimation from the framerate, an instantatneous lux measurement (that you know and have measured separately), and the framerate. What it does is to basically integrate the area under the curve. The Y axis is re-linearized assuming it was in sRGB gamma space (gama 2.2)

The result of this is... values that are sensible, but instead of under-estimating the exposure, if I belive this thing's output, I was actually *under* estimating the exposure.