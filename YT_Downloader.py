import os
from pytube import YouTube, Playlist
from moviepy.editor import VideoFileClip

def create_output_folders():
    # Create the 'YTDownloads' folder in the current directory if it doesn't exist
    if not os.path.exists('YTDownloads'):
        os.mkdir('YTDownloads')

    # Create the 'MP4 Files' folder within 'YTDowloads' if it doesn't exist
    mp4_folder = os.path.join('YTDownloads', 'MP4 Files')
    if not os.path.exists(mp4_folder):
        os.mkdir(mp4_folder)

    # Create the 'WAV Files' folder within 'YTDowloads' if it doesn't exist
    wav_folder = os.path.join('YTDownloads', 'WAV Files')
    if not os.path.exists(wav_folder):
        os.mkdir(wav_folder)

def video_exists(video_title):
    start_path = '.'
    # Check file subdirectories 
    for root, dirs, files in os.walk(start_path):
        for filename in files:
            if video_title in filename:
                return True

    return False

def save_wav(mp4_output_path, video):
    # Convert the video to .wav format
    video_filename = os.path.join(mp4_output_path, video.title + ".mp4")
    video_clip = VideoFileClip(video_filename)
    
    # Generate WAV filename using video title
    wav_filename = os.path.join('YTDownloads', 'WAV Files', f"{video.title}.wav")
    
    # Write audio to WAV file
    video_clip.audio.write_audiofile(wav_filename)
    return wav_filename


def download_youtube_content(url, output_folder="."):
    try:
        create_output_folders()

        if url == '1':
            # The user provided a URL for a single video
            yt = YouTube(input("Enter the URL of the YouTube video: "))
            video_title = yt.title
            mp4_output_path = os.path.join('YTDownloads', 'MP4 Files')
            
            if (video_exists(video_title)):
                print("Video already exists in the 'MP4 Files' directory or its subdirectories. There is no need to download.")
                return
            else:
                # Defining video
                video = yt.streams.get_highest_resolution()
            
                # saving mp4 file
                video.download(output_path=mp4_output_path)
            
                wav_filename = save_wav(mp4_output_path,video)

            print(f"Video downloaded and saved as {os.path.basename(wav_filename)} in the 'WAV Files' folder.")
        elif url == '2':
            # The user provided a URL for a playlist
            playlist_url = input("Enter the URL of the YouTube playlist: ")
            playlist = Playlist(playlist_url)

            mp4_output_path = os.path.join('YTDownloads', 'MP4 Files')

            for video in playlist.videos:
                video_title = video.title

                if video_exists(video_title):
                    print(f"Video '{video_title}' already exists in the 'MP4 Files' directory or its subdirectories. Skipping download.")
                else:
                    video.streams.get_highest_resolution().download(output_path=mp4_output_path)
                    wav_filename = save_wav(mp4_output_path,video)

            print(f"All videos in the playlist have been downloaded to the 'MP4 Files' folder and converted to 'WAV Files'.")
        else:
            print("Invalid input. Please enter '1' for a single video or '2' for a playlist.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    user_choice = input("Is the URL to a single YouTube video or a playlist? Press 1 for a single video, press 2 for a playlist: ")
    download_youtube_content(user_choice)