import os
import cv2
video_path = r"C:\Users\Gaurav\OneDrive\文档\Desktop\DRS\videos\input\mai.mp4"
output_folder = "result/frames"

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_name = os.path.join(
        output_folder,
        f"frame_{frame_count:04d}.jpg"
    )

    cv2.imwrite(frame_name, frame)

    frame_count += 1

print(f"Total Frames Saved: {frame_count}")

cap.release()