import moviepy
import moviepy.editor
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
from moviepy.editor import VideoFileClip, concatenate_videoclips



def cutvideo(video,ttime):
    stime1=0
    etime1=ttime/2.2
    ffmpeg_extract_subclip(video,stime1 , etime1, targetname="e1.mp4")
    
    v1 = VideoFileClip("e1.mp4")
    v2 = VideoFileClip("ad1.mp4")
    

    final_video= concatenate_videoclips([v1, v2])
    final_video.write_videofile("final.mp4")  




def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return hours, mins, seconds



video = moviepy.editor.VideoFileClip("episode.mp4")
video_duration = int(video.duration)
hours, mins, secs = convert(video_duration)
print("Hours:", hours)
print("Minutes:", mins)
print("Seconds:", secs)


cutvideo("episode.mp4",video_duration)

