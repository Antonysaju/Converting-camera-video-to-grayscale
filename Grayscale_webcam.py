import cv2 as cv

vid_capture=cv.VideoCapture(0)

while (True):
    ret,frame= vid_capture.read()
    grayFrame= cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    cv.imshow("Colour Video",frame)
    cv.imshow("Grayscale Video", grayFrame)
    
    if cv.waitKey(1) &0XFF == ord('x'):
        break

vid_capture.release()
cv.destroyAllWindows()
