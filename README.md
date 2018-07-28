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

In order to test the application, I have created Anon's frienst list:
<ul>
    <li><img src="https://github.com/timudk/smart_doorbell/blob/master/test_friend_list/images/friend_angela.jpg"></li>
    <li><img src="https://github.com/timudk/smart_doorbell/blob/master/test_friend_list/images/friend_angelique.jpg"></li>
</ul>
