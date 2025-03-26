import cv2
import os

# Start video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # Set video width
cam.set(4, 480)  # Set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Enter user ID
face_id = input('\nEnter user ID and press <return>: ')

print("\n[INFO] Capturing face images. Look at the camera...")

count = 0
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1

        # Save image to dataset
        cv2.imwrite(f"dataset/User.{face_id}.{count}.jpg", gray[y:y+h, x:x+w])
        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xFF
    if k == 27 or count >= 30:  # Capture 30 images
        break

print("\n[INFO] Face images captured. Exiting...")
cam.release()
cv2.destroyAllWindows()
