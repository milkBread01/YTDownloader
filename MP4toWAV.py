import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_wav(input_directory, output_directory):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith(".mp4"):
            mp4_path = os.path.join(input_directory, filename)
            wav_filename = os.path.splitext(filename)[0] + '.wav'
            wav_path = os.path.join(output_directory, wav_filename)

            # Check if WAV file already exists in the output directory
            if os.path.exists(wav_path):
                print(f"The file {wav_filename} has been skipped. The WAV file already exists in this directory.")
            else:
                # Convert MP4 to WAV
                video_clip = VideoFileClip(mp4_path)
                video_clip.audio.write_audiofile(wav_path, codec='pcm_s16le', bitrate='600k')
                #video_clip.audio.write_audiofile(wav_path, codec='pcm_s16le', bitrate='600k', fps=44100, bits_per_sample=16, channels=2)

                print(f"Conversion of {filename} to {wav_filename} is complete.")

input_directory = input("Enter Path to MP4 Files: ")
#input_directory = "/home/ancelotti/Documents/School"

output_directory = input("Enter Path to WAV Desitination: ")
#output_directory ="/home/ancelotti/Documents/School"
convert_mp4_to_wav(input_directory, output_directory)
