import face_recognition
import cv2
import numpy as np
import streamlit as st
import os
import tempfile

import requests

def get_directory_contents(base_url): #username, repo_name, path, branch='master'):
    # base_url = f'https://api.github.com/repos/{username}/{repo_name}/contents/{path}?ref={branch}'
    response = requests.get(base_url)

    if response.status_code == 200:
        contents = response.json()
        return contents
    else:
        st.write(f"Failed to retrieve directory contents. Status code: {response.status_code}")
        return None

# Replace these with your GitHub username, repository name, and directory path
# username = 'Shubham11git'
# repo_name = 'FaceRecognitionProject'
# directory_path = 'images'

url = 'https://github.com/Shubham11git/FaceRecognitionProject/tree/main/images'
contents = get_directory_contents(url)

if contents:
    for item in contents:
        st.write(item.split('.')[0])
