# Created by Matt G. Chiu — Eastman School of Music
# mchiu9@u.rochester.edu / matthewgychiu@gmail.com (860)682–3832
# functions for calculating manualArrays
# If you would like to use the functions or code, please contact me

from music21 import *
import numpy as np
import math
from numpy.linalg import norm

# ------------------------------------------------------------------------------------------------------------
#Log-Weight Collection
def Log_Weight(x):
	for counter, i in enumerate(x):
		x[counter] = math.log(i+1, 2)
	return x

# DFT Calculation
# For Complex, and separated magnitude/phase elements
def DFT_Calculation(array):
	magnitudeArray = []
	phaseArray = []
	DFTArray = []
	DFTArray.append(np.fft.fft(array))
	magnitudeArray.append(np.absolute(DFTArray))
	phaseArray.append(np.angle(DFTArray))
	return DFTArray, magnitudeArray, phaseArray

# ------------------------------------------------------------------------------------------------------------

# JUST FOR ROUNDING PHASE
def roundToClosebyRadian(angle,N):
	rounded = round(angle*(N/(2*math.pi)))/(N/(2*math.pi))
	return rounded

def modSpace(n, component):
	modSpace = []
	positions = 12
	cycle = 0
	for y in range(n):
		solve = (component*y)%n
		# for n2 in range(n):
		if solve==0:
			cycle+=1
	numberOfPositions=positions/cycle
	if component==0:
		numberOfPositions=n
	return numberOfPositions
# print(modSpace(576, 0))
# print(modSpace(12, 3))



