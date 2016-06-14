#!/usr/bin/env python

import numpy as np
import time
import random 
import itertools
import matplotlib.pyplot as plt

class oscillator(object): 
	def __init__(self, id, phase): 
		"""return an oscillator object whose name is *name* and starting phase is *phase*""" 
		self.id =  id
		self.phase = phase 
	def addFreq(self, freq, ang, kn): 
		""" add initilized freq to phase"""
		self.phase += freq
		self.phase += kn*np.sin(ang-self.phase)
		self.phase %= (2*np.pi) 
		return self.phase 
	def showPhase(self): 
		print self.phase 
		return self.phase

plt.ion()
fig = plt.figure() 
plt.axis([0, 2*np.pi, 0, 2*np.pi]);

myosc = oscillator(0, 0.0) 

oscs = []
ifreqs = [] 

for i in range(0,10): 
	ifreqs.append(random.random())


# create 10 new oscillators
for i in range(0,10):
	oscs.append(oscillator(i, random.random()*2*np.pi)) # random initial phases 


while(True):
	tempPh = []
	r = 0
	for osc in oscs:
		tempPh.append(osc.showPhase())
		myphase = osc.showPhase()
		r += (np.cos(myphase) + 1j*np.sin(myphase) )

	plt.plot(tempPh) 

	r /= len(oscs) 
	rang = np.arctan(np.real(r)/np.imag(r)) 
	
	for i in range(0,10):
		oscs[i].addFreq(ifreqs[i], rang, 0.01) 

	#sumPh = sum(tempPh) 
	#sumPh /= len(oscs) 
	#sumPh = np.cos(
	#print "temporary phases: ", tempPh

	#for x,y in itertools.combinations(tempPh, 2): 
	#	print x,y

	time.sleep(0.3)
	print "\n \n "


