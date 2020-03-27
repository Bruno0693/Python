import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt




def valeur_k():
	k = input("Entrez la valeur de k : ")
	k = float(k)
	return k


def truc(y,t, k):
	dydt = -k*y
	return dydt

def figure():
	plt.plot(t,y)
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

y0 = 5

t = np.linspace(0,20)

c = 0

while c==0:
	k = valeur_k()
	y = odeint(truc, y0, t, args=(k,))
	figure()
	c=recommencer()







