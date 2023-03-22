import cv2

img = cv2.imread("solar-system.jpg")

# add text below each planet
cv2.putText(img, "Mercury", (55, 220), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
cv2.putText(img, "Venus", (160, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
cv2.putText(img, "Earth", (280, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
cv2.putText(img, "Mars", (400, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
cv2.putText(img, "Jupiter", (565, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
cv2.putText(img, "Saturn", (715, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
cv2.putText(img, "Uranus", (950, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
cv2.putText(img, "Neptune", (1070, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))


cv2.imshow("output", img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", img)
