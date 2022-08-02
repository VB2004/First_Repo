import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("Images/region.png")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

titles = ['Image', 'RGB', 'HSV', 'LAB', 'Gray']
images = [img, rgb, hsv, lab, gray]

img.shape
print("Height :", img.shape[0])
print("Width :", img.shape[1])
print("Size :", img.size)

fig = plt.figure(figsize=(6,6))
for i in range(5):
    fig.add_subplot(2,3,i+1)
    plt.title(titles[i])
    plt.imshow(images[i])
plt.show()


#cv2.imshow("Image",img)
#cv2.imshow("RGB",rgb)
#cv2.imshow("HSV",hsv)
#cv2.imshow("Lab",lab)
#cv2.imshow("Gray",gray)

cv2.waitKey(0)   
cv2.destroyAllWindows()
