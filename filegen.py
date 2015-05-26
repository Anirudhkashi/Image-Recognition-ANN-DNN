'''File used to combine the individual image vectors into a single vector and add them to a file'''

import copy

letter= [0.0, 0.0, 0.0, 0.0]
XTr= []
YTr= []
XTe= []
YTe= []


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


	fp1= open("XTr.txt", "w")
	for i in range(len(XTr)):
		fp1.write(','.join([str(j) for j in XTr[i]]))
		fp1.write("\n")
	fp1.close()

	fp1= open("XTe.txt", "w")
	for i in range(len(XTe)):
		fp1.write(','.join([str(j) for j in XTe[i]]))
		fp1.write("\n")
	fp1.close()

	fp1= open("YTr.txt", "w")
	for i in range(len(YTr)):
		fp1.write(','.join([str(j) for j in YTr[i]]))
		fp1.write("\n")
	fp1.close()

	fp1= open("YTe.txt", "w")
	for i in range(len(YTe)):
		fp1.write(','.join([str(j) for j in YTe[i]]))
		fp1.write("\n")
	fp1.close()
	

def discretize(Y):
	
	for i in range(len(Y)):
		temp= copy.deepcopy(letter)
		temp[int(Y[i])]= 1.0
		Y[i]= temp

getData()
