import numpy as np 
import keras

def L2(img1, img2):
	diff = 0
	for i in range(1, len(img1)):
		diff += (img1[i]-img2[i]) * (img1[i]-img2[i])

	diff = np.sqrt(diff)
	return diff

def neural_network(img1, img2):
	nn = keras.models.load_model('neural_network/face_model_L2.h5')

	diff = []
	for i in range(0, len(img1)):
		diff.append((img1[i]-img2[i]) * (img1[i]-img2[i]))

	diff = np.array(diff)[np.newaxis]
	
	prediction = nn.predict(diff)
	print(prediction[0][0])

	return (1-prediction[0][0])
