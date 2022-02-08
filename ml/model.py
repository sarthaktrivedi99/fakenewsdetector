import tensorflow as tf
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
def vectorize(data):
    model = KeyedVectors.load_word2vec_format('/home/sarthak/Desktop/Word2Vec/GoogleNews-vectors-negative300.bin',binary=True)
    number_data=len(data)
    final_vector= np.zeros(300,)
    for i in data:
        try:
            final_vector=final_vector+ model[i]
        except:
            logging.debug(i + "not Found in Word2Vec model")
    final_vector=final_vector/number_data
        
    return final_vector
def nn_model(vector):
	tf.keras.backend.clear_session()
	nn = tf.keras.models.load_model('/home/sarthak/PycharmProjects/FakeNews/ml/train/Fakenews.model')
	prediction = nn.predict(x=vector)
	return str(prediction)