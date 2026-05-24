import numpy as np

# Simulated electrical signal
np.random.seed(42)
time = np.linspace(0, 10, 500)
signal = np.sin(time) + np.random.normal(0, 0.1, 500)

# Inject anomaly
signal[300:320] += 2

# Simple anomaly detection
mean = np.mean(signal)
std = np.std(signal)

threshold = mean + 2 * std

anomalies = [i for i, val in enumerate(signal) if val > threshold]

print("Detected anomaly indices:", anomalies[:10])
