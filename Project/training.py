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
nltk.download('omw-1,4')

lemmatizer = nltk.WordNetLemmatizer()

intents = json.loads(open('data.json').read())