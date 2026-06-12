import cv2

image = cv2.imread("result/frames/frame_0030.jpg")

points = [
    (306, 167),
    (309, 179),
    (311, 190),
    (315, 206),
    (320, 211),
    (322, 197)
]

for point in points:
    cv2.circle(image, point, 8, (0, 0, 255), -1)

for i in range(len(points) - 1):
    cv2.line(image, points[i], points[i + 1], (255, 0, 0), 3)

cv2.imshow("Ball Trajectory", image)
cv2.waitKey(0)
cv2.destroyAllWindows()