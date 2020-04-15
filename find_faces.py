import face_recognition

image = face_recognition.load_image_file('F:/Software/Python_Facial_Recognition_Img/img/group/team-3.jpg')

face_location = face_recognition.face_locations(image)

#Array of co-ordiantes of faces

# print(face_location)

print(f'There are total of {len(face_location)} people in the image')
