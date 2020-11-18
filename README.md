# VideoCoding_S2
## Seminar 2 of Video Coding: More ffmpeg

**Task 1:** Cut 10 seconds of the BBB video.

**Task 2:** Extract the YUV histogram from the previous BBB video you’ve done and create a new video with both images at the same time.

**Task 3:** Resize the BBB video into 4 different video outputs (doesn’t need to be at the same time):

* 720p
* 480p
* 360x240
* 160x120

**Task 4:** Change the audio into mono output and in a different audio codec.

### Requirements
	ffmpeg, Python3

### Executing
Run Video_editor.py in the same folder as the video you want to edit, you can have several videos in the folder.

Before every edition it will show the .mp4 files in the folder, and will ask which file you want to edit. Enter the option via the number besides the video.

In the menu you can choose which of the tasks defined above you want to realize entering the number beside the option.

* Task 1: Trim a video (10 seconds if you want)

	1.	Enter the starting timestep of the trim in the format **hh:mm:ss**.
	1. 	Enter the duration of the trim.

* Task 2: Get a copy of the input video with the YUV histogram overlayed.
* Task 3: Resize video in the formats mentioned.
	* Enter the format you want via the number beside the option.
* Task 4: Get a copy of the input video with the audio in AAC format and mono.
