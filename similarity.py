#encoding:utf-8
from __future__ import absolute_import
import jieba
import time
from scipy import spatial
import numpy as np

from Utils.load_data import *

file_voc='./data/voc.txt'
file_idf='./data/idf.txt'
file_userdict='./data/medfw.txt'

class SSIM(object):

    def __init__(self):
        t1 = time.time()
        self.voc=load_voc(file_voc)
        print("Loading  word2vec vector cost %.3f seconds...\n" % (time.time() - t1))
        t1 = time.time()
        self.idf=load_idf(file_idf)
        print("Loading  idf data cost %.3f seconds...\n" % (time.time() - t1))
        jieba.load_userdict(file_userdict)

    def M_cosine(self,s1,s2):
        s1_list=jieba.lcut(s1)
        s2_list=jieba.lcut(s2)

        v1=np.array([self.voc[s] for s in s1_list if s in self.voc])
        v2=np.array([self.voc[s] for s in s2_list if s in self.voc])

        v1=v1.sum(axis=0)
        v2=v2.sum(axis=0)

        sim=1-spatial.distance.cosine(v1,v2)

        return sim

    def M_idf(self,s1, s2):
        v1, v2 = [], []
        s1_list = jieba.lcut(s1)
        s2_list = jieba.lcut(s2)

        for s in s1_list:
            idf_v = self.idf.get(s, 1)
            if s in self.voc:
                v1.append(1.0 * idf_v * self.voc[s])

        for s in s2_list:
            idf_v = self.idf.get(s, 1)
            if s in self.voc:
                v2.append(1.0 * idf_v * self.voc[s])

        v1 = np.array(v1).sum(axis=0)
        v2 = np.array(v2).sum(axis=0)

        sim = 1 - spatial.distance.cosine(v1, v2)

        return sim

    def M_bm25(self,s1, s2, s_avg=10, k1=2.0, b=0.75):
        bm25 = 0
        s1_list = jieba.lcut(s1)
        for w in s1_list:
            idf_s = self.idf.get(w, 1)
            bm25_ra = s2.count(w) * (k1 + 1)
            bm25_rb = s2.count(w) + k1 * (1 - b + b * len(s2) / s_avg)
            bm25 += idf_s * (bm25_ra / bm25_rb)
        return bm25

    def M_jaccard(self,s1, s2):
        s1 = set(s1)
        s2 = set(s2)
        ret1 = s1.intersection(s2)
        ret2 = s1.union(s2)
        jaccard = 1.0 * len(ret1)/ len(ret2)

        return jaccard

    def ssim(self,s1,s2,model='cosine'):

        if model=='idf':
            f_ssim=self.M_idf
        elif model=='bm25':
            f_ssim=self.M_bm25
        elif model=='jaccard':
            f_ssim=self.M_jaccard
        else:
            f_ssim = self.M_cosine

        sim=f_ssim(s1,s2)

        return sim

sm=SSIM()
ssim=sm.ssim