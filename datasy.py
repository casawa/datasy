"""
This module provides various NLP data processing tools.
"""

from __future__ import print_function
import numpy as np
import sys
import string

class datasy:
    """
    Converts the words in the data into word vectors.
    """
    def conv_word_vectors(self, size=50):
        pass

    """
    Converts the data into a bag of words representation.
    """
    def conv_bag_of_words(self):
        pass

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
    Removes stop words from the data.
    """
    def remove_stop_words(self):
        pass

    """
    Converts all the data into lowercase. 
    """
    def lowercase(self):
        pass

    """
    Builds the vocabulary for the data.
    """
    def build_vocab(self):
        pass


    def __init__(self, train_path=None, test_path=None):
        pass
        # if train_path is not None:
