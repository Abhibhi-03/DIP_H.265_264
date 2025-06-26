# main.py
import os
import cv2
import numpy as np
import time
from encoder import encode_frame, motion_estimation
from decoder import decode_frame
from utils import save_frame, psnr

# Configuration
USE_GRAYSCALE = False         # Set True for grayscale compression
MAX_FRAMES = 15               # Process 15 frames for quick testing

# Output directories
os.makedirs("input", exist_ok=True)
os.makedirs("output/original_frames", exist_ok=True)
os.makedirs("output/reconstructed_frames", exist_ok=True)

# Load video
cap = cv2.VideoCapture("input/sample_video.mp4")
success, frame = cap.read()
frame_id = 0
psnr_total = 0
prev_frame = None

# Frame processing loop
while success and frame_id < MAX_FRAMES:
    start_time = time.time()

    # Optional grayscale conversion
    frame_proc = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) if USE_GRAYSCALE else frame.copy()

    # Save original frame
    save_frame(frame_proc, f"output/original_frames/frame_{frame_id:03d}.png")

    # Encode/Decode
    if prev_frame is None:
        encoded = encode_frame(frame_proc)
        decoded = decode_frame(encoded)
    else:
        flow = motion_estimation(prev_frame, frame_proc)
        encoded = encode_frame(frame_proc, flow)
        decoded = decode_frame(encoded)

    # Save reconstructed frame
    save_frame(decoded, f"output/reconstructed_frames/frame_{frame_id:03d}.png")

    # Quality metric
    psnr_val = psnr(frame_proc, decoded)
    psnr_total += psnr_val

    print(f"[Frame {frame_id:02d}] PSNR: {psnr_val:.2f} dB | Time: {time.time() - start_time:.2f}s")

    # Next frame prep
    prev_frame = frame_proc.copy()
    frame_id += 1
    success, frame = cap.read()

cap.release()

# Summary
print(f"Average PSNR over {frame_id} frames: {psnr_total / frame_id:.2f} dB")
print("To generate video, run:")
print("ffmpeg -framerate 10 -i output/reconstructed_frames/frame_%03d.png -c:v libx265 -crf 18 output/output_video.mp4")
