import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import tensorflow as tf
import numpy as np
import nltk
import random
import json
import pickle

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')

lemmatizer = nltk.WordNetLemmatizer()

intents = json.loads(open('data.json').read())

words = []
classes = []
documents = []
ignore_letters = ['!', '?', ',', '.', '-', '_', '/', '\'']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]

words = sorted(set(words))
classes = sorted(set(classes))

pickle.dump(words, open('words.pk1', 'wb'))             # Dumping into two pickle files. 'wb' stands for "write binary".
pickle.dump(classes, open('classes.pk1', 'wb'))         # We do this to not repeat ourselves and to imcrease efficiency.

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

