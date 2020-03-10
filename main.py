import cv2
import os
import matplotlib.pyplot as plt
import numpy as np


def show_image(img):
    plt.imshow(img)
    plt.show()


def show_class(idx):
    celing = (img[:, :] == [idx, idx, idx]) * 1.0
    plt.imshow(celing)
    plt.show()


# input image in order calibration
INPUT_DIR = 'data/seg'
PATH = os.path.join(os.getcwd(), INPUT_DIR)

images = os.listdir(PATH)
img = cv2.imread(os.path.join(PATH, images[0]))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
mi, ma = np.min(img), np.max(img)
n_classes = ma - mi + 1
print('Class:{}'.format(n_classes))

# get shape of image
W, H, _ = img.shape
show_class(0)
show_class(1)
show_class(2)
show_class(3)
show_class(4)
show_class(5)
# celing = (img[:,:]==[187, 188,67])*1.0
# show_image(celing)
# celing [187, 188,67]
plt.imshow(img)
plt.show()

# mi, ma = np.min(img), np.max(img)
# n_classes = ma - mi + 1
