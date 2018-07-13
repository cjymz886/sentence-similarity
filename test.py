#encoding:utf-8

import codecs
import similarity
import json
import time


def test():
    test_data=[u'临床表现及实验室检查即可做出诊断',
               u'面条汤等容易消化吸收的食物为佳',
               u'每天应该摄入足够的维生素A',
               u'视患者情况逐渐恢复日常活动',
               u'术前1天开始预防性运用广谱抗生素']
    model_list=['cosine','idf','bm25','jaccard']
    file_sentence=codecs.open('./data/file_sentence.txt','r',encoding='utf-8')
    train_data=file_sentence.readlines()
    for model in model_list:
        t1 = time.time()
        dataset=dict()
        result=dict()
        for s1 in test_data:
            dataset[s1]=dict()
            for s2 in train_data:
                s2=s2.strip()
                if s1!=s2:
                    sim=similarity.ssim(s1,s2,model=model)
                    dataset[s1][s2]=dataset[s1].get(s2,0)+sim
        for r in dataset:
            top=sorted(dataset[r].items(),key=lambda x:x[1],reverse=True)
            result[r]=top[0]
        with codecs.open('./data/test_result.txt','a') as f:
            f.write('--------------The result of %s method------------------\n '%model)
            f.write('\tThe computing cost %.3f seconds\n'% (time.time() - t1))
            f.write(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=False))
            f.write('\n\n')

    file_sentence.close()


test()




