import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    dimensions = (width, heigth)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('opencv/photos/cat.jpg')

img_resized = rescaleFrame(img, scale=0.4)

cv.imshow('Cat', img_resized)

cv.waitKey(0)
