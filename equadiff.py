import numpy as np
from math import * 
from scipy.integrate import odeint
import matplotlib.pyplot as plt




def valeur_k():
	k1 = input("Entrez une valeur de k : ")
	k2 = input("Entresz une seconde valeur de k : ")
	k1 = float(k1)
	k2 = float(k2)
	return (k1,k2)

def conditionInitiale():
	Y = input("Entrez la condition initiale y_0 : ")
	return Y


def truc(y,t, k):
	dydt = -k*t*y
	return dydt

def figure():
	plt.plot(t,y1)
	plt.plot(t,y2)
	plt.xlabel('time')
	plt.ylabel('y(t)')
	plt.show()
	
def recommencer():
	c1 = 0
	while c1 == 0:
		s = input("Voulez-vous recommencer (O/N) ? ")
		if (s =='O' or s == 'N'):
			c1 = 1
		else:
			print("Vous devez entrer O ou N")
			c1 = 0

	if s=='O':
		c=0
		return c
	elif s=='N':
		c=1
		return c


t = np.linspace(0,20, 200)

c = 0

while c==0:
	(k1, k2) = valeur_k()
	y0 = conditionInitiale()
	y1 = odeint(truc, y0, t, args=(k1,))
	y2 = odeint(truc, y0, t, args=(k2,))
	figure()
	c=recommencer()







