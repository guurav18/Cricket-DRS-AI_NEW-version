import cv2

# Load image
image = cv2.imread("result/frames/frame_0026.jpg")

# Crop pitch area
crop = image[100:250, 200:450]

# Convert to grayscale
gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

# Threshold
_, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

best_ball = None

for contour in contours:

    area = cv2.contourArea(contour)

    # Small objects only
    if 2 < area < 20:

        x, y, w, h = cv2.boundingRect(contour)

        ratio = w / h

        # Ball should be roughly square
        if 0.5 < ratio < 1.5:

            center_x = x + w // 2
            center_y = y + h // 2

            # Ignore objects outside pitch center region
            if 60 < center_x < 180 and center_y > 50:

                best_ball = (center_x, center_y)

            print(
    f"Candidate -> X:{center_x} Y:{center_y} Area:{area}"
)
                

# Draw detected ball
if best_ball:

    cv2.circle(
        crop,
        best_ball,
        8,
        (0, 0, 255),
        -1
    )

    cv2.putText(
        crop,
        "BALL",
        (best_ball[0] + 10, best_ball[1]),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

    print("Final Ball Detected:", best_ball)

else:
    print("No Ball Detected")

# Show result
cv2.imshow("Ball Detection", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()