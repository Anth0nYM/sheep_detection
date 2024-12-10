import os
from moviepy.video.io.VideoFileClip import VideoFileClip

INPUT_DIR = 'samples/sheeps/mov'
OUTPUT_DIR = 'samples/sheeps/mp4'
os.makedirs(OUTPUT_DIR, exist_ok=True)


def convert_to_mp4(video_path, output_path):
    try:
        clip = VideoFileClip(video_path)
        clip.write_videofile(
            output_path,
            codec="h264_nvenc",
            ffmpeg_params=["-preset", "fast", "-crf", "23"]
        )
        clip.close()
        print("Success")
        return output_path
    except Exception as e:
        print(f"There's an error converting your video: {e}")
        return None


if __name__ == '__main__':

    for filename in os.listdir(INPUT_DIR):
        if filename.endswith('.mov'):
            input_path = os.path.join(INPUT_DIR, filename)
            output_filename = f"{os.path.splitext(filename)[0]}.mp4"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            print(f"Converting: {input_path} -> {output_path}")
            convert_to_mp4(input_path, output_path)

    print("Finished!")
