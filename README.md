# Smart doorbell
Find out who is ringing your door bell and pass on personalized messages to your visitors when you are not at home. 

## Getting started
This application uses [Clarifai's face embedding model](https://clarifai.com/models/face-embedding-image-recognition-model-d02b4508df58432fbb84e800597b8959). You can create a free account [here](https://clarifai.com/developer/) to get an api key. 

In order to use the smart doorbell you have to create a hidden file (**you never want to share this information**) containting your api key:
```console
foo@bar:~$ echo "your api key" > .clarifai_api_key.txt 
```

### Prerequisites

The code is based on the following packages that have to be installed in advance:
* NumPy
* OpenCV
* Clarifai 

### Running the test

In order to test the application, I have created Anon's frienst list including:
* Angela Merkel
* Angelique Kerber
* Barack Obama
* Cristiano Ronaldo
* DeMar DeRozan
* LeBron James
* Jimmy Kimmel
* Marie Curie
* Messi
* Richard Feynman

You can now test if the doorbell works by:
```console
foo@bar:~$ echo python3 doorbell.py 
```
* Press *Quit* in the first textbox
* Press *l* and type test_friend_list/friend_list_anon
* A message should pop up saying that the friend list has been loaded
* Show a picture of either of Anon's friends to your webcam and press *c*
* A message for Anon's frined (e.g. **Hello Marie**) should pop up

## Comming soon

The face embedding is based on the Euclidean distance of the 1024-dimensional image representation. If this distance between two faces is less than **0.85** the doorbell treat them as the same person. I am working on a neural network (similar to [FaceNet](https://arxiv.org/abs/1503.03832) ) using the database [Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) that should drastically improve the current solution.
