import cv2
import numpy as np
import threading
import sys


class my_thread(threading.Thread):
    def __init__(self, func, *params):
        self.__func = func
        self.__params = params
        super(my_thread, self).__init__()
    def run(self):
        cv2.namedWindow(self.__params[0])
        self.__func(*self.__params)
        cv2.waitKey(0)


def img_show(title, image):
    th = my_thread(cv2.imshow, title, image)
    th.run()

def _img_show(image, title=[]):
    cv2.namedWindow(str(title))
    cv2.imshow(str(title), im_gray)
    print("title:", title)
    title.append('x')

filepath = "./target.png"
im = cv2.imread(filepath)

#彩色转灰度
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

#大津阈值
cv2.threshold(im_gray, 0, 255, cv2.THRESH_OTSU, im_gray)
_img_show(im_gray)

#图像腐蚀 然后分割? 分割采用分水岭算法？
# kernel = np.ones((5,5), np.uint8)


kernel = np.ones((3,3), np.uint8)
cv2.dilate(im_gray, kernel, im_gray)

cv2.erode(im_gray, kernel, im_gray)

# img_show("target", im_gray)
_img_show(im_gray)
cv2.waitKey(0)

