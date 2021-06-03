import cv2


cap=cv2.VideoCapture(0)
cap.set(3,640) # width
cap.set(4,480) # height
cap.set(10,100) #brigthness
print(cap.isOpened())
while(cap.isOpened()):
    x,y=cap.read()
    g=cv2.cvtColor(y,cv2.COLOR_BGR2GRAY)
    cv2.imshow("try",g)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()