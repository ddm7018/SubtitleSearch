import speech_recognition as sr

# obtain audio from the microphone

def speechToText():
	r = sr.Recognizer()
	with sr.Microphone() as source:
   		print("Say something!")
    	audio = r.listen(source)
# recognize speech using Google Speech Recognition
	
# for testing purposes, we're just using the default API key
# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
# instead of `r.recognize_google(audio)`
		
	try:
		transcribed = r.recognize_google(audio)
		print("Google Speech Recognition thinks you said " +transcribed )
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
	return transcribed
	
def inputToText():
	simpleText = raw_input('Simple Text Search:')
	return simpleText 
'''
fileName = raw_input('File name: ')
print fileName
with open(fileName+".wav","wb") as f:
	f.write(audio.get_wav_data())
	'''
'''    
with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file

try:
    print("Transcription: " + r.recognize(audio))   # recognize speech using Google Speech Recognition
except LookupError:                                 # speech is unintelligible
    print("Could not understand audio")
'''

#speechToText()