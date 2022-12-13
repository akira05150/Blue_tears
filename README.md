# Blue_tears

## Pre-Requisites
1. Open anaconda and activate your environment.
	```bash
	conda activate your_env
	```
2. Open the blue tears system directory.
	```bash
	cd ./Blue_tears
	```
3. Install all the required packages by type this command below:
	```bash
	pip install -r requirements.txt
	```

	> **NOTICE!** : If you could not install `dlib` by `pip/pip3` successfully, try `conda install dlib` under your environment.

4. Download all the data from google drive. Follow the [rules](#data-collection) as below.


## Instructions
1. To manipulate the sun: turn the knob to the 180 degrees
2. To turn on the light: open your palm
3. To turn off the light: close your palm
4. To pray for the blue tears: upper heart or down heart
5. To zoom in on the part of the blue tears: step closer to the picture (less than 50 cm)
	
	> :warning: 
	> After praying for the blue tears, you need to **wait for a few seconds** then the blue tears would show up.
	> While blue tears appeared, you **could not do anything** then. It will disappear after around 30 seconds. After then, you could manipulate everything again.

6. To play again, you have to wait for the sun to reverse back to 0 degrees. (You could not do anything until the sun back to the starting point.)
7. After then, you could back to step 1.


## Data Collection
- The size of the videos are large so we didn't upload them here, all the video are on our google drive. Download the materials from [here](https://drive.google.com/drive/u/0/folders/12hI5uB_-W8tm1z1VPcJoLmeoTQmb6mGd) before you run the program.
- Put them under the directory `./data/`, then rename `藍眼淚呈現v3.mp4` as `blue_tears_v3.mp4`, `燈塔轉動.mp4` as `rotate.mp4` and `陽光下的淚Sun.mp4` as `sun.mp4`.


## How to use?
- Scripts: 
	- `app.py`: server
	- `detection.py`: detect gesture and distance and display images/videos
	- `detect_gesture.py`: gesture recognition
	- `distacne.py`: distance measurement
- Usage: 
	```bash
	python app.py
	```
	And then paste `127.0.0.1:6200` to the browser.

## Reference
1. Mediapipe
2. Opencv
3. Kazuhito Takahashi, 2020 "hand-gesture-recognition-mediapipe". [Source code](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe)
4. Asadullah Dal, 2021 "Distance measurement using single1️⃣camera 📷". [Source code](https://github.com/Asadullah-Dal17/Distance_measurement_using_single_camera)
