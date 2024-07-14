import cv2 as cv 

img = cv.imread("varun.jpg",0)
cv.imshow("X",img)
cv.waitKey(0)
cv.destroyAllWindows()
