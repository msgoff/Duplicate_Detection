from simserver import SessionServer
from gensim import utils
import logging

service = SessionServer('/tmp/')

#put the content you want to compare in this list. 
texts=['this is one document','this is one second','this is one document','this is one second']


corpus = [{'id': 'doc_%i' % num, 'tokens': utils.simple_preprocess(text)}
           for num, text in enumerate(texts)]
service.train(corpus, method='lsi')
service.index(corpus)

lst=[]
for ix in corpus:
    score=service.find_similar(ix['id'])
    for item in score:
        print item[1]
	if item[1]>.7:      #Closer to 1 means identical content
            lst.append((ix['id'],item[0],item[1]) if ix['id']!=item[0] else '')


print lst
#print service.find_similar('doc_1')
