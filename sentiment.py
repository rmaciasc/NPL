from textblob import TextBlob
import docx
import os

dir = os.path.dirname(__file__)

conv = os.path.join(dir, 'conv_trump.docx')

doc = docx.Document(conv)

pars = doc.paragraphs

statement = []

for par in pars:
    statement.append(par.text)
statement = str(statement)

blob2 = TextBlob(statement)
lang = blob2.detect_language()

newline = '\n'
print(f'Idioma detectado: {lang}. {newline}Calculando polaridad sentimental...')

if lang == 'en':
    blob2_ready = blob2
else:
    blob2_ready = blob2.translate(to = 'en')

sentiment = blob2_ready.sentiment.polarity

print(f'{newline}La polaridad sentimental es de: {sentiment}. {newline}Lo que significa que:')

if sentiment == 0:
    print('El cliente se muestra neutral.')
elif sentiment > 0:
    print(u'El cliente se muestra satisfecho!')
else:
    print('El cliente se muestra insatisfecho.')