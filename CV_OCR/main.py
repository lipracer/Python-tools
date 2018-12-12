import cv2
import threading


class my_thread(threading.Thread):
    def __init__(self, func, *params):
        self.__func = func
        self.__params = params
        super(my_thread, self).__init__()
    def run(self):
        self.__func(*self.__params)


def img_show(title, image):
    cv2.namedWindow(title)
    th = my_thread(cv2.imshow, title, image)
    th.run()



filepath = "./target.png"
im = cv2.imread(filepath)

#彩色转灰度
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

#大津阈值

cv2.threshold(im_gray, 0, 255, cv2.THRESH_OTSU, im_gray)



# img_show("target", im_gray)
cv2.namedWindow("title")
cv2.imshow("title", im_gray)
cv2.waitKey(0)