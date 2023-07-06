#::::::::::::::::::::::::::::::::: FACE RECOGNITION  ATTENDANCE  SYSTEM :::::::::::::::::::::::::::::::;
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> BY HMC  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# pip install face_recognition
# pip install cmake
#  pip install opencv-python
# pip install numpy

# Import the required libraries
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Initialize the video capture object for the default camera
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Load known faces
harshs_image = face_recognition.load_image_file("faces/harsh.jpg")  # Load image file for Harsh
harsh_encoding = face_recognition.face_encodings(harshs_image)[0]  # Encode the face of Harsh

sundarams_image = face_recognition.load_image_file("faces/sundaram.jpg")  # Load image file for Sundaram
sundaram_encoding = face_recognition.face_encodings(sundarams_image)[0]  # Encode the face of Sundaram

known_face_encodings = [harsh_encoding, sundaram_encoding]  # List of known face encodings
known_face_names = ["Harsh Mishra", "Kumar Sundaram"]  # List of known face names

# Create a copy of the known face names for expected students
students = known_face_names.copy()

# Initialize variables for face locations and encodings
face_locations = []
face_encodings = []

# Get the current time
now = datetime.now()
current_date = now.strftime("%d-%m-%y")

# Open a CSV file for writing attendance
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

# Start the main video capture loop
while True:
    _, frame = video_capture.read()  # Read the current frame from the video capture

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # Resize the frame for faster processing
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)  # Convert the frame to RGB color space

    # Recognize faces in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame)  # Locate faces in the frame
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)  # Encode faces in the frame

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)  # Compare face encodings
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)  # Calculate face distance
        best_match_index = np.argmin(face_distance)  # Get the index of the best match

        if matches[best_match_index]:  # If the face is a match
            name = known_face_names[best_match_index]  # Get the corresponding name

        # Add text if the person is present
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + " PRESENT ", bottomLeftCornerOfText, 0, fontScale, fontColor, thickness, lineType)

            if name in students:  # If the student is in the list of expected students
                students.remove(name)  # Remove the student from the list
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])  # Write the student's name and current time to theattendance CSV file

    cv2.imshow(" HMC Attendance ", frame)  # Display the frame with attendance information

    if cv2.waitKey(1) & 0xFF == ord("q"):  # Break the loop if 'q' is pressed
        break

# Release the video capture object and close windows
video_capture.release()
cv2.destroyAllWindows()
f.close()
