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
		#if self.phase >= (2*np.pi):
		#	self.phase = 0 
		self.phase += freq + kn*np.sin(ang-self.phase)
		return self.phase 
	def showPhase(self): 
		print self.phase 
		return self.phase

plt.ion()
fig,axarr = plt.subplots(1,sharex=True) 
myosc = oscillator(0, 0.0) 

oscs = []
ifreqs = [] 
kn = 0.8  # no coupling, for tesing
for i in range(0,10): 
	ifreqs.append(random.random()/10)


# create 10 new oscillators
for i in range(0,10):
	oscs.append(oscillator(i, random.random()*2*np.pi)) # random initial phases 



while(True):
	plt.ylim([-1.1,1.1])
	plt.xlim([-1.1, 1.1])
	axarr.set_ylim([-1.1,1.1])
	tempPh = []
	r = 0
	for osc in oscs:
		tempPh.append(osc.showPhase())
		myphase = osc.showPhase()
		r += (np.cos(myphase) + 1j*np.sin(myphase) )

	tempPh = np.array(tempPh)
	rcirc = np.exp(-1j*tempPh)

	r /= len(oscs) 
	rang = np.arctan(np.imag(r)/np.real(r)) 

	if (np.real(r) < 0 and np.imag(r) > 0):
		rang  += np.pi 
	elif (np.real(r) < 0 and np.imag(r) < 0): 
		rang += np.pi 
	elif (np.real(r) > 0 and np.imag(r) < 0): 
		rang += 2*np.pi
	
	for i in range(0,10):
		oscs[i].addFreq(ifreqs[i], rang, kn) 

	x0,x1 =axarr.get_xlim()
	y0,y1 = axarr.get_ylim() 
	axarr.set_aspect(abs(x1-x0)/abs(y1-y0)) 
	axarr.grid(b=True, which='major', color='k', linestyle='--') 

	plt.scatter(np.real(rcirc), np.imag(rcirc)) 
	plt.pause(0.0001)

	#sumPh = sum(tempPh) 
	#sumPh /= len(oscs) 
	#sumPh = np.cos(
	#print "temporary phases: ", tempPh

	#for x,y in itertools.combinations(tempPh, 2): 
	#	print x,y
	plt.cla()
	time.sleep(0.06)
	print "\n \n "


