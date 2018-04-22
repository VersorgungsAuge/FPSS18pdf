import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy as sp
import csv
import matplotlib.ticker as plticker

x,y = np.genfromtxt("gedaempft_werte_alles_vor_t=0_geloescht.txt", unpack=True)

plt.xlabel("$t/s$")
plt.ylabel("Daempfung")
#plt.title("Daempfung der gedaepften Schwingung")

plt.plot(x, np.exp(-138.53*x), "g-", label="Daempfung")

plt.grid()
plt.yscale("log")
plt.legend(loc= "best")
plt.tight_layout()
plt.savefig("gedaempft_daempfung.pdf")

