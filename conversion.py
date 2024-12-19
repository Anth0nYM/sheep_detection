import os
from moviepy.video.io.VideoFileClip import VideoFileClip


class Converter:
    def __init__(self) -> None:
        pass

    def mov_to_mp4(self, mov_path: str, mp4_path: str) -> bool:
        try:
            clip = VideoFileClip(mov_path)
            clip.write_videofile(
                mov_path,
                codec="h264_nvenc",
                ffmpeg_params=["-preset", "fast", "-crf", "23"]
            )
            clip.close()
            print("Success")
            return True
        except Exception as e:
            print(f"There's an error converting your video: {e}")
            return False


if __name__ == '__main__':
    INPUT_DIR = 'samples/sheeps/mov'
    OUTPUT_DIR = 'samples/sheeps/mp4'
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    converter = Converter()

    for filename in os.listdir(INPUT_DIR):
        if filename.endswith('.mov'):
            input_path = os.path.join(INPUT_DIR, filename)
            output_filename = f"{os.path.splitext(filename)[0]}.mp4"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            print(f"Converting: {input_path} -> {output_path}")
            converter.mov_to_mp4(input_path, output_path)

    print("Finished!")
