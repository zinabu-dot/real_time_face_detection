import cv2

def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(grey_img, scaleFactor, minNeighbors)
    coords = []
    for (x,y, w, h) in features:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
        cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords = [x, y, w, h]

    return coords, img

def detect(img, faceCascade):
    color = {'blue':(255, 0,0), 'red':(0,0,255), 'green':(0,255,0)}
    coords, img = draw_boundary(img, faceCascade, 1.1, 10, color['blue'], "Face")

    return img

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

live_video = cv2.VideoCapture(0) # 0 for the build-in webcam (the laptop camera, default camera), -1 for external camera (example phone's camera)

while True:
    _, img = live_video.read()
    img = detect(img, faceCascade)
    cv2.imshow('face detction', img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Terminating the loop by typing q
        break

live_video.release()  # start capturing the video
cv2.destroyAllWindows()
