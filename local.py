# This code can be used to run the app on local machine only

import face_recognition
import cv2
import numpy as np
import streamlit as st
from face_encodeings_names import *


st.title('Face Recognition')

directory = "images"

known_face_encodings = face_encodings(directory) 

known_face_names = face_names(directory) 

# Using the webcam of local device
cap = cv2.VideoCapture(0)

frame_placeholder = st.empty() 
stop_button_pressed = st.button('Stop') 

process_frame = True

while cap.isOpened() and not stop_button_pressed:
    ret, frame = cap.read() # To read each frame from webcam

    # For processing every other frame to make the code run faster
    if process_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25) # Frame has been reduced in size to its 25%
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB) # Converting frame to  RGB, because face_recognition library 
                                                                       # uses RGB frame and OpenCV creates BGR frame by defaul

        face_location = face_recognition.face_locations(rgb_small_frame) # To draw rectangle on face
        rgb_frame_encoding = face_recognition.face_encodings(rgb_small_frame, face_location)
    
        name_list = []
        
        # For every face visible in webcam
        for face_encoding in rgb_frame_encoding:
            match = face_recognition.compare_faces(known_face_encodings, face_encoding)
            
            name = 'Unknown'

            if True in match:
                index = match.index(True)
                name = known_face_names[index]

            name_list.append(name)

    # Scaling up the face locations and drawing rectangle on faces
    for (top, right, bottom, left), name in zip(face_location, name_list):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        
        if name == 'Unknown':
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left, bottom + 20), font, 0.5, (255, 255, 255), 1)
        else:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left, bottom + 20), font, 0.5, (255, 255, 255), 1)

    process_frame = not process_frame


    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame_placeholder.image(frame, channels='RGB')

    if stop_button_pressed:
        break


