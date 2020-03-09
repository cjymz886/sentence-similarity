# sentence-similarity
对四种句子/文本相似度计算方法进行实验与比较；<br>
四种方法为:cosine,cosine+idf,bm25,jaccard；<br>
本实验仍然利用之前抓取的医疗语料库；<br>

1 环境
=
python3<br>
gensim<br>
jieba<br>
scipy<br>
numpy<br>

2 算法原理
=
![image](https://github.com/cjymz886/sentence-similarity/raw/master/images/cosine.png)<br>
![image](https://github.com/cjymz886/sentence-similarity/raw/master/images/idf.png)<br>
![image](https://github.com/cjymz886/sentence-similarity/raw/master/images/bm25.png)<br>
![image](https://github.com/cjymz886/sentence-similarity/raw/master/images/jaccard.png)<br>

3 运行步骤
=
setp1:先利用word2vec对./data/file_corpus进行词向量训练(python train_word2vec.py)，生成voc.txt词向量文件<br>
setp2:对训练出来的词，计算其在语料库中idf词(python compute_idf.py),生成idf.txt文件<br>
setp3:统计语料库中存在的句子(python get_sentence.py),生成file_sentece.txt文件;考虑计算量问题，本实验只取了出现频率最高的前10000个句子<br>
setp4：运行python test.py，可对设定好的5个句子，按照不同的算法得出最相似的结果

备注说明：./data/medfw.txt文件是我上个项目find-Chinese-medcial-words在同样语料库找出的词文件，本次作为用户词库参与jieba分词;similarity.py文件为四种算法实现的程序，可以调用，不同的环境下只需重新训练词向量和词的idf矩阵；./data/test_result.txt文件是本实验测试结果。<br>


4 测试结果
=
下面表格是对5个相同的句子进行测试的结果，结果可以看出，cosine+idf方法计算复杂度最大，但效果就我个人来看，此方法相对其他方法结果更精确些；bm25算法对有些句子匹配显得有点偏离，我觉得可能跟调节因子k1，b有关；jaccard方法最为简单，计算也是最快，计算结果带不上语义效果；cosine方法算是最常用方法，它的结果非常依赖Word2vec训练的结果。

![image](https://github.com/cjymz886/sentence-similarity/raw/master/images/result.png)<br>


![image](https://github.com/cjymz886/sentence-similarity/blob/master/images/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86%E7%AE%97%E6%B3%95%E4%B8%8E%E5%AE%9E%E8%B7%B5.png)<br>


