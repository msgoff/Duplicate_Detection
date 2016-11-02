from simserver import SessionServer
from gensim import utils
import logging

service = SessionServer('/tmp/test/')

texts=['this is one document','this is the second','this is one document']


corpus = [{'id': 'doc_%i' % num, 'tokens': utils.simple_preprocess(text)}
           for num, text in enumerate(texts)]
service.train(corpus, method='lsi')
service.index(corpus)

lst=[]
for ix in corpus:
    score=service.find_similar(ix['id'])
    for item in score:
        if item[1]>.7:
            lst.append((ix['id'],item[0],item[1]) if ix['id']!=item[0] else '')


print lst
