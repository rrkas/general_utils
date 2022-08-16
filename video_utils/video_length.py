import subprocess
import sys

# float: seconds
def get_video_length(filepath):
    try:
        res = subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=noprint_wrappers=1:nokey=1",
                f"{filepath}",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        return float(res.stdout)
    except:
        return None


if __name__ == "__main__":
    path = sys.argv[1]
    length = get_video_length(path)
    print(path, ":", length)
