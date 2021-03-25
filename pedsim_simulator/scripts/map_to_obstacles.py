import cv2
import matplotlib.pyplot as plt

image = cv2.imread("playpen.pgm")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
element = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
#binary = cv2.dilate(binary, element)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find minimum value to normalize with
min_val = 1000000000
max_val = 0
for i in range(len(contours)):
    for j in range(len(contours[i])):
        if contours[i][j][0][0] < min_val:
            min_val = contours[i][j][0][0]

        #if contours[i][j][0][1] < min_val:
        #    min_val = contours[i][j][0][1]

        if contours[i][j][0][0] > max_val:
            max_val = contours[i][j][0][0]

        #if contours[i][j][0][1] > max_val:
        #    max_val = contours[i][j][0][1]

diff = (max_val - min_val) / 20
print(len(contours))
for i in range(len(contours)):
    for j in range(len(contours[i]) - 1):
        x1 = contours[i][j][0][0] / diff
        y1 = contours[i][j][0][1] / diff
        x2 = contours[i][j+1][0][0] / diff
        y2 = contours[i][j+1][0][1] / diff
        print('<obstacle x1="' + str(x1) + '" y1="' + str(y1) + '" x2="' + str(x2) + '" y2="' + str(y2) + '"/>')
image = cv2.drawContours(image, contours, -1, (0,255,0), 2)
plt.imshow(image)
plt.show()
