import cv2

# Frame load
image = cv2.imread("result/frames/frame_0030.jpg")

# Pitch crop
crop = image[100:250, 200:450]

# Ball points
points = [
    (102,58),
    (106,67),
    (112,92),
    (121,97)
]

# Draw trajectory
for point in points:
    cv2.circle(crop, point, 5, (0,0,255), -1)

for i in range(len(points)-1):
    cv2.line(
        crop,
        points[i],
        points[i+1],
        (255,0,0),
        2
    )

# Virtual stumps
stump_x = 170

cv2.line(crop, (stump_x,40), (stump_x,120), (0,255,0), 3)
cv2.line(crop, (stump_x+8,40), (stump_x+8,120), (0,255,0), 3)
cv2.line(crop, (stump_x+16,40), (stump_x+16,120), (0,255,0), 3)

# Decision
decision = "NOT OUT"

cv2.putText(
    crop,
    decision,
    (10,25),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0,255,255),
    2
)

cv2.imshow("DRS Visualization", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()