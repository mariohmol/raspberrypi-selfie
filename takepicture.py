from SimpleCV import Image, Camera

cam = Camera()
img = cam.getImage()
img.save("filename.jpg")

## USING CV
#import cv2
#vidcap = cv2.VideoCapture()
#vidcap.open(0)
#retval, image = vidcap.retrieve()
#vidcap.release()
#Cleaned up camera.
#cv2.imwrite("test.png", image)