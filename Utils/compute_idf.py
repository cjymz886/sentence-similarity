#encoding:utf-8
from __future__ import absolute_import
import multiprocessing
import codecs
import math
import json
import time
from load_data import *

file_corpus='../data/file_corpus.txt'
file_voc='../data/voc.txt'
file_idf='../data/idf.txt'


class ComIdf(object):

    def __init__(self,file_corpus,file_voc,file_idf):
        self.file_corpus=file_corpus
        self.file_voc=file_voc
        self.file_idf=file_idf
        self.voc=load_voc(self.file_voc)
        self.corpus_data=self.load_corpus()
        self.N=len(self.corpus_data)

    def load_corpus(self):
        input_data = codecs.open(self.file_corpus, 'r', encoding='utf-8')
        return input_data.readlines()

    def com_idf(self,word):
        n = 0
        for _,line in enumerate(self.corpus_data):
           n+=line.count(word)
        idf=math.log(1.0*self.N/n+1)
        return {word:idf}

    def parts(self):
        words=set(self.voc.keys())
        multiprocessing.freeze_support()
        cores=multiprocessing.cpu_count()
        pool=multiprocessing.Pool(processes=cores-2)
        reuslt=pool.map(self.com_idf,words)
        idf_dict=dict()
        for r in reuslt:
            k=list(r.keys())[0]
            v=list(r.values())[0]
            idf_dict[k]=idf_dict.get(k,0)+v
        with codecs.open(self.file_idf,'w',encoding='utf-8') as f:
            f.write(json.dumps(idf_dict,ensure_ascii=False,indent=2,sort_keys=False))

if __name__ == '__main__':
    t1 = time.time()
    IDF=ComIdf(file_corpus,file_voc,file_idf)
    IDF.parts()
    print('-------------------------------------------')
    print("Computing idf of words cost %.3f seconds...\n" % (time.time() - t1))












