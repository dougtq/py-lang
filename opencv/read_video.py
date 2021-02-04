import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    dimensions = (width, heigth)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, heigth):
    # only works for live videos
    capture.set(3, width)
    capture.set(4, heigth)

capture = cv.VideoCapture('opencv/videos/cat.mp4')

while True:
    isTrue, frame = capture.read()
    if frame:
        frame_resized = rescaleFrame(frame)
        cv.imshow('Vid', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()
