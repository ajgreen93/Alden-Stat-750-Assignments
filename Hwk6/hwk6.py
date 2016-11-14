import numpy as np
import random
import os
from hwk5 import dcos

##find closest k documents according to cosine distance
def IrSearch(BoW,BoWcorpus,k = 1):
	similarities = []
	for i in range(BoWcorpus.shape[0]):
		similarities.extend([dcos(BoW,BoWcorpus[i,:])])
		dcos(BoW,BoWcorpus[i,:])
	indices = np.argpartition(np.array(similarities),-k)[-k:]	
	return indices[np.argsort(np.array(similarities)[indices])].tolist()


collection_of_documents = ['./nyt-collection-text/art/' + \
							document for document in os.listdir('./nyt-collection-text/art')] + \
							['./nyt-collection-text/music/' + \
							document for document in os.listdir('./nyt-collection-text/music')]

ndocs = 10
BoWcorpus = np.genfromtxt('corpus.csv',delimiter = ',')
random_doc_indices = random.sample(range(BoWcorpus.shape[0]),ndocs)

k = 6
closest_docs = []							
for index in random_doc_indices:
	closest_doc_indices = IrSearch(BoWcorpus[index,:],BoWcorpus,k) 
	closest_doc_indices = [i for i in closest_doc_indices if i != index]
	closest_docs.append([collection_of_documents[i] for i in closest_doc_indices])
	


						
