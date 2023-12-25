# Face Recognition Web Application
This is a Face Recognition Web Application developed using Streamlit.

This application used webcam of a device to detect the faces and match those faces with the faces available in the 'images' directory (included in the repository).

**face_recognition** library has been used to detect the faces from webcam and match those faces with the available faces.

**OpenCV** has been used for image processing operations.

This repository contains two python files: 1. local.py 2. server.py

To run the app on local machine, local.py can be used. OpenCV, Numpy, face_recognition library, and streamlit must be installed on the local machine. This code can also be modified to run the app without the use of streamlit on the local machine.

To deploy the app on remote server, server.py has been used. For deploying the app on the remote server, streamlit_webrtc, streamlit, face_recognition, OpenCV, and Numpy must be installed on the remote server platform.