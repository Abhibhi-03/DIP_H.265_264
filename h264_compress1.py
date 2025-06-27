import cv2
import os

# --------- CONFIG ---------
input_file = 'input.mp4'
opencv_output = 'output_h264_opencv.mp4'
# --------------------------

# Open input video
cap = cv2.VideoCapture(input_file)

if not cap.isOpened():
    print("Could not open input video.")
    exit()

# Get properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Codec and writer
fourcc = cv2.VideoWriter_fourcc(*'avc1')  # H.264-compatible
out = cv2.VideoWriter(opencv_output, fourcc, fps, (width, height))

# Read first frame for PSNR calculation
ret, first_frame = cap.read()
first_frame_out = None

# Write frames
while ret:
    out.write(first_frame)
    if first_frame_out is None:
        first_frame_out = first_frame.copy()
    ret, first_frame = cap.read()

cap.release()
out.release()
print("OpenCV compression complete.")

# --------- PSNR Calculation ---------
cap1 = cv2.VideoCapture(input_file)
cap2 = cv2.VideoCapture(opencv_output)

ret1, frame1 = cap1.read()
ret2, frame2 = cap2.read()

if ret1 and ret2:
    psnr = cv2.PSNR(frame1, frame2)
    print(f"PSNR (Input vs. Compressed Frame): {psnr:.2f} dB")
else:
    print("⚠️ Could not compute PSNR")

cap1.release()
cap2.release()

# --------- File Size Comparison ---------
input_size = os.path.getsize(input_file) / (1024 * 1024)
output_size = os.path.getsize(opencv_output) / (1024 * 1024)
compression_ratio = input_size / output_size if output_size else float('inf')

print(f"Original size: {input_size:.2f} MB")
print(f"Compressed size: {output_size:.2f} MB")
print(f"Compression ratio: {compression_ratio:.2f}x")

# References:
# [1] OpenCV Documentation, https://docs.opencv.org/4.x/
# [2] OpenCV PSNR Tutorial, https://docs.opencv.org/4.x/d5/dc4/tutorial_video_input_psnr_ssim.html
# [3] FourCC Codecs, https://www.fourcc.org/codecs.php
# [4] Wikipedia – Peak Signal-to-Noise Ratio, https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio
# [5] MathWorks – PSNR, https://www.mathworks.com/help/images/ref/psnr.html