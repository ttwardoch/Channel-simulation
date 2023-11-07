import numpy as np


def rayleigh_channel(x, sigma_r, sigma_n):
    """
    rayleigh_channel(x, sigma_r, sigma_n)
        Function simulating the Rayleigh Fading Channel.
            y = a*x + n

        Parameters
        ----------
        x: 1-D array-like or float
            an input array or value for the channel
        sigma_r: float
            a value of sigma for Rayleigh distribution of a
        sigma_n: float
            a value of sigma for Gaussian distribution of n

        Returns
        -------
        out : 1-D array-like or float (like x)
            output of the channel
    """
    n = x.size
    a = np.random.rayleigh(scale=sigma_r, size=n)
    norm = np.random.normal(loc=0.0, scale=sigma_n, size=n)
    return a * x + norm


def isi_channel(x, h, sigma_n):
    """
    isi_channel(x, h, sigma_n)
        Function simulating the Inter-Symbol Interference Channel.
            y = convolve(h*x) + n

        Parameters
        ----------
        x: 1-D array-like or float
            an input array or value for the channel
        h: 1-D array-like or float
            channel impulse response
        sigma_n: float
            a value of sigma for Gaussian distribution of n

        Returns
        -------
        out : 1-D array-like or float (like x)
            output of the channel
    """
    n = x.size
    convolved = np.convolve(x, h)[:-(h.size-1)]
    norm = np.random.normal(loc=0.0, scale=sigma_n, size=n)
    return convolved + norm


def generate_h_for_isi_channel(n, sigma_h=1, alfa=1, sign="mixed"):
    """
    generate_h_for_isi_channel(n, sigma_h=0.3, alfa=2, sign="mixed")
        Function generating random impulse response for an Inter-Symbol Interference Channel.
            h

        Parameters
        ----------
        n: int
            number of elements n >= 1
        sigma_h: float
            channel impulse response
        alfa: float
            the decrease in sigma_h for each further element
        sign: basestring
            decide if h should be "mixed" of "positive" only

        Returns
        -------
        out : 1-D array-like or float (length n)
            impulse response for the channel

        Raises
        ------
        ValueError
            If n is not an int or is less than 1
            If alfa = 0
    """
    if n < 1:
        raise ValueError
    if type(n) is not int:
        raise ValueError
    if alfa == 0:
        raise ValueError

    h = [1, ]
    for i in range(n-1):
        h_new = np.random.normal(loc=0.0, scale=sigma_h)
        h.append(h_new)
        sigma_h /= alfa

    h = np.array(h)

    if sign == "positive":
        h = np.abs(h)

    return h
