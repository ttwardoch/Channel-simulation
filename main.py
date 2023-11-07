import numpy as np
import matplotlib.pyplot as plt
from channels import *


# Set constants
n = 1000000
sigma_r = 1
sigma_n = 1
r = 1

errors = []
SNRs = []
h = generate_h_for_isi_channel(50, sigma_h=0.3, alfa=2)
print(h)
for log_x_strength in np.linspace(-2, 4, 61):
    x_strength = 10 ** log_x_strength

    data = np.random.choice((-1, 1), size=n)  # Generate bits using BPSK (-1 or 1)
    x = x_strength * data  # Set amplitude
    # y = rayleigh_channel(x, sigma_r, sigma_n)  # Find channel output
    # y = rice_channel(x, r, sigma_r, sigma_n)  # Find channel output
    y = isi_channel(x, h, sigma_n)  # Find channel output

    # Find SNR and error rate, it is BPSK, and it is symmetrical so all positive act as 1 and negative as -1
    data_out = np.array([i/abs(i) for i in y])
    error = n/2 - np.dot(data, data_out)/2
    snr = x_strength**2 / sigma_n**2

    # Add data for plotting
    errors.append(error/n)
    SNRs.append(snr)

# Plot Pe vs SNR
plt.plot(SNRs, errors)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("SNR")
plt.ylabel("Pe")
plt.title("Probability of error given the SNR")
plt.grid()
plt.show()
