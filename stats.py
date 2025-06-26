import os
import cv2
import numpy as np
from math import log2
import pandas as pd

def calculate_entropy(image):
    if len(image.shape) == 3:
        channels = cv2.split(image)
        return np.mean([
            -np.sum([(p/np.sum(hist)) * log2(p/np.sum(hist)) for p in hist if p > 0])
            for hist in [cv2.calcHist([c], [0], None, [256], [0, 256]).ravel() for c in channels]
        ])
    else:
        hist = cv2.calcHist([image], [0], None, [256], [0, 256]).ravel()
        hist /= hist.sum()
        return -np.sum([p * log2(p) for p in hist if p > 0])

def compute_stats(input_dir, output_dir):
    files = sorted(os.listdir(input_dir))
    stats = []

    for file in files:
        orig_path = os.path.join(input_dir, file)
        recon_path = os.path.join(output_dir, file)
        if not os.path.exists(recon_path): continue

        original = cv2.imread(orig_path)
        compressed = cv2.imread(recon_path)

        original_size = os.path.getsize(orig_path)
        compressed_size = os.path.getsize(recon_path)
        compression_ratio = original_size / compressed_size if compressed_size else float('inf')

        entropy_orig = calculate_entropy(original)
        entropy_comp = calculate_entropy(compressed)
        entropy_loss = entropy_orig - entropy_comp

        psnr_val = cv2.PSNR(original, compressed)

        stats.append({
            "Frame": file,
            "Original Size (KB)": round(original_size / 1024, 2),
            "Compressed Size (KB)": round(compressed_size / 1024, 2),
            "Compression Ratio": round(compression_ratio, 2),
            "Original Entropy": round(entropy_orig, 2),
            "Compressed Entropy": round(entropy_comp, 2),
            "Entropy Loss": round(entropy_loss, 2),
            "PSNR (dB)": round(psnr_val, 2)
        })

    df = pd.DataFrame(stats)
    print(df.to_string(index=False))
    return df

# Update with your actual paths
compute_stats("output/original_frames", "output/reconstructed_frames")
