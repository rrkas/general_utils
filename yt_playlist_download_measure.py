import os
from youtube.download_playlist import download_playlist
from video_utils.video_dir_length import get_video_dir_length
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        print("youtube playlist url expected!")
    url = args[0]
    output_dir = "outputs"
    if len(args) > 1:
        output_dir = args[1]

    try:
        os.makedirs(output_dir, exist_ok=True)
        dir_path = download_playlist(url, output_dir=output_dir)
        print(dir_path)
        secs = get_video_dir_length(dir_path)
        print(secs)
    except BaseException as e:
        print(e.args)
