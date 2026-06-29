import cv2
import matplotlib.pyplot as plt

image = cv2.imread("//Users//sreedeviviswambaran//Documents//Python//Classwork//zImage Manipulation//Screenshot 2025-08-25 at 7.47.48 PM.png")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB Image")
plt.show()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap = "gray")
plt.title("Grayscale Image")
plt.show()

cropped_image = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()