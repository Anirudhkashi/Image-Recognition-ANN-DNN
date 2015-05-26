''' This file vectorizes the images into vectors. 
	Also, the RGB values are normalized.

	It saves all images of type 064 into the file dataset-16x8/064-0100/064.txt

	That file will be used in the continuing process and has to be copied into the same file as neural networks directory.
'''

import Image, os

def normVec(vec):
	#Required Size As xN x yN
	xN=16
	yN=8
	for i in range(yN):
		for j in range(xN):
			vec[i][j]=list(vec[i][j])
			vec[i][j][0]/=255.0
			vec[i][j][1]/=255.0
			vec[i][j][2]/=255.0
	return vec

iI="145"	#Image Id
cI="0499"	#Count Of Images Of That ID
lst=[]
for i in range(int(cI)):
	lst.append(iI+"_%04d.thumbnail"%(i+1))
os.chdir("dataset-16x8/"+iI+"-"+cI+"")
fp=open(iI+".txt","w")
for img in lst:
	im = Image.open(img)
	im=im.convert("RGB")
	pixels = list(im.getdata())
	width, height = im.size
	pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
	norm=normVec(pixels)
	opLst=[str(k) for i in norm for j in i for k in j]
	fp.write(','.join(opLst))
	fp.write("\n")