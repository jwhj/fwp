from random import *
import cv2
import numpy as np
K=3
R=1
def func(a,f,S=0):
	f=np.array(f)
	n,m=a.shape[:2]
	if (n%2):
		n+=1
	if (m%2):
		m+=1
	a=cv2.resize(a,(m,n))
	f=cv2.resize(f,(m,n))
	a=cv2.dct(np.float32(a))
	f=f[::K,::K]
	if (S):
		seed(S)
		x,y=list(range(n//K)),list(range(m//K))
		shuffle(x)
		shuffle(y)
		f=f[x,:][:,y]
	f=np.pad(f,((n-n//K,0),(m-m//K,0)),'constant')
	a=a+f*R
	return cv2.idct(a)
def encode(a,f,S=0):
	b,g,r=cv2.split(a)
	fb,fg,fr=cv2.split(f)
	b=func(b,fb,S)
	g=func(g,fg,S)
	r=func(r,fr,S)
	return cv2.merge([b,g,r])
def func1(a,S=0):
	n,m=a.shape[:2]
	if (n%2):
		n+=1
	if (m%2):
		m+=1
	a=cv2.resize(a,(m,n))
	a=cv2.dct(np.float32(a))
	if (S):
		n,m=a.shape[:2]
		b=a[n-n//K::1,m-m//K::1]
		seed(S)
		x1,y1=list(range(n//K)),list(range(m//K))
		shuffle(x1)
		shuffle(y1)
		x,y=list(range(n//K)),list(range(m//K))
		for i in range(n//K):
			x[x1[i]]=i
		for i in range(m//K):
			y[y1[i]]=i
		b=b[x,:][:,y]-b
		b=np.pad(b,((n-n//K,0),(m-m//K,0)),'constant')
		a=a+b
	return a
def decode(a,S=0):
	b,g,r=cv2.split(a)
	b=func1(b,S)
	g=func1(g,S)
	r=func1(r,S)
	a=cv2.merge([b,g,r])/R
	return a
'''
def main():
	a=cv2.imread('a.jpg')
	f=cv2.imread('b.jpg')
	a=encode(a,f)
	cv2.imwrite('c.png',a)
	a=cv2.imread('c.png')
	c=decode(a)
	cv2.imwrite('d.png',c)

if __name__=='__main__': main()
'''