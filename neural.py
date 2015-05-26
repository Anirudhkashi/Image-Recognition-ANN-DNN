'''
	The neural network implementation of detecting the objects in the image.
	We got an efficiency of 77%.

'''


import neurolab as nl
import numpy
import copy


XTr= []
YTr= []
XTe= []
YTe= []
letter= [float(0) for i in range(4)]
inp= [[0.0, 1.0]]* 384
net= nl.net.newff(inp, [10, 4], transf= [nl.trans.TanSig(), nl.trans.SoftMax()])

def getData():

	global XTr
	global YTr
	global YTe
	global XTe
	X=[]
	Y=[]

	fp= open("064.txt", "r")
	for line in fp:
		line= line.strip("\n").split(',')
		X.append(line)
		Y.append("0")

	fp.close()

	discretize(Y)

	for i in range(len(X)):
		X[i]= [float(j) for j in X[i]]

	XTe= copy.deepcopy(XTe)+copy.deepcopy(X[70:])
	YTe= copy.deepcopy(YTe)+copy.deepcopy(Y[70:])
	XTr= copy.deepcopy(XTr)+copy.deepcopy(X[:70])
	YTr= copy.deepcopy(YTr)+copy.deepcopy(Y[:70])

	X=[]
	Y=[]

	fp= open("105.txt", "r")
	for line in fp:
		line= line.strip("\n").split(',')
		X.append(line)
		Y.append("1")

	fp.close()

	discretize(Y)

	for i in range(len(X)):
		X[i]= [float(j) for j in X[i]]

	XTe= copy.deepcopy(XTe)+copy.deepcopy(X[105:])
	YTe= copy.deepcopy(YTe)+copy.deepcopy(Y[105:])
	XTr= copy.deepcopy(XTr)+copy.deepcopy(X[:105])
	YTr= copy.deepcopy(YTr)+copy.deepcopy(Y[:105])


	X=[]
	Y=[]

	fp= open("129.txt", "r")
	for line in fp:
		line= line.strip("\n").split(',')
		X.append(line)
		Y.append("2")

	fp.close()

	discretize(Y)

	for i in range(len(X)):
		X[i]= [float(j) for j in X[i]]

	XTe= copy.deepcopy(XTe)+copy.deepcopy(X[105:])
	YTe= copy.deepcopy(YTe)+copy.deepcopy(Y[105:])
	XTr= copy.deepcopy(XTr)+copy.deepcopy(X[:105])
	YTr= copy.deepcopy(YTr)+copy.deepcopy(Y[:105])


	X=[]
	Y=[]

	fp= open("145.txt", "r")
	for line in fp:
		line= line.strip("\n").split(',')
		X.append(line)
		Y.append("3")

	fp.close()

	discretize(Y)

	for i in range(len(X)):
		X[i]= [float(j) for j in X[i]]

	XTe= copy.deepcopy(XTe)+copy.deepcopy(X[350:])
	YTe= copy.deepcopy(YTe)+copy.deepcopy(Y[350:])
	XTr= copy.deepcopy(XTr)+copy.deepcopy(X[:350])
	YTr= copy.deepcopy(YTr)+copy.deepcopy(Y[:350])

	print(len(XTr))
	train()

	test()

def discretize(Y):
	
	#Converts output into one-hot representation

	for i in range(len(Y)):
		temp= copy.deepcopy(letter)
		temp[int(Y[i])]= 1.0
		Y[i]= temp


def getWeights():

	#This function writes the weights for visualization later.

	fp= open("weight1.txt", "w")
	for i in range(len(net.layers[0].np['w'])):
		fp.write(','.join([str(j) for j in net.layers[0].np['w'][i]]))
		fp.write("\n")

	fp.close()

	fp= open("weight2.txt", "w")
	for i in range(len(net.layers[1].np['w'])):
		fp.write(','.join([str(j) for j in net.layers[1].np['w'][i]]))
		fp.write("\n")
	fp.close()


def train():
	global net
	err = net.train(XTr, YTr, show=1)

def test():

	global net
	ret= list(net.sim(XTe))

	count= 0
	totalCount= len(ret)


	for i in range(len(ret)):
		flag=1
		ret[i]= list(maxed(ret[i]))
		for j in range(len(ret[i])):
			if(ret[i][j]!= YTe[i][j]):
				flag=0
				break
		if(flag):
			count=count+1

	accuracy= (float(count)/float(totalCount))*100.0
	print str(accuracy)+ "%"


def maxed(lst):
	maxVal= lst[0]
	maxIndex= 0
	for i in range(len(lst)):
		if(lst[i]> maxVal):
			maxIndex= i
			maxVal= lst[i]

	for i in range(len(lst)):
		if(i== maxIndex):
			lst[i]= 1.0
		else:
			lst[i]= 0.0

	return lst

getData()
getWeights()