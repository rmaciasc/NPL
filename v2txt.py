import speech_recognition as sr
from textblob import TextBlob

r = sr.Recognizer()
mic= sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    print('Empieza a hablar muchaho!')
    audio = r.listen(source)

trans = r.recognize_google(audio, language= 'es-ES')
print(trans)

blob2 = TextBlob(trans)
lang = blob2.detect_language()
print(lang)
if lang == 'en':
    blob2_ready = blob2
else:
    blob2_ready = blob2.translate(to = 'en')

sentiment = blob2_ready.sentiment.polarity

if sentiment == 0:
    print('El cliente se mostro neutral.')
elif sentiment > 0:
    print('El cliente esta satisfecho!')
else:
    print('El cliente nos odia!!!!!')