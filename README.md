# Blue_tears

## Instructions
- To turn on the light: open your palm
- To turn off the light: close your palm
- To pray for the blue tears: upper heart or down heart

	> :warning: 
	> You need to **wait for a few seconds**, then the blue tears appeared.
	> While blue tears appeared, you **could not do anything** then. It will disappear after around 30 seconds. After then, you could manipulate everything again.


## Data Collection
- The size of the videos are large so we didn't upload them here, all the video are on our google drive. Download the materials from [here](https://drive.google.com/drive/u/0/folders/12hI5uB_-W8tm1z1VPcJoLmeoTQmb6mGd) before you run the program.
- Put them under the directory `./data/`, then rename `藍眼淚呈現v2.mp4` as `blue_tears_v2.mp4` and `燈塔轉動.mp4` as `rotate.mp4`.


## How to use?
- Scripts: 
	- `app.py`: server
	- `detect_gesture.py`: detect gesture and distance
	- `distacne.py`: distance measurement
- Usage: 
	```bash
	python app.py
	```

## Reference
1. Mediapipe
2. Opencv
3. Kazuhito Takahashi, 2020 "hand-gesture-recognition-mediapipe". [Source code](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe)
