''' 
    Used to convert all images into 16X8 (or which ever size needed) .
    
    The images are saved as image_name.thumbnail
    The image name 064_0001.jpg has to be placed in dataset/064-0100(0100 Being the total number of images of type 064)
    The above image will be resized and saved in dataset-16x8/064-0100
''' 

import os, sys
import Image

size = 16, 8    #Required Size
iI="064"	#Image Id
cI="0100"	#Count Of Images Of That ID
if not os.path.exists("dataset-16x8/"+iI+"-"+cI+""):
	os.makedirs("dataset-16x8/"+iI+"-"+cI+"")
os.chdir("dataset-16x8/"+iI+"-"+cI+"")
lst=[]
for i in range(int(cI)):
	lst.append("../../dataset/"+iI+"-"+cI+"/"+iI+"_%04d.jpg"%(i+1))
for infile in lst:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im=im.resize(size, Image.ANTIALIAS)
            im.save(os.path.splitext(infile)[0].split("/")[-1]+".thumbnail", "JPEG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile