import cv2
import numpy as np
def draw_centerness(box):
    x1, y1, x2, y2 = box
    w, h = x2 - x1, y2 - y1
    xs = np.arange(w).repeat(h).reshape(h, w).transpose(1, 0).reshape(-1, 1)
    ys = np.arange(h).repeat(w).reshape(h, w).reshape(-1, 1)
    left = xs - x1
    right = x2 - xs
    top = ys - y1
    bottom = y2 -ys
    hm = np.sqrt(np.minimum(left, right)/np.maximum(left, right) * np.minimum(top, bottom)/np.maximum(top, bottom))
    hm = hm.reshape(h, w)
    return hm
hm =draw_centerness([0, 0, 512, 512])
cv2.imshow('hm', hm)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("D:/documents/2023spring/nndl/centerness.png", hm*255)