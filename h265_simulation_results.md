# Video Compression Simulation Results

## Table 1: Frame-wise PSNR and Processing Time

This table shows the PSNR (Peak Signal-to-Noise Ratio) in decibels and the processing time in seconds for each processed frame. Higher PSNR values (above 40 dB) indicate excellent reconstructed quality. Processing times vary due to frame complexity and computational demand.

| Frame    |   PSNR (dB) |   Time (s) |
|:---------|------------:|-----------:|
| Frame 00 |       42.38 |      11.52 |
| Frame 01 |       42.38 |      15.84 |
| Frame 02 |       42.26 |      18.93 |
| Frame 03 |       42.51 |      15.51 |
| Frame 04 |       42.19 |      20.11 |
| Frame 05 |       42.49 |      20.03 |
| Frame 06 |       42.37 |      15.39 |
| Frame 07 |       42.48 |      14.46 |
| Frame 08 |       42.27 |      15.69 |
| Frame 09 |       42.45 |      14.85 |
| Frame 10 |       42.33 |      15.01 |
| Frame 11 |       42.41 |      14.24 |
| Frame 12 |       42.2  |      15.05 |
| Frame 13 |       42.38 |      14.34 |
| Frame 14 |       42.28 |      15.26 |

## Table 2: Frame-wise Compression Metrics

This table includes original and compressed sizes, compression ratios, entropy values before and after compression, entropy loss, and PSNR for each frame. The compression ratio reflects data reduction, while entropy values indicate information density. The small entropy loss and high PSNR confirm efficient, non-destructive compression.

| Frame         |   Original Size (KB) |   Compressed Size (KB) |   Compression Ratio |   Original Entropy |   Compressed Entropy |   Entropy Loss |   PSNR (dB) |
|:--------------|---------------------:|-----------------------:|--------------------:|-------------------:|---------------------:|---------------:|------------:|
| frame_000.png |              6529.47 |                5997.05 |                1.09 |               7.35 |                 7.06 |           0.29 |       42.38 |
| frame_001.png |              6489.2  |                6143.29 |                1.06 |               7.36 |                 7.07 |           0.29 |       42.38 |
| frame_002.png |              6545.71 |                6243.31 |                1.05 |               7.36 |                 7.07 |           0.28 |       42.26 |
| frame_003.png |              6434.29 |                6156.97 |                1.05 |               7.36 |                 7.08 |           0.28 |       42.51 |
| frame_004.png |              6571.91 |                6190.92 |                1.06 |               7.36 |                 7.07 |           0.28 |       42.19 |
| frame_005.png |              6496.63 |                6207.25 |                1.05 |               7.36 |                 7.08 |           0.28 |       42.49 |
| frame_006.png |              6592.99 |                6276.37 |                1.05 |               7.37 |                 7.08 |           0.28 |       42.37 |
| frame_007.png |              6503.72 |                6235.45 |                1.04 |               7.37 |                 7.09 |           0.28 |       42.48 |
| frame_008.png |              6626.42 |                6222.32 |                1.06 |               7.37 |                 7.09 |           0.28 |       42.27 |
| frame_009.png |              6567.68 |                6278.27 |                1.05 |               7.38 |                 7.09 |           0.28 |       42.45 |
| frame_010.png |              6656.17 |                6334.96 |                1.05 |               7.38 |                 7.09 |           0.28 |       42.33 |
| frame_011.png |              6585.79 |                6302.88 |                1.04 |               7.38 |                 7.1  |           0.28 |       42.41 |
| frame_012.png |              6716.47 |                6317.68 |                1.06 |               7.38 |                 7.1  |           0.28 |       42.2  |
| frame_013.png |              6650.78 |                6352.51 |                1.05 |               7.38 |                 7.1  |           0.28 |       42.38 |
| frame_014.png |              6719.99 |                6395.86 |                1.05 |               7.39 |                 7.1  |           0.28 |       42.28 |
