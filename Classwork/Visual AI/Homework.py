import cv2 

image = cv2.imread("//Users//sreedeviviswambaran//Documents//Python//Classwork//Visual AI//dog.png")

cv2.namedWindow("Loaded Image", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Loaded Image", 1000, 800)

cv2.imshow("Loaded Image", image)

cv2.waitKey(0)

cv2.destroyAllWindows()


image2 = cv2.imread("//Users//sreedeviviswambaran//Documents//Python//Classwork//Visual AI//Screenshot 2025-08-25 at 7.47.48 PM.png")

cv2.namedWindow("Loaded Image2", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Loaded Image2", 600, 400)

cv2.imshow("Loaded Image2", image)

cv2.waitKey(0)

cv2.destroyAllWindows()

image3 = cv2.imread("//Users//sreedeviviswambaran//Documents//Python//Classwork//Visual AI//Screenshot 2025-08-25 at 7.47.48 PM.png")

cv2.namedWindow("Loaded Image3", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Loaded Image3", 300, 200)

cv2.imshow("Loaded Image3", image)

cv2.waitKey(0)

cv2.destroyAllWindows()

print(f"Image Dimensions: {image.shape}")