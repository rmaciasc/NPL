from textblob import TextBlob
import docx

doc = docx.Document('C:/Users/rmaci/OneDrive/Documentos/PythonScripts/MLtutorial/voice2txt/conv_trump.docx')

pars = doc.paragraphs

statement = []

for par in pars:
    statement.append(par.text)
type(statement)
statement = str(statement)

blob2 = TextBlob(statement)
lang = blob2.detect_language()
print(lang)
if lang == 'en':
    blob2_ready = blob2
else:
    blob2_ready = blob2.translate(to = 'en')

sentiment = blob2_ready.sentiment.polarity

if sentiment == 0:
    print('El cliente se mostró neutral.')
elif sentiment > 0:
    print(u'El cliente está satisfecho!')
else:
    print('El cliente nos odia!!!!!')