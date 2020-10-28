#!/usr/bin/env python3

import moviepy.editor as mp


def convert_vs(vid_file, out_dir):
    clip = mp.VideoFileClip(vid_file) # mp4
    clip.audio.write_audiofile(out_dir + "/" + str(vid_file).rsplit("/", 1)[1].split(".")[0] + ".mp3") # mp3
    print(out_dir + "/" + str(vid_file).rsplit("/", 1)[1].split(".")[0] + ".mp3")

#convert_vs('/run/media/chaos/850 evo/Images/test_vid.mp4', '/run/media/chaos/850 evo/Images/Testing')