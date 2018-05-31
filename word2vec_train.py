# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:02:55 2018

@author: Anan
"""

import logging

from gensim.models import word2vec

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence("wiki_seg.txt")
    model = word2vec.Word2Vec(sentences, size=250)

    model.save("word2vec.model")


if __name__ == "__main__":
    main()

