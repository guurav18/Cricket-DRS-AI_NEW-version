import numpy as np
import matplotlib.pyplot as plt

# Ball coordinates from tracking
x = np.array([102, 106, 112, 121])
y = np.array([58, 67, 92, 97])

# Curve fitting
coeff = np.polyfit(x, y, 2)
curve = np.poly1d(coeff)

# Future trajectory
x_future = np.linspace(min(x), 180, 200)
y_future = curve(x_future)

# Virtual stump position
stump_x = 170
stump_y_top = 40
stump_y_bottom = 120

# Predicted ball height at stump
ball_y_at_stump = curve(stump_x)

print("Predicted Ball Y at Stump:", ball_y_at_stump)

if stump_y_top <= ball_y_at_stump <= stump_y_bottom:
    decision = "OUT"
else:
    decision = "NOT OUT"

print(decision)

with open("result/drs_result.txt", "w") as file:
    file.write(decision)

# Plot
plt.scatter(x, y, label="Ball Points")

plt.plot(
    x_future,
    y_future,
    label="Predicted Trajectory"
)

plt.axvline(
    x=stump_x,
    linestyle="--",
    label="Stumps"
)

plt.legend()
plt.savefig("result/trajectory_prediction.png")
plt.show()
