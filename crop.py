import cv2
import os
from tqdm import tqdm


class Cropper:
    def __init__(self, coordinates: list[tuple[int, int]]):
        self.__coordinates = coordinates

    def __open_video(self, video_path: str) -> cv2.VideoCapture:
        video = cv2.VideoCapture(filename=video_path)

        if not video.isOpened():
            raise Exception("Error opening video file")

        return video

    def __create_folder(self, path: str = 'samples/sheeps/cropped') -> None:
        if not os.path.exists(path):
            os.makedirs(path)
            print('The out folder has been created')

    def get_proprieties(self, video_path: str) -> dict[str, int]:
        video = self.__open_video(video_path)

        frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(video.get(cv2.CAP_PROP_FPS))
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        return {
            'width': frame_width,
            'height': frame_height,
            'fps': fps,
            'frame_count': frame_count
        }

    def crop(self, input_path: str):
        video = self.__open_video(input_path)
        self.__create_folder()
        out_filename = f'{input_path.split("/")[-1]}'
        output_path = f'samples/sheeps/cropped/{out_filename}'

        properties = self.get_proprieties(input_path)
        fps = properties['fps']
        frame_count = properties['frame_count']

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # type: ignore
        width = self.__coordinates[1][0] - self.__coordinates[0][0]
        height = self.__coordinates[1][1] - self.__coordinates[0][1]
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        with tqdm(total=frame_count, desc="Processing frames") as pbar:
            while True:
                ret, frame = video.read()
                if not ret:
                    break

                x1, y1 = self.__coordinates[0]
                x2, y2 = self.__coordinates[1]
                cropped_frame = frame[y1:y2, x1:x2]

                out.write(cropped_frame)
                pbar.update(1)

        video.release()
        out.release()
        print(f"Cropped video saved to {output_path}")
        return output_path


if __name__ == '__main__':
    INPUT_PATH = 'samples/sheeps/mp4/2.mp4'
    COORDINATES = [
        (0, 1050),  # Top-left corner of the lower left screen
        (1680, 2100)  # Bottom-right corner of the lower left screen
    ]
    cropper = Cropper(coordinates=COORDINATES)
    cropper.crop(input_path=INPUT_PATH)
