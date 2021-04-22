import cv2

data_set = 'frontalface_dataset.xml'  # dataset
faceCascade = cv2.CascadeClassifier(data_set)

video_capture = cv2.VideoCapture(0)  

def camera_stream():
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Drawing a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Displaying the resulting frame in browser
    return cv2.imencode('.png', frame)[1].tobytes()



def gen_frame():
    """Video streaming generator function."""
    while True:
        frame = camera_stream()
        yield (b'--frame\r\n'
               b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n') # concate frame one by one and show result