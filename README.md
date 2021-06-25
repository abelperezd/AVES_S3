### Repository information
In this repository we find the delivery of the seminar 3 of the Audio and Video Encoding Systems subject (video part).

In order to use it correctly we need the video "Big Buck Bunny", included in the repository.

We have 4 .py files and in each of them we find a detailed explanation on how to use them:


## **ex1.py**
We get the above video in 4 new formats*:
- 720p resolution with vp8 video codec.
- Resolution 480p with video codec vp9.
- Resolution 360x240 with .h265 video codec.
- Resolution 160x120 with video codec av1.

*The formats are not exactly the defined ones since I have prioritized to conserve the aspect ratio. In case you want to force it you can use the following code:

`$ ffmpeg -i <input_video> -s 720x480 <output_video>`.


## **ex2.py**
After running the above script, we can pack all the obtained videos into a single container (4 video and 4 audio channels).

<img src="https://drive.google.com/uc?export=view&id=1uOJt5dCAuRYckoc0V5GL0OzgB60ha037" width="600">

Through a video player such as VLC we can switch between the different formats. We can observe how, for example, 480p video with vp9 codec is seen with higher quality than 720p video with vp8 codec. This may be due to the compatibility between codecs and container type.


## **ex3.py**
In this script we perform a steaming in the local network of the video generated in the previous script. In order to view it we simply have to access the url through which we share it.

<img src="https://drive.google.com/uc?export=view&id=1bhuSNG4dfAXGMzM5dHiu7ZUqkKUk0wn1" width="300" height ="200"> <img src="https://drive.google.com/uc?export=view&id=1Vw9Bos3Ut5B-6EatIxWLux96EKwWx7uj" width="300" height ="200">


## **ex4.py**
In this script we find a menu that allows us to select which of the above scripts we want to run.

<img src="https://drive.google.com/uc?export=view&id=19B9Q_6w9t7t89fs0w0-kmlUP8ZtRP7O2" width="300">
