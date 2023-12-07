import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

import face_recognition
import cv2
import numpy as np

import os
import av



class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        # Define any initialization code here
        # self.i = 0
        pass
    
    
    def recv(self, frame):
        # Process the frame (e.g., apply filters, perform analysis)
        process_frame = False

        known_face_encodings = []
        known_face_names = []

        known_image_dir = 'images'

        for file in os.listdir(known_image_dir):
            image = face_recognition.load_image_file(known_image_dir + '/' + file)
            image_encoding = face_recognition.face_encodings(image)[0]
            image_name = file.split('.')[0]
            known_face_encodings.append(image_encoding)
            known_face_names.append(image_name)

        if process_frame:
            img = frame.to_ndarray(format='bgr24')

            small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        
            face_location = face_recognition.face_locations(rgb_small_frame)
            rgb_frame_encoding = face_recognition.face_encodings(rgb_small_frame, face_location)
        
            name_list = []

            for face_encoding in rgb_frame_encoding:
                match = face_recognition.compare_faces(known_face_encodings, face_encoding)
                
                name = 'Unknown'

                if True in match:
                    index = match.index(True)
                    name = known_face_names[index]

                name_list.append(name)

            process_frame = True

        for (top, right, bottom, left), name in zip(face_location, name_list):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
        
            if name == 'Unknown':
                cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(img, name, (left, bottom + 20), font, 0.5, (255, 255, 255), 1)
            else:
                cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(img, name, (left, bottom + 20), font, 0.5, (255, 255, 255), 1)
            # In this example, we simply return the frame without any processing
        return av.VideoFrame.from_ndarray(img, format='bgr24')

def main():

    

    st.title("Face Recognition")

        # Create a WebRTC component with the VideoTransformer class
    webrtc_ctx = webrtc_streamer(
            key="sample",
            video_processor_factory=VideoProcessor,
            async_processing=True,
            sendback_audio=False,
            rtc_configuration={  # Add this config
            "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        }
        )

   
main()
