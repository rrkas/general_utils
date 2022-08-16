import os
import sys
from video_length import get_video_length

# float: seconds
def get_video_dir_length(dir_path):
    total_length = 0

    for root, _, files in os.walk(dir_path):
        for file in sorted(files):
            try:
                path = os.path.join(root, file)
                print(path)
                total_length += get_video_length(path)
            except:
                pass

    return total_length

if __name__ == "__main__":
    path = sys.argv[1]
    length = get_video_dir_length(path)
    print(path, ":", length)