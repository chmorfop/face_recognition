import face_recognition

image_of_obama = face_recognition.load_image_file('./known/obama.jpg')

obama_face_encoding=face_recognition.face_encodings(image_of_obama)[0]

unknown_image = face_recognition.load_image_file('./unknown/proedros.jpg')

unknown_face_encoding=face_recognition.face_encodings(unknown_image)[0]

#print(obama_face_encoding)
#print(unknown_face_encoding)

#compare faces

results=face_recognition.compare_faces([obama_face_encoding], unknown_face_encoding)
#print(results)

if results[0]:
    print('This is Obama.')
else:
    print('This is not Obama.')
