# Tweets_pre_processing.py
# Author: Cheng XU
# Date created: 15/01/2023
# Last modified: 06/03/2023
# Github page for this code: https://github.com/chengxuphd/AROT-COV23
#
# Description: A Python script for pre-processing tweets data.

import pandas as pd
import numpy as np
import tqdm
import re
import arabic_reshaper
from bidi.algorithm import get_display
from nltk.stem.isri import ISRIStemmer
import gensim
from nltk.corpus import stopwords
import nltk

import warnings
warnings.filterwarnings("ignore")

nltk.download('stopwords')

# Set the workspace path here
workspace = '/content/drive/MyDrive/'


def clean_text(text):
  # Remove any non-Arabic characters
  text = re.sub(r'[^\u0621-\u064A]', ' ', text)
  # Remove extra white space
  text = re.sub(r'\s+', ' ', text)
  return text

def normalize_text(text):
  # Use Arabic reshaper to restore characters to their correct form
  text = arabic_reshaper.reshape(text)
  # Use bidirectional algorithm to adjust character order for display
  text = get_display(text)
  return text

def tokenize_text(text):
  # Split text into a list of words
  words = text.split()
  return words

def remove_stop_words(sentence):
  # Remove stop words from the tokens
  stop_words = set(stopwords.words('arabic'))
  filtered_tokens = [token for token in sentence if token not in stop_words]
  return filtered_tokens

def stem_words(words):
  # Initialize ISRI stemmer
  stemmer = ISRIStemmer()
  # Stem each word in the list of words
  stemmed_words = [stemmer.stem(word) for word in words]
  return stemmed_words

def word_embedding(words):
  # Train a word2vec model on the list of words
  # model = gensim.models.Word2Vec([words], min_count=1, size=100, batch_words=10)
  model = gensim.models.Word2Vec()
  model.build_vocab(words)
  # Use the model to get the vector representation of each word
  # word_vectors = [model.wv[word] for word in words]
  # Train the Word2Vec model on the filtered tokens
  model.train(words, total_examples=len(words), epochs=10)

  # Get the word vectors for the model
  word_vectors = model.wv

  return word_vectors

def preprocess(text): 
  warnings.filterwarnings(action='ignore',category=UserWarning,module='gensim')  
  warnings.filterwarnings(action='ignore',category=FutureWarning,module='gensim')     
  text = clean_text(text)
  text = normalize_text(text)
  words = tokenize_text(text)
  words = remove_stop_words(words)
  stemmed_words = stem_words(words)
  # word_vectors = word_embedding(stemmed_words)
  return stemmed_words


# Read data file
data = pd.read_csv(workspace + 'Arabic_Tweets.csv')

text_data = []
# for i in tqdm.tqdm(range(len(data))):
for i in tqdm.tqdm(range(100)):
  # data['tweet'][i] = preprocess(data['tweet'][i])
  text_data.append(preprocess(data['tweet'][i]))

data.to_csv(workspace + 'Arabic_Tweets_Processed.csv')