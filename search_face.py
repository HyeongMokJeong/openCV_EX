import cv2, dlib

# scaler = 0.8

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if not ret: break

    # img = cv2.resize(img, (int(img.shape[1] * scaler), int(img.shape[0] * scaler)))
    ori = img.copy()

    # detect faces
    faces = detector(img)
    face = None
    if len(faces) != 0:
        face = faces[0]

    # visualize
    if face != None:
        img = cv2.rectangle(img, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()), color=(255, 255, 255), thickness=2)

    cv2.imshow('img', img)
    cv2.waitKey(1)