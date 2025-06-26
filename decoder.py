import cv2
import numpy as np
from encoder import QUANT_MAT

def block_idct_dequantize(channel):
    h, w = channel.shape
    result = np.zeros_like(channel, dtype=np.float32)

    for i in range(0, h, 8):
        for j in range(0, w, 8):
            block = channel[i:i+8, j:j+8]
            if block.shape == (8, 8):
                deq_block = block * QUANT_MAT
                idct = cv2.idct(deq_block)
                result[i:i+8, j:j+8] = idct

    result = np.clip(result + 128, 0, 255)
    return result.astype(np.uint8)

def decode_frame(encoded_frame):
    decoded_channels = [block_idct_dequantize(c) for c in encoded_frame]
    if len(decoded_channels) == 3:
        return cv2.merge(decoded_channels)
    return decoded_channels[0]
