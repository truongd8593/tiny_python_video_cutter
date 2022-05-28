import os

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from conf import ROOT_DIR
from src.argument_parser import argument_parser


if __name__ == "__main__":
    args = argument_parser()
    ffmpeg_extract_subclip(
        filename=os.path.join(ROOT_DIR, args.file_name),
        t1=args.start_time * 60,
        t2=args.end_time * 60,
        targetname=args.target_name
    )