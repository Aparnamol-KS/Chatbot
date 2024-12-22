import random
import json
import pickle
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model


def clean_up_sentence(sentence):
    lemmatizer =  WordNetLemmatizer()
    ignore_symbols = ['?','!','.',',']

    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words if word not in ignore_symbols]

    return sentence_words


def bag_of_words(sentence):
    words = pickle.load(open('Flask Application/model/words.pkl', 'rb'))

    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    classes = pickle.load(open('Flask Application/model/classes.pkl', 'rb'))
    model = load_model('Flask Application/model/chatbot_model.keras')


    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25

    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []

    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})

    return return_list


def get_response(intents_list):
    intents_json = json.load(open('Flask Application/model/intents.json'))
    if not intents_list: 
        return "I'm sorry, I didn't catch that."
    
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']


    result = "I'm sorry, I don't understand that."

    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break

    return result
