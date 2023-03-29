import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,
            "Sun",
            (20, 300),
            cv2.FONT_HERSHEY_PLAIN,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Mercury",
            (50, 300),
            cv2.FONT_HERSHEY_PLAIN,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Venus",
            (80, 300),
            cv2.FONT_HERSHEY_PLAIN,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Earth",
            (110, 300),
            cv2.FONT_HERSHEY_PLAIN,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Mars",
            (140, 300),
            cv2.FONT_HERSHEY_PLAIN,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Jupiter",
            (170, 300),
            cv2.FONT_HERSHEY_PLAIN,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Saturn",
            (200, 300),
            cv2.FONT_HERSHEY_PLAIN,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Uranus",
            (230, 300),
            cv2.FONT_HERSHEY_PLAIN,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Neptune",
            (260, 300),
            cv2.FONT_HERSHEY_PLAIN,
            0.5,
            (255,255,255))
cv2.waitKey(0)   
cv2.imshow("Planets", img)