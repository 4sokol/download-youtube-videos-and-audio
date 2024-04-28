# import the YouTube and 'os' module class, which provides a portable way of interacting with the operating system. We'll use it to get the current working directory and manipulate file paths from the pytube library. 
from pytube import YouTube
import os

def download_music():
    # Ask for the YouTube Music URL
    music_url = input("Enter the YouTube Music URL: ")

    # Initialize a YouTube object with the music URL
    yt = YouTube(music_url)

    # Get the audio stream (audio only)
    stream = yt.streams.filter(only_audio=True).first()

    # Ask for the directory to save the music
    save_dir = input("Enter the directory to save the music (leave empty for current directory): ")
    if not save_dir:
        save_dir = os.getcwd()  # Use current directory if no directory is specified

    # Download the music to the specified directory
    stream.download(output_path=save_dir)

    print('Download completed!')

if __name__ == "__main__":
    download_music()
