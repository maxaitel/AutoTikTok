from datetime import timedelta
import json

from moviepy.video.tools.subtitles import SubtitlesClip

from moviepy.editor import TextClip, CompositeVideoClip, VideoFileClip

def overlay_srt_on_video(path_to_video, path_to_srt, new_path):
    main_video = VideoFileClip(path_to_video)
    generator = lambda txt: TextClip(txt, font="arial", fontsize=50, color="white", method='caption', size=main_video.size)

    sub_clip = SubtitlesClip(path_to_srt, generator)

    result = CompositeVideoClip((main_video, sub_clip), size=main_video.size)
    result.write_videofile(new_path, fps=main_video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")


def format_video_verticle():
    pass

def add_attention_video():
    pass



