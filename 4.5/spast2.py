import matplotlib.pyplot as plt
import numpy as np
import csv


with open("scope_198.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	for row in reader:
		print(row[0], row[1])

#terminal print in anderem file speichern: im terminal .....py > ...txt
#> ueberschreibt alles >> haengt hinten dran