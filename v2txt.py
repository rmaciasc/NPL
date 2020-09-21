import speech_recognition as sr
from textblob import TextBlob

r = sr.Recognizer()
mic= sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    print('Recording... Please speak now.')
    audio = r.listen(source)

trans = r.recognize_google(audio, language= 'es-ES')
print(trans)

blob2 = TextBlob(trans)
lang = blob2.detect_language()

newline = '\n'
print(f'Detected language: {lang}. {newline}Getting sentiment polarity...')

if lang == 'en':
    blob2_ready = blob2
else:
    blob2_ready = blob2.translate(to = 'en')

sentiment = blob2_ready.sentiment.polarity

print(f'{newline}Sentiment polarity: {sentiment}. {newline}This means:')

if sentiment == 0:
    print('Customer was neutral.')
elif sentiment > 0:
    print('Customer was satisfied!')
else:
    print('Customer was not satisfied.')