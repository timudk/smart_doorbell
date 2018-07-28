import numpy as np 

def L2(img1, img2):
	diff = 0
	for i in range(1, len(img1)):
		diff += (img1[i]-img2[i]) * (img1[i]-img2[i])

	diff = np.sqrt(diff)
	return diff