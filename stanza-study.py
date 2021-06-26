#Most of code from sample. Edited to test out.
import stanza

#Uncomment Below if you need to download English models
#stanza.download('en')

nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt')
doc = nlp('What is your favorite food?')
for token in doc.sentences[0].tokens:
    print(f'token: {token.text}\twords: {", ".join([word.text for word in token.words])}')
