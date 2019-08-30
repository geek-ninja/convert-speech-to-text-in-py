import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
	print("Speak anything")
	r.adjust_for_ambient_noise(source)
	audio=r.listen(source)

	try:
		text=r.recognize_google(audio)
		print(text)
	except:
		print("Sorry can't listen")
