import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Hello, this is a test.")
for token in doc:
    print(token.text, token.pos_, token.dep_)
