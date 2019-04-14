import face_recognition
from PIL import Image, ImageDraw

image_of_obama = face_recognition.load_image_file('./known/me.jpg')

obama_face_encoding=face_recognition.face_encodings(image_of_obama)[0]

image_of_stevejobs = face_recognition.load_image_file('./known/Steve_Jobs.jpg')

stevejobs_face_encoding=face_recognition.face_encodings(image_of_stevejobs)[0]


#Create an array of encoding and names
known_face_encodings=[
obama_face_encoding,
stevejobs_face_encoding
]

known_face_names=[
"Morf","Steve Jobs"
]

test_image = face_recognition.load_image_file('./group/groupkgamos.jpg')

#Find faces in test image
face_locations=face_recognition.face_locations(test_image)
face_encodings=face_recognition.face_encodings(test_image,face_locations)








#Convert to PIL format
pil_image= Image.fromarray(test_image)

#Create a ImageDraw instance
draw=ImageDraw.Draw(pil_image)

#loop through faces in test image
for(top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):
    matches= face_recognition.compare_faces(known_face_encodings, face_encoding)

    name="Unknown Person"

    #If match

    if True in matches:
        first_match_index=matches.index(True)
        name=known_face_names[first_match_index]

    #Draw a Box
    draw.rectangle(((left,top),(right,bottom)), outline=(0,0,0))


    #Draw label
    text_width, text_height =draw.textsize(name)
    draw.rectangle(((left,bottom-text_height-10),(right,bottom)),fill=(0,0,0),outline=(0,0,0))
    draw.text((left+6,bottom - text_height-5),name,fill=(255,255,255,255))

del draw

#Display Image
pil_image.show()
