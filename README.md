# Smart doorbell
Find out who is ringing your door bell and pass on personalized messages to your visitors when you are not at home. 

## Getting started
This application uses [Clarifai's face embedding model](https://clarifai.com/models/face-embedding-image-recognition-model-d02b4508df58432fbb84e800597b8959). You can create a free account [here](https://clarifai.com/developer/) to get an api key. 

In order to use the smart doorbell you have to create a hidden file containting your api key:
```console
foo@bar:~$ echo "your api key" > .clarifai_api_key.txt 
```
