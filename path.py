import cv2

def process_video_frame(video_path):
    """
    Process each frame of a video and save the processed frame as a new image.

    Args:
    video_path (str): Path to the video file.
    """
    cap = cv2.VideoCapture(video_path)
