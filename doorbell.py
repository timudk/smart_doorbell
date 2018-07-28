import numpy as np
import cv2 

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

from text_box import Textbox
from distance_functions import L2

from tkinter import Tk, Button

class Doorbell():
	def __init__(self):
		self.read_api_key()
		self.model = self.api_key.models.get('d02b4508df58432fbb84e800597b8959') 

		self.friends = []

		self.show_message = 0

	def read_api_key(self):
		with open('.clarifai_api_key.txt', 'r') as file:
			key = file.read().splitlines()
			self.api_key = ClarifaiApp(api_key=key[0])

	def start_message(self, frame):

		message = 'Hello their.\nAdd a new friend by pressing f.\nCheck who is in front of your door by pressing c.\nPress h to see this message.'
		y0, dy = 50, 50
		for i, line in enumerate(message.split('\n')):
			y = y0 + i*dy
			cv2.putText(frame, line, (50, y), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)

		cv2.imshow('Video', frame)

	def friend_message(self, frame):
		message = 'Hello {}'.format(self.friend_name)

		cv2.putText(frame, message, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
		cv2.imshow('Video', frame)

	def no_friend_message(self, frame):
		message = 'It seems like you have not been added to the friend list yet.'

		cv2.putText(frame, message, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
		cv2.imshow('Video', frame)


	def add_friend(self, frame):
		friend = Textbox()

		friend_img_name = 'friend_{}.png'.format(friend.TempVar)
		cv2.imwrite(friend_img_name, frame)
		print('{} written!'.format(friend_img_name))

		self.friends.append([friend.TempVar, self.extraxt_embedding(friend_img_name)])

	def extraxt_embedding(self, filename):
		usr_img = ClImage(filename=filename)
		usr_img_pred = self.model.predict([usr_img])
		while True:
			try:
				face_embedding = usr_img_pred['outputs'][0]['data']['regions'][0]['data']['embeddings'][0]['vector']
				return face_embedding
			except KeyError:
				print ("Oops!  That was no valid number.  Try again...")

	def check_friend(self, frame):
		img_name = 'tmp.png'
		cv2.imwrite(img_name, frame)
		print("{} written!".format(img_name))

		differences = []
		for friend in self.friends:
			test_img = ClImage(filename=img_name)
			test_img_pred = self.model.predict([test_img])
			while True:
				try:
					pic2 = test_img_pred['outputs'][0]['data']['regions'][0]['data']['embeddings'][0]['vector']
					break
				except KeyError:
					print ("Oops!  That was no valid number.  Try again...")

			differences.append(L2(pic2, friend[1]))

		if min(differences) < 0.8:
			self.friend_name = self.friends[differences.index(min(differences))][0]
			self.show_message = 1
		else:
			self.show_message = 2

	def start_doorbell(self):
		cam = cv2.VideoCapture(0)
		cv2.namedWindow("Smart doorbell")

		while True:
			ret, frame = cam.read()

			if not ret:
				break

			k = cv2.waitKey(1)

			if self.show_message==0:
				self.start_message(frame)
			elif self.show_message==1:
				self.friend_message(frame)
			elif self.show_message==2:
				self.no_friend_message(frame)

			if k%256 == 27:
				# ESC pressed
				print("Escape hit, closing...")
				break

			elif k%256 == 102:
				# f pressed
				show_start_message = False
				print('Adding a new friend.')
				self.add_friend(frame)

			elif k%256 == 104:
				# h pressed
				self.show_start_message = 1

			elif k%256 ==99:
				# c pressed
				self.check_friend(frame)

def main():
	master = Tk()
	Button(master, text="Quit", command=master.destroy).pack()
	master.mainloop()

	doorbell = Doorbell()
	doorbell.start_doorbell()

if __name__ == '__main__':
    main()


