#encoding:utf-8

import codecs
import re

re_han= re.compile(u"([\u4E00-\u9FD5a-zA-Z0-9+#&\._%]+)")  #the method of cutting text to sentence

def get_sentence():
    file_corpus=codecs.open('../data/file_corpus.txt','r',encoding='utf-8')
    file_sentence=codecs.open('../data/file_sentence.txt','w',encoding='utf-8')

    st=dict()
    for _,line in enumerate(file_corpus):
        line=line.strip()
        blocks=re_han.split(line)
        for blk in blocks:
            if re_han.match(blk) and len(blk)>10:
                st[blk]=st.get(blk,0)+1

    st=sorted(st.items(),key=lambda x:x[1],reverse=True)
    for s in st[:10000]:
        file_sentence.write(s[0]+'\n')


    file_corpus.close()
    file_sentence.close()

get_sentence()