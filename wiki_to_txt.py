# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:02:55 2018

@author: Anan
"""

import logging
import os
import re
import codecs
import jieba
from opencc import OpenCC
from gensim.models import word2vec 

def cut(string): return list(jieba.cut(string))

def get_stopwords(filename = "D:/Code/Pycharm/Data_source/chinese_stopwords.txt"):
    stopwords_dic = open(filename, encoding= 'utf-8')
    stopwords = stopwords_dic.readlines()
    stopwords = [w.strip() for w in stopwords]
    stopwords_dic.close()
    print(stopwords)
    stopwords.append('\r\n')
    return stopwords

stopwords = get_stopwords()

def read(filename): 
    sline = ''
    with codecs.open(filename,'r','utf-8') as f:
        for line in f:
            sline += line.strip()
    return sline

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', raw_html)
    return cleantext
 
def cleanstopword(words):
    words = [w for w in words if len(w)>1 and not re.match('^[a-z|A-Z|0-9|.]*$',w)]
    words = [w for w in words if w not in stopwords]
    return words     

def convert2simple(word):
    openCC = OpenCC('tw2sp')
    return openCC.convert(word)

def wiki2txt(filename):
    output = open('wiki_seg.txt', 'a', encoding='utf-8')
    for root, dirs, files in os.walk(filename):
        for filename in files:
            file_path = root + '/' + filename
            content = read(file_path)
            clean = cleanhtml(content)
            converted = convert2simple(clean)
            cut_line = cleanstopword(cut(converted))
            line = ' '.join(cut_line)
            output.write(line)
    output.close()
        
wiki2txt("D:/Code/zhwiki-gensim-word2vec/AC")



