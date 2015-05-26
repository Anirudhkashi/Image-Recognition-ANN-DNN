''' 
	Used to visualize the weight vectors using matplotlib.
'''

import numpy
import matplotlib.pylab as plt

lst=[]
fo = open("W3.txt", "r+") # Replace this with the name of weight vector. (Here, W1.txt, W2.txt, W3.txt, weight1.txt, weight2.txt)
st=fo.readline()
while (st):
	st=st.strip('\n')
	li=st.split(",")
	ls=[float(i) for i in li]
	lst.append(ls)
	st=fo.readline()

#print lst
matrix = numpy.matrix(lst)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_aspect('equal')
plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.ocean,  extent=(0.5,10.5,0.5,10.5))
plt.colorbar()

plt.show()

	
	

