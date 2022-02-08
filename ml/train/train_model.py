import model
import tensorflow as tf
import numpy as np
import json
from gensim.models import KeyedVectors
def data_to_vectors(data_location):
    mod = KeyedVectors.load_word2vec_format('/home/sarthak/Desktop/Word2Vec/GoogleNews-vectors-negative300.bin',binary=True)
    file = open(data_location,'r')
    final_vector = np.array([])
    final_label = np.array([])
    newspost = json.loads(file.read())
    for i in newspost:
        text_data = i['text']
        label = i['label']
        text_data = model.tokenize(text_data)
        vector = model.vectorize(text_data,mod)
        try:
            final_vector = np.vstack((final_vector,vector))
            final_label = np.vstack((final_label,label))
        except:
            final_vector = np.append(final_vector,vector)
            final_label = np.append(final_label, label)
    return final_vector,final_label
def nn_model(data_location):
    vector,label = data_to_vectors(data_location)
    nn = tf.keras.Sequential()
    nn.add(tf.keras.layers.Dense(300,input_shape=(300,)))
    nn.add(tf.keras.layers.Dense(151,activation='relu'))
    nn.add(tf.keras.layers.Dense(2,activation='sigmoid'))
    nn.compile(optimizer=tf.train.AdamOptimizer(0.001), loss='mean_squared_error', metrics=['accuracy'])
    nn.fit(vector,label,batch_size=10,epochs=30)
    tf.keras.models.save_model(nn,'Fakenews.model')

if __name__ == '__main__':
    nn_model('/home/sarthak/PycharmProjects/Word2Vec/ml/train/Data/Train/fake.txt')
