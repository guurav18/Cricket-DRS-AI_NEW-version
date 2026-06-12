import cv2

# Frame load
image = cv2.imread("result/frames/frame_0030.jpg")

# Crop same as tracking
crop = image[100:250, 200:450]

# Ball points from tracking
points = [
    (102, 58),
    (106, 67),
    (112, 92),
    (114, 78),
    (121, 97),
    (124, 82),
    (142, 78),
    (178, 85)
]

# Draw points
for point in points:
    cv2.circle(crop, point, 5, (0, 0, 255), -1)

# Draw trajectory
for i in range(len(points) - 1):
    cv2.line(
        crop,
        points[i],
        points[i + 1],
        (255, 0, 0),
        2
    )

cv2.imshow("Automatic Trajectory", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()