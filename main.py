import face_recognition
import cv2
import numpy as np
import streamlit as st
# import os
# import tempfile

from main2 import *

st.title('Face Recognition')

username = 'Shubham11git'
repo_name = 'FaceRecognitionProject'
directory_path = 'images'

contents = get_directory_contents(username, repo_name, directory_path)
print(contents)

known_face_encodings = []
known_face_names = []

if contents:
    for item in contents:
        # st.write(item.split('.')[0])
        # # print(item)
        # image = face_recognition.load_image_file(item)
        # image_encoding = face_recognition.face_encodings(image)[0]
        image_name = item['name'].split('.')[0]

        # known_face_encodings.append(image_encoding)
        known_face_names.append(image_name)

print(known_face_names)

# known_image_dir = 'images'

# for file in os.listdir(known_image_dir):
#     image = face_recognition.load_image_file(known_image_dir + '/' + file)
#     image_encoding = face_recognition.face_encodings(image)[0]
#     image_name = file.split('.')[0]

#     known_face_encodings.append(image_encoding)
#     known_face_names.append(image_name)

# cap = cv2.VideoCapture(0)

# frame_placeholder = st.empty()
# stop_button_pressed = st.button('Stop')

# process_frame = True

# while cap.isOpened() and not stop_button_pressed:
#     ret, frame = cap.read()

#     if process_frame:
#         small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#         rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    
#         face_location = face_recognition.face_locations(rgb_small_frame)
#         rgb_frame_encoding = face_recognition.face_encodings(rgb_small_frame, face_location)
    
#         name_list = []

#         for face_encoding in rgb_frame_encoding:
#             match = face_recognition.compare_faces(known_face_encodings, face_encoding)
            
#             name = 'Unknown'

#             if True in match:
#                 index = match.index(True)
#                 name = known_face_names[index]

#             name_list.append(name)

#     for (top, right, bottom, left), name in zip(face_location, name_list):
#         top *= 4
#         right *= 4
#         bottom *= 4
#         left *= 4
        
#         if name == 'Unknown':
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#             font = cv2.FONT_HERSHEY_DUPLEX
#             cv2.putText(frame, name, (left, bottom + 20), font, 0.5, (255, 255, 255), 1)
#         else:
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#             font = cv2.FONT_HERSHEY_DUPLEX
#             cv2.putText(frame, name, (left, bottom + 20), font, 0.5, (255, 255, 255), 1)

#     process_frame = not process_frame

#     # cv2.imshow('Face', frame)

#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     frame_placeholder.image(frame, channels='RGB')
    
#     if cv2.waitKey(1) & 0xFF == ord('q') or stop_button_pressed:
#         break


# cap.release()
# cv2.destroyAllWindows()

