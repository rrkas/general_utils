import os
import sys
from .video_length import get_video_length

# float: seconds
def get_video_dir_length(dir_path):
    total_length = 0

    metadata = open(os.path.join(dir_path, "metadata.txt"), "w")
    for root, _, files in os.walk(dir_path):
        for file in sorted(files):
            try:
                path = os.path.join(root, file)
                length = get_video_length(path)
                total_length += length
                metadata.write(f"{path} = {length}\n")
            except:
                pass

    metadata.write(f"------------------------------\n")
    metadata.write(f"Total = {total_length:.2f} secs")

    if total_length >= 60:
        total_min = total_length / 60
        metadata.write(f" = {total_min:.2f} minutes")

    if total_length >= 3600:
        total_hr = total_length / 3600
        metadata.write(f" = {total_hr:.2f} hours")

    metadata.close()
    return total_length


if __name__ == "__main__":
    path = sys.argv[1]
    length = get_video_dir_length(path)
    print(path, ":", length)
