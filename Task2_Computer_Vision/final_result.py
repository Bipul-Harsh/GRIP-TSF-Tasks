#!/usr/bin/python3
import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser(description="Can check pixel value of any point in given photo.")
parser.add_argument('--input_file', type=str, help="(Required) the image file you want to read")
parser.add_argument('--wt_ratio', type=float, default=1, help="width ratio to resize frame horizontally")
parser.add_argument("--ht_ratio", type=float, default=1, help="height ratio to resize frame veritcally")
parser.add_argument("--wt_size", type=int, default=0, help="to provide the frame width size in pixels")
parser.add_argument("--ht_size", type=int, default=0, help="to provide the frame height size in pixels")
parser.add_argument("--pallete_size", type=int, default=40, help="to provide height for the pallete window showing pixel value")

args = parser.parse_args()

INPUT_FILE = args.input_file
assert INPUT_FILE != None, "Please provide a image file"
WT_RATIO = args.wt_ratio
HT_RATIO = args.ht_ratio
WT_SIZE = args.wt_size
HT_SIZE = args.ht_size
HEIGHT = args.pallete_size

image = cv2.imread(INPUT_FILE)
assert type(image) != type(None), "Please provide valid image location"
image = cv2.resize(image, (WT_SIZE,HT_SIZE), fx=WT_RATIO, fy=HT_RATIO)

display_portion = np.zeros((HEIGHT, image.shape[1], 3),dtype=np.uint8)
updated_image = np.vstack((image, display_portion))
temp = image.copy()
# Default Text
cv2.putText(updated_image, text="Hover Over Image To See Pixel Value | Double Click to Print on Console", org=(10, image.shape[0]+HEIGHT-10), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.6, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)

def display_pixel_value(event, x, y, flags, params):
    '''
    Display the updated pixel vlaue in bottom area
    Arguments:
        All arguments are as per instruction for setMouseCallback function in OpenCV documentation
    '''
    global image
    global updated_image
    image = temp.copy()
    updated_image = np.vstack((image, np.array([image[y, x]]).repeat(HEIGHT*image.shape[1], axis=0).reshape(HEIGHT, image.shape[1], 3) ))
    color = (255, 255, 255) if image[y,x,2]<105 else (0,0,0)
    cv2.putText(updated_image, text=f"RGB: ({image[y,x][2]},{image[y,x][1]},{image[y,x][0]})", org=(10, image.shape[0]+HEIGHT-10), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.6, color=color, thickness=1, lineType=cv2.LINE_AA)
    if event == cv2.EVENT_MBUTTONDBLCLK:
        print(f'Your selected pixel : {image[y,x]}')

cv2.namedWindow("Color Picker")
cv2.setMouseCallback("Color Picker", display_pixel_value)

while(True):
    cv2.imshow("Color Picker", updated_image)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
