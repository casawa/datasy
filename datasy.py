"""
This module provides various NLP data processing and representation tools.
"""

from __future__ import print_function
import numpy as np
import sys
import string

class datasy:
    """
    Converts the words in the data into Glove word vectors.
    """
    def conv_glove_word_vectors(self, wv_path, size=50):
        pass

    """
    Converts the data into a bag of words representation.
    """
    def conv_bag_of_words(self):
        #self.train_X = np.zeros((len(self.raw_train, self.vocab_size))
        pass

    """
    Converts the data into a sparse vector representation.
    """
    def conv_sparse_vector(self):
        pass

    """
    Removes punctuation for the data given
    """
    def __remove_punct(self, data):
        no_punct = []
        for example in data:
            no_punct_example = [token.translate(None, string.punctuation) for token in example]
            no_punct.append(no_punct_example)

        data = no_punct

    """
    Removes punctuation from the text data.
    """
    def remove_punctuation(self):
        pass

    """
    Stems the data.
    """
    def stem(self):
        pass

    """
    Removes stop words for the data given.
    """
    def __remove_stop(self, data):
        #nonstop = []
        #for example in data:
        #    removed = 

        data = nonstop

    """
    Removes stop words from the data.
    """
    def remove_stop_words(self):
       pass 

    """
    Lowercases the data given.
    """
    def __lower_data(self, data):
        lowered = []
        for example in data:
            lowered_example = [token.lower() for token in example]
            lowered.append(example)

        data = lowered

    """
    Converts all the data into lowercase. 
    """
    def lowercase(self):
        pass

    """
    Given the split ratio, splits the training data into a training and dev set
    """
    def create_dev(self, split=10):
        pass

    """
    Builds the vocabulary for the data.
    """
    def build_vocab(self):

        # self.word_to_id = {}
        # self.vocab_size = len(self.vocab)
        pass

    def __init__(self, train_path=None, test_path=None):
        self.train_X = None
        self.train_y = None
        self.test_X = None
        self.test_y = None

        self.raw_train = []
        if train_path is not None:
            with open(train_path, 'r') as train_file:


