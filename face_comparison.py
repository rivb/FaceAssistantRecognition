import face_recognition
from datetime import date
from add_drive import create_csv
import csv
import time

def face_comparison(name,saved_image,unknown_image):

	#create csv. If is already created pass open it
	try:
		open("persons.csv")
	except:
		create_csv()


	#encode picture of the user.
	picture_of_me = face_recognition.load_image_file(saved_image)
	my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

	#check time that algorithm take to recognize
	start = time.time()

	unknown_picture = face_recognition.load_image_file(unknown_image)
	unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
	# Now we can see the two face encodings are of the same person with `compare_faces`!

	end = time.time()

	print(end-start)

	results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

	today = str(date.today())

	if results[0] == True:

	    with open('persons.csv', 'w') as csvfile:
	    	filewriter = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    	filewriter.writerow([name, today])

	    print("It's a picture of me!")

	else:

	    print("It's not a picture of me!")

