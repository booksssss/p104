import cv2

img = cv2.imread("imgs/solar-system.jpg")

cv2.putText(img,
"Sun",
(100,100),
cv2.FONT_HERSHEY_COMPLEX,
3, 
(0,0,255)
)
cv2.putText(img,
"Mercury",
(115,300),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255,255,255)
)
cv2.putText(img,
"Venus",
(195,300),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255,255,255)
)

cv2.putText(img,
"Earth",
(280,300),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255,255,255)
)

cv2.putText(img,
"Mars",
(380,300),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255,255,255)
)

cv2.putText(img,
"Jupiter",
(430,100),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255,255,255)
)

cv2.putText(img,
"Saturn",
(790,100),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255,255,255)
)


cv2.putText(img,
"Uranus",
(960,100),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255,255,255)
)


cv2.putText(img,
"Neptune",
(1090,100),
cv2.FONT_HERSHEY_COMPLEX,
0.5, 
(255,255,255)
)

cv2.imshow("output", img)
print(img)
cv2.waitKey(0)