# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:02:55 2018

@author: Anan
"""
from gensim.models import word2vec
from gensim import models
import logging
from sklearn.manifold import TSNE

from matplotlib import pylab
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] 
mpl.rcParams['axes.unicode_minus'] = False 

def plot(embeddings, labels):
    assert embeddings.shape[0] >= len(labels), 'More labels than embeddings'
    pylab.figure(figsize=(15,15),dpi=600)  
    for i, label in enumerate(labels):
        x, y = embeddings[i,:]
        pylab.scatter(x, y)
        pylab.annotate(label, xy=(x, y), xytext=(5, 2), textcoords='offset points',ha='right', va='bottom')
    pylab.show()

def show_word(word_start,word_end):
    tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000, method='exact')
    two_d_embeddings = tsne.fit_transform(X[word_start:word_end, :])
    plot(two_d_embeddings, wordVocab[word_start:word_end])
    
def main():    
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = models.Word2Vec.load('word2vec.model')
    
    wordVocab = [k for (k,v) in model.wv.vocab.items()]
    X = model[model.wv.vocab]
    
    show_word(1000,1100)

if __name__ == '__main__':
    main()




