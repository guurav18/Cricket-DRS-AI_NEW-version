import cv2
import os
import csv

frames_folder = "result/frames"

ball_points = []

for frame_num in range(20, 41):

    frame_name = f"frame_{frame_num:04d}.jpg"
    frame_path = os.path.join(frames_folder, frame_name)

    image = cv2.imread(frame_path)

    if image is None:
        continue

    crop = image[100:250, 200:450]

    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    best_ball = None

    for contour in contours:

        area = cv2.contourArea(contour)

        if 2 < area < 20:

            x, y, w, h = cv2.boundingRect(contour)

            ratio = w / h

            if 0.5 < ratio < 1.5:

                center_x = x + w // 2
                center_y = y + h // 2

                if 60 < center_x < 180 and center_y > 50:
                    best_ball = (center_x, center_y)

    if best_ball:
        ball_points.append(
            [frame_num, best_ball[0], best_ball[1]]
        )

with open(
    "result/ball_coordinates.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(["Frame", "X", "Y"])

    writer.writerows(ball_points)

print("CSV File Saved Successfully!")