import cv2
import time
import os

def video_to_frames(input_loc, output_loc):
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print("Number of frames: ", video_length)
    count = 0
    frame_count = 0
    print("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        if not ret:
            continue
        count += 1
        # Save every 4th frame
        if count % 4 == 0:
            frame_count += 1
            # Write the results back to output location.
            cv2.imwrite(os.path.join(output_loc, f"{filename}{frame_count:05d}.jpg"), frame)
        # If there are no more frames left
        if count > video_length:
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print("Done extracting frames.\n%d frames extracted" % frame_count)
            print("It took %d seconds for conversion." % (time_end - time_start))
            break

if __name__ == "__main__":
    video_folder_path = '.\\data\\raw data\\videos'
    output_folder_path = '.\\data\\raw data\\temporary'
    for filename in os.listdir(video_folder_path):
        input_file_path = os.path.join(video_folder_path, filename)
        output_path = os.path.join(output_folder_path, filename)
        os.makedirs(output_path, exist_ok=True)
        video_to_frames(input_file_path, output_path)
