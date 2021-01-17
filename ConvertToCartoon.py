import cv2
from Tkinter import getImageLocation
import sys

def main():
    image=getImageLocation()
    photoname=image.split('\\' if sys.platform.startswith('win') else '/')[-1]
    img=cv2.imread(image)
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray=cv2.medianBlur(gray, 5)
    edges=cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,9)
    color=cv2.bilateralFilter(img, 9, 250, 250)
    cartoon=cv2.bitwise_and(color, color, mask=edges)
    cv2.imwrite(f"Cartoonized_{photoname}", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()