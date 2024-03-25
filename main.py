from __future__ import print_function
import cv2 as cv
import numpy as np
alpha = 0.5
raw_input = input # Python 3
print(''' Simple Linear Blender
-----------------------
* Enter alpha [0.0-1.0]: ''')
input_alpha = float(raw_input().strip())
if 0 <= alpha <= 1:
 alpha = input_alpha
# [load]
src1 = cv.imread(cv.samples.findFile('cat.jpg'))
src2 = cv.imread(cv.samples.findFile('monkey.jpg'))
# [load]
if src1 is None:
 print("Error loading src1")
 exit(-1)
elif src2 is None:
 print("Error loading src2")
 exit(-1)
# [blend_images]
image1 = cv.resize(src1, (350, 300))
image2 = cv.resize(src2, (350, 300))
# Create frames (black backgrounds) for each image
frame1 = np.zeros((300, 400, 3), dtype=np.uint8)
frame2 = np.zeros((300, 400, 3), dtype=np.uint8)
# Place the images within the frames
frame1[0:300, 0:350] = image1
frame2[0:300, 50:400] = image2

beta = (1.0 - alpha)
# dst = cv.addWeighted(src1, alpha, src2, beta, 0.0)
dst = np.uint8(alpha*(frame1)+beta*(frame2))
# [blend_images]
# [display]
cv.imshow('dst', dst)
cv.waitKey(0)
# [display]
cv.destroyAllWindows()