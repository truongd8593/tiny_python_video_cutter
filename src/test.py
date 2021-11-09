from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

start_time = 0
end_time = 10
ffmpeg_extract_subclip("387.mp4", start_time, end_time, targetname="test.mp4")
