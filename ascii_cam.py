import cv2
import numpy as np
import sys

# ASCII characters to represent pixel intensity
# ASCII_CHARS = "@%#*+=-:. "
ASCII_CHARS = "@#$&WM%QO0X*o+=-:. |/\()[]ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


# Function to convert frame to ASCII
def frame_to_ascii(frame, width=80, height=40):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (width, height))
    ascii_frame = "".join(ASCII_CHARS[pixel // 32] for pixel in resized.flatten())
    ascii_image = "\n".join(
        ascii_frame[i * width:(i + 1) * width] for i in range(height)
    )
    return ascii_image

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    sys.exit()

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        ascii_art = frame_to_ascii(frame, width=500, height=200)
        
        # Clear screen and print ASCII frame
        sys.stdout.write("\033[H\033[J")  # ANSI escape codes to clear terminal
        print(ascii_art)
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    cap.release()
    cv2.destroyAllWindows()