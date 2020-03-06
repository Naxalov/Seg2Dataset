import cv2
import os
import matplotlib.pyplot as plt
# input image in order calibration
INPUT_DIR = 'data/seg'
PATH = os.path.join(os.getcwd(), INPUT_DIR)

images = os.listdir(PATH)
img = cv2.imread(os.path.join(PATH, images[0]))
# get shape of image
W, H, _ = img.shape

plt.imshow(img)
plt.show()
