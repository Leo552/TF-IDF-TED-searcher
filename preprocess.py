from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

def remove_stop_words(text):
    text = re.split(r'[;,.\s]\s*', text)
    stop_words = stopwords.words('english')
    index_to_remove = []
    
    for i in range(len(text)):
        
        # Make the word lower case
        text[i] = text[i].lower()
        
        # Remove the word if the word is a stop word
        if text[i] in stop_words:
            index_to_remove.append(i)
            continue

    for index in index_to_remove[::-1]:
        text.pop(index)
    
    return text

def remove_symbols(text):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n\r0123456789',"
    for symbol in symbols:
        text = text.replace(symbol, ' ')
        
    return text

def remove_apostrophes(text):
    return [word.replace('`', '') for word in text]

def stemming(text):
    stemmer = PorterStemmer()
    
    for i in range(len(text)):
        text[i] = stemmer.stem(text[i])
    
    return text

def preprocess_query(query):
    text = query

    text = remove_symbols(text)
    text = remove_stop_words(text)
    text = remove_apostrophes(text)
    text = stemming(text)
    
    return text
