import cv2

INPUT = "samples/sheeps/cropped/sheeps.mp4"
MIN_CONTOUR_AREA = 1500
SHADOW_TRESH = 250


def vid_inf(vid_path):
    cap = cv2.VideoCapture(vid_path)

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS)) or 30  # Default FPS if not detected
    frame_size = (frame_width, frame_height)
    output_video = f"outputs/output_{vid_path.split('/')[-1]}"
    print(f"frame_width: {frame_width}, "
          f"frame_height: {frame_height}, "
          f"fps: {fps}")

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec for MP4 format
    out = cv2.VideoWriter(output_video, fourcc, fps, frame_size)

    backSub = cv2.createBackgroundSubtractorMOG2()

    if not cap.isOpened():
        print("Error opening video file")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("End of video file or error reading frame.")
            break

        fg_mask = backSub.apply(frame)

        _, mask_thresh = cv2.threshold(
            fg_mask, SHADOW_TRESH, 255, cv2.THRESH_BINARY)
        # cv2.imshow('frame_thresh', mask_thresh)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        mask_eroded = cv2.morphologyEx(mask_thresh, cv2.MORPH_OPEN, kernel)

        contours, _ = cv2.findContours(
            mask_eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        large_contours = [
            cnt for cnt in contours if cv2.contourArea(cnt) > MIN_CONTOUR_AREA
        ]
        frame_out = frame.copy()
        for cnt in large_contours:
            x, y, w, h = cv2.boundingRect(cnt)
            frame_out = cv2.rectangle(
                frame_out, (x, y), (x + w, y + h), (0, 0, 200), 3
            )

        out.write(frame_out)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Resources released successfully.")


if __name__ == "__main__":
    vid_inf(INPUT)
