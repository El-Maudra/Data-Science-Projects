import os
from pytube import YouTube

def download_youtube_video(video_url):
    def progress_callback(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        downloaded_size = total_size - bytes_remaining
        percentage = (downloaded_size / total_size) * 100
        print(f"Download progress: {percentage:.2f}%")

    try:
        # Define the path for saving the video
        save_path = os.path.join(os.path.expanduser("~"), 'Downloads')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        yt = YouTube(video_url, on_progress_callback=progress_callback)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(save_path)
        print(f"Downloaded '{yt.title}' successfully to {save_path}!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)
