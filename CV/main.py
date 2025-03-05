import cv2

# Load the pre-trained face detection model
face_ref = cv2.CascadeClassifier('face_ref.xml')
camera = cv2.VideoCapture(0)

# List of names corresponding to detected faces
names = ["King Fatwa"]  # Start with the first name
next_person_id = 2  # Counter for new people

def face_detection(frame):
    optimize_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_ref.detectMultiScale(optimize_frame, scaleFactor=1.1, minSize=(100, 100))
    return faces

def drawer_box(frame):
    global next_person_id  # Use global variable to track new people
    faces = face_detection(frame)

    for i, (x, y, w, h) in enumerate(faces):
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)

        # Display the name above the rectangle
        if i < len(names):
            cv2.putText(frame, names[i], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

def close_win():
    camera.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        _, frame = camera.read()
        frame = cv2.flip(frame, 1)  # Flip the frame horizontally
        drawer_box(frame)
        cv2.imshow('FatwaAI', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            close_win()

if __name__ == '__main__':
    main()
