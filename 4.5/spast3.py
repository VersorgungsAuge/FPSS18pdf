import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy as sp
import csv
import matplotlib.ticker as plticker

x,y = np.genfromtxt("gedaempft_werte_alles_vor_t=0_geloescht.txt", unpack=True)
#werte vor t=0 muessen gekoescht werden, sonst st der fit eher ne gerade, weil der fehler so minimiert ist
plt.plot(x,y, "rx", label="Messwerte")
plt.xlabel("$t/s$")
plt.ylabel("$U_A/V$")
#plt.title("gedaempfte schwingung h), also ausgangsspannung U_A als funktion der zeit")

#xmarks macht aufeinmal nix mehr??
#xmarks=np.arange(-0.01, 0.05+0.001, 0.01)#wie np.range nur mit floats,
#plt.xticks(xmarks)# legt x achsen beschriftung anfang ende und abstaende fest

'''
def U_A(t,U0,phi,w,b):
	return U0*np.sin(w*t+phi)*np.exp(-b*t)
popt, pcov = curve_fit(U_A, x, y)
print (popt)

def f(t):
	return popt[0]*np.sin(popt[2]*t+popt[1])*np.exp(-popt[3]*x)
plt.plot(x, f(x), "b-", label="Fit")
'''
#IDENTISCH ZU (EINFACHER)

def fit(x,A,phi,w,b):
	return A*np.sin(w*x+phi)*np.exp(-b*x)#verschiebung phi muss dazu sein, weil er sons bei t=0 nur durch 0 gehen kann

params, covariance = curve_fit(fit,x,y)
errors = np.sqrt(np.diag(covariance))

print ("U0=",params[0],"+-",errors[0],"   ", "omega=",params[2],"+-",errors[2],"   ", "b=",params[3],"+-",errors[3],"   ", "phi=",params[1],"+-",errors[1])#fitvariableen mit absolutem fehler
plt.plot (x, fit(x,*params), "b-", label="Fit")#plot fertige fitfkt/ausgleichfkt

plt.plot(x, params[0]*np.exp(-params[3]*x), "g-", label="Daempfung")#nur die daempfung/e-fkt
#U0*np.exp(-b*x) geht nicht, weil b und U0 nicht definiert
#ok, nur die daempfung ist e fkt ohne amplitude als vorfaktor


'''
def U_A(t,eta,RC,U0,versch): #RC, eta eine variable, name kann natuerlich ganzes wort sein
	return U0*np.exp((eta*(t+versch))/(20*RC))*np.sin((t+versch)/RC)
popt, pcov = curve_fit(U_A, x, y, p0=(-1,0.0001,0.04,1)) #popt[0] ist eta, popt[1] ist RC usw.
#erstes argument ist funktion die an x,y wertepaare (mit fehler) geplottet werden soll, dann die x werte, dann y werte, immer muss so sein natuerlich
#p0() legt startwerte fuer asugleichvariablen fest (standart alles 1), also erstes argument ist eta usw, snytax p0=() wird so erkannt
print (popt)

def f(t):
	return popt[2]*np.exp((popt[0]*(t+popt[3]))/(20*popt[1]))*np.sin((t+popt[3])/popt[1])
plt.plot(x, f(x), "r-", label="Fit")
#def U_A_Ausgleich(t,popt[0],popt[1],popt[2]):
	#return U_A(t, popt[0], popt[1], popt[2])
#plt.plot(x, U_A_Ausgleich, "b-", label="Fit")
DAS FUNKTIONIERT ALLES NICHT (PROGAMIERUNG RICHTIG), WEIL BEI FITFKT 
SOWAS WIE e^(a/b) WAR, WOBEI ABER NICHT a ODER b DEFINIERT, DAS HEIST BEIDE SIND VARIABEL BEIM FIT, ALSO WEIS ER NICHT, WIE MAN DIE GEWICHTEN SOLL
'''

plt.grid()
#plt.yscale("log")#logarithmische y achse
plt.legend(loc= "best")
plt.tight_layout()#wird so gemacht, dass graph erster und letzter wert genau an bildgrenze sind, und in y achse auch weniger platz lassen bis zum graphen
#plt.show()
plt.savefig("gedaempft.pdf")


fig=plt.gcf()
fig.set_size_inches(50, 10.5)#x y groesse beliebig aendern, herbe gut
fig.savefig("drool.pdf", dpi=100)#macht eigneltich nur pdf, genau wie plt.savefig