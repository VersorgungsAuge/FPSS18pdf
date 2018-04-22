import matplotlib.pyplot as plt
import numpy as np
import csv

x=[]
y=[]
#DAS HIER IST WIE SPAST2 NUR SCHLECHTER, OHNE NUMPY
with open('scope_198.csv') as csvfile:
	plots = csv.reader(csvfile, delimiter=",") #die einruekungen mit tab SIND NOTWENDIG
	for row in plots:
		x.append(float(row[0]))
		y.append(float(row[1]))

plt.plot(x,y, label="spastiker")
plt.xlabel("t/s")
plt.ylabel("U_A/V")
plt.title("titel spast")
plt.legend()
plst.show()