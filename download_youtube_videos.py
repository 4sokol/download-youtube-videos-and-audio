from pytube import YouTube
import os

def download_video():
    # Ask for the Youtube video URL
    video_url = input("Enter the Youtube video URL: ")

    # Initialize a Youtube object with the video URL
    yt = YouTube(video_url)

    # Get the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    # Ask for the directory to save the video
    save_dir = input("Enter the directory to save the video (leave empty for current directory): ")
    if not save_dir:
        save_dir = os.getcwd()  # Use current directory if no directory is specified

    # Download the video to the specified directory
    stream.download(output_path=save_dir)

    print('Download completed!')

if __name__ == "__main__":
    download_video()
