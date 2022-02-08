from tensorflow import keras
import numpy as np
import logging
from gensim.models import KeyedVectors
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
def tokenize(data):
    stop_words = set(stopwords.words('english'))
    word_tokens = RegexpTokenizer(r'\w+').tokenize(data)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    return filtered_sentence
def vectorize(data,model):
    number_data=len(data)
    final_vector= np.zeros(300,)
    for i in data:
        try:
            final_vector=final_vector+ model[i]
        except:
            logging.debug(i + "not Found in Word2Vec model")
    #print(final_vector)
    print(number_data)
    final_vector=final_vector/number_data
    return final_vector
