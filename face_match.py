import face_recognition

image_of_bill = face_recognition.load_image_file('F:/Software/Python_Facial_Recognition_Img/img/known/bill.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]


unknown_image = face_recognition.load_image_file('F:/Software/Python_Facial_Recognition_Img/img/unknown/kohli_test.jpg')
unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

#Compare faces

results = face_recognition.compare_faces([bill_face_encoding], unknown_image_encoding)

if results[0]:
    print('This is Bill Gates')
else:
    print('This is not Bill Gates')

