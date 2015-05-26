
''' This is the stacked autoencoder taking its weights from the autoencoders which have been trained
 	previously (in layer.py file)

'''

import neurolab as nl
import numpy

XTr= []
YTr= []
XTe= []
YTe= []
W4=[]
W5=[]
# W3=[]

def calcH(x):
        """Return the output of the network if ``a`` is input."""
        x=[x]
        x=numpy.array(x)
        x=numpy.transpose(x)
        h=numpy.add(numpy.transpose(numpy.array(numpy.dot(net.layers[0].np["w"],x))),numpy.array(net.layers[0].np["b"]))
        h=sigmoid_vec(numpy.transpose(h))
        return h

def sigmoid(z):
	#Tansig
    return 2.0/(1.0+numpy.exp(-2*z))-1

sigmoid_vec = numpy.vectorize(sigmoid)

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

def train():
	global net
	err = net.train(XTr, YTr, epochs= 10, show=1)

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


inp= [[0.0, 1.0]]* 384
net= nl.net.newff(inp, [8,4],transf= [nl.trans.TanSig(),nl.trans.SoftMax()])


#Following four are the training and testing data stored in respective files.

fp= open("XTr.txt", "r")
for line in fp:
	line= line.strip().split(",")
	line= [float(j) for j in line]
	XTr.append(line)

fp= open("YTr.txt", "r")
for line in fp:
	line= line.strip().split(",")
	line= [float(j) for j in line]
	YTr.append(line)

fp= open("XTe.txt", "r")
for line in fp:
	line= line.strip().split(",")
	line= [float(j) for j in line]
	XTe.append(line)

fp= open("YTe.txt", "r")
for line in fp:
	line= line.strip().split(",")
	line= [float(j) for j in line]
	YTe.append(line)


#Following three are the weights

fp= open("W4.txt", "r")
for line in fp:
	line= line.strip().split(",")
	line= [float(j) for j in line]
	W4.append(line)

fp= open("W5.txt", "r")
for line in fp:
	line= line.strip().split(",")
	line= [float(j) for j in line]
	W5.append(line)

# fp= open("W3.txt", "r")
# for line in fp:
# 	line= line.strip().split(",")
# 	line= [float(j) for j in line]
# 	W3.append(line)

#Setting of initial weights from those gotten from the autoencoders

net.layers[0].np['w'][:]=W4
net.layers[1].np['w'][:]=W5
# net.layers[2].np['w'][:]=W3

train()
test()

print "Done"