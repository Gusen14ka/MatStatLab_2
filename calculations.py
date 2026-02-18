import numpy as np

def calculate(sample, n):
    x_mean = np.mean(sample)

    x_med = np.median(sample)

    xR = (min(sample) + max(sample)) / 2

    q1, q3 = np.percentile(sample, [25, 75])
    xQ = (q1 + q3) / 2

    sorted_sample = np.sort(sample)
    r = int(0.1 * n)
    xTR = np.mean(sorted_sample[r:-r])

    return x_mean, x_med, xR, xQ, xTR