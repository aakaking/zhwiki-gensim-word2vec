# zhwiki-gensim-word2vec

## The goal of this assignment is to train a Word2Vec using gensim over zhwiki(http://dumps.wikimedia.org/zhwiki/latest/) data and show the result by TSNE.

## 用Wikipedia的中文数据训练Word2Vec

1 下载数据(http://dumps.wikimedia.org/zhwiki/latest/)

2 解压数据 WikiExtractor

3 数据准备
  + a. jieba切词
  + b. 数据清洗、去停用词
  + c. 繁体化简体 OpenCC
  
4 用gensim 训练 Word2Vec 

5 结果显示 TSNE
