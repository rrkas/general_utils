from sanitize_filename import sanitize
import pytube
import sys
import os


def download_video(url, file_name=None, filter_format="mp4", output_dir="outputs"):
    try:
        yt = pytube.YouTube(url)
        t = yt.streams.filter(file_extension=filter_format)
        t = t.order_by("resolution").desc().first()
        t.download(output_path=output_dir, filename=sanitize(file_name))

    except BaseException as e:
        print(e)


if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)
    args = sys.argv
    url = (
        args[1]
        if len(args) > 1
        else "https://www.youtube.com/watch?v=6altVgTOf9s&list=PLIP_AClgjRDifgmU_0q3D4G87P0RfGFQ_&index=1"
    )
    file_name = args[2] if len(args) > 2 else None
    download_video(url, file_name)
