from threading import Thread
import pytube
import sys
import os
from sanitize_filename import sanitize
from tqdm import tqdm


def download_playlist(url, filter_format="mp4", output_dir="outputs", thread_limit=4):
    try:
        pl = pytube.Playlist(url)
        dir_path = os.path.join(output_dir, sanitize(pl.title))
        print(dir_path)
        os.makedirs(dir_path, exist_ok=True)
        pad = len(str(pl.length))

        def _download(idx, video):
            try:
                t = video.streams.filter(file_extension=filter_format)
                t = t.order_by("resolution").desc().first()
                t.download(
                    output_path=dir_path,
                    filename=sanitize(
                        f"{str(idx+1).zfill(pad)}_{video.title}.{filter_format}"
                    ),
                )
            except BaseException as e:
                print(idx, e.args)

        threads = []
        for idx, video in enumerate(tqdm(pl.videos)):
            try:
                thread = Thread(target=_download, args=(idx, video))
                thread.start()
                threads.append(thread)

                while sum([t.is_alive() for t in threads]) >= thread_limit:
                    pass

            except BaseException as e:
                print(e)

        while any([t.is_alive() for t in threads]):
            pass

        return dir_path

    except BaseException as e:
        print(e)


if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)
    args = sys.argv
    url = (
        args[1]
        if len(args) > 1
        else "https://www.youtube.com/playlist?list=PLIP_AClgjRDifgmU_0q3D4G87P0RfGFQ_"
    )
    output_dir = args[2] if len(args) > 2 else "outputs"
    download_playlist(url, output_dir=output_dir)
