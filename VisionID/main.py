import os
import cv2
import face_recognition
import numpy as np
import pandas as pd
from datetime import datetime

folder_path = 'attendance_data'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

attendance_file = os.path.join(folder_path, 'attendance.csv')

if not os.path.isfile(attendance_file):
    with open(attendance_file, 'w') as f:
        f.write('Name,Date,Time\n')

known_face_encodings = []
known_face_names = []

known_people_folder = 'known_people'
for filename in os.listdir(known_people_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(known_people_folder, filename)
        image = face_recognition.load_image_file(image_path)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(os.path.splitext(filename)[0])

video_capture = cv2.VideoCapture(0)

def mark_attendance(name):
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M:%S')
    df = pd.read_csv(attendance_file)
    if not ((df['Name'] == name) & (df['Date'] == date_str)).any():
        with open(attendance_file, 'a') as f:
            f.write(f'{name},{date_str},{time_str}\n')
        print(f'Attendance marked for {name} at {time_str} on {date_str}')

print("Press 'q' to exit video stream.")

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        if name != "Unknown":
            mark_attendance(name)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
