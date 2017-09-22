import numpy as np
import requests
from skimage import io
import matplotlib.pyplot as plt
from __future__ import division
from scipy.misc import imresize

width = 50
dark = True
debug = False

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/M101_hires_STScI-PRC2006-10a.jpg/1280px-M101_hires_STScI-PRC2006-10a.jpg"
#url = "https://pbs.twimg.com/profile_images/707025898222936064/hs3oOROZ.jpg"
url = "http://i0.kym-cdn.com/entries/icons/original/000/009/556/jesus-bleu-mauve.jpg"
url = "https://i.pinimg.com/736x/24/b6/14/24b6146e74288878ccd010614d4f71d9--simple-paintings-image-of-jesus.jpg"
url = "emily.jpg"
a = io.imread(url)

chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))


if debug:
	#quick plot
	plt.imshow(a)
	plt.show()

gray = np.mean(a,-1) #average values to get gray

scaling = width/gray.shape[1] #limit on characters in x-axis
newsize = (int(gray.shape[0]*scaling),int(gray.shape[1]*7/4*scaling))

#resize

little = imresize(gray,newsize)

#normalize
if dark:
	img = dark = (little/little.max())*(chars.size-1)
else:
	img = light = (1.0 - little/little.max())*(chars.size-1)

print( "\n".join(("".join(r) for r in chars[img.astype(int)])))