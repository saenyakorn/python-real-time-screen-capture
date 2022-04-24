import numpy as np
import cv2
from time import time
from PIL import ImageGrab

def main():
  print("Starting...")

  while 1:
    begin_time = time()
    screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)

    # Show screenshot
    cv2.imshow('Screen Capture', np.array(screenshot))

    # Debug using FPS
    print(f'FPS {1/(time()-begin_time):.4f}, Size {screenshot.shape}')

    # Wait key event for 25 ms
    # Press q to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

if __name__ == "__main__":
  main()
