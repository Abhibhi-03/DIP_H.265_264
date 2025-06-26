import cv2
import numpy as np

def motion_estimation(prev_frame, curr_frame):
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY) if len(prev_frame.shape) == 3 else prev_frame
    curr_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY) if len(curr_frame.shape) == 3 else curr_frame
    flow = cv2.calcOpticalFlowFarneback(prev_gray, curr_gray, None,
                                        pyr_scale=0.5, levels=3, winsize=15,
                                        iterations=3, poly_n=5, poly_sigma=1.2, flags=0)
    return flow

# Standard quantization matrix (JPEG-like)
QUANT_MAT = np.array([
    [16,11,10,16,24,40,51,61],
    [12,12,14,19,26,58,60,55],
    [14,13,16,24,40,57,69,56],
    [14,17,22,29,51,87,80,62],
    [18,22,37,56,68,109,103,77],
    [24,35,55,64,81,104,113,92],
    [49,64,78,87,103,121,120,101],
    [72,92,95,98,112,100,103,99]
])

def block_dct_quantize(channel):
    h, w = channel.shape
    channel = channel.astype(np.float32) - 128
    result = np.zeros_like(channel)

    for i in range(0, h, 8):
        for j in range(0, w, 8):
            block = channel[i:i+8, j:j+8]
            if block.shape == (8, 8):
                dct = cv2.dct(block)
                q_block = np.round(dct / QUANT_MAT)
                result[i:i+8, j:j+8] = q_block

    return result

def encode_frame(frame, flow=None):
    # Split BGR channels
    if len(frame.shape) == 3:
        channels = cv2.split(frame)
        encoded_channels = [block_dct_quantize(c) for c in channels]
        return encoded_channels
    else:
        return [block_dct_quantize(frame)]