import cv2
import pytesseract as pyts 

def validate_document(image):
	img = cv2.imread(image)
	text_list = pyts.image_to_string(img).lower().split()

	stopwords = "a about after all also always am an and any are at be been being but by came can cant come could did didnt do does doesnt doing dont else for from get give goes going had happen has have having how i if ill im in into is isnt it its ive just keep let like made make many may me mean more most much no not now of only or our really say see some something take tell than that the their them then there they thing this to try up us use used uses very want was way we what when where which who why will with without wont you your youre"

	text_after_remove_sw = []
	for word in text_list:
		if word not in stopwords:
			text_after_remove_sw.append(word)

	medical_words = {'medical','nursing','healthcare','hospital','hospitals','emergency','Dr.', 'doctor', 'doctors',
					'report','injury','injuries','treatment','condition','patient'}

	score = 0
	for word in text_after_remove_sw:
		if word in medical_words:
			score += 1

	if score>0:
		return True, ','.join(text_after_remove_sw)
	else:
		return False, None