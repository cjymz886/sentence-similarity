#encoding:utf-8
import os
import logging
import re
import time
import codecs
import jieba
from gensim.models import word2vec

file_corpus='../data/file_corpus.txt'
file_userdict='../data/medfw.txt'
file_voc='../data/voc.txt'

re_han= re.compile(u"([\u4E00-\u9FD5a-zA-Z0-9+#&\._%]+)") # the method of cutting text into sentences in jieba


class MySentences(object):
    def __init__(self, file_corpus,file_userdict):
        self.file_corpus = file_corpus
        jieba.load_userdict(file_userdict)

    def __iter__(self):
        with codecs.open(self.file_corpus,'r',encoding='utf-8') as f:
            for _,line in enumerate(f):
                blocks=re_han.split(line.strip())
                seglist=[]
                for blk in blocks:
                    if re_han.match(blk):
                        seglist.extend(jieba.lcut(blk))
                yield seglist


if __name__ == '__main__':
    t1 = time.time()
    sentences=MySentences(file_corpus,file_userdict)
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model=word2vec.Word2Vec(sentences,size=50,window=5,min_count=1,workers=6)
    model.wv.save_word2vec_format(file_voc, binary=False)
    print('-------------------------------------------')
    print("Training word2vec model cost %.3f seconds...\n" % (time.time() - t1))