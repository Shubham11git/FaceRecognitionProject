import face_recognition
import os

# For creating list of encodings and names for all the known faces 

def face_encodings(dir):
    face_encodings = []
    for file in os.listdir(dir):
        image = face_recognition.load_image_file(dir + '/' + file)
        image_encoding = face_recognition.face_encodings(image)[0]
        face_encodings.append(image_encoding)
    return face_encodings

def face_names(dir):
    face_names = []
    for file in os.listdir(dir):
        image_name = file.split('.')[0]
        face_names.append(image_name)
    return face_names