import cv2

# Read Image
img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(100,80),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Mercury",(120,80),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Venus",(140,80),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Earth",(160,80),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Mars",(200,80),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Jupiter",(240,80),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Saturn",(280,80),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Uranus",(320,80),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Neptune",(360,80),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
# Display Colored Image
print(img)
cv2.imshow("output",img)


cv2.waitKey(0)
cv2.imwrite("solorSystemWithName.jpg ")