import os
import csv
from hwk3 import makeBoW
from hwk2 import tokenize

def analyzeCorpus(collection_of_documents):
	collection_of_BoWs = []
	lexicon = []
	for document in collection_of_documents:
		tokens = tokenize(document)
		lexicon = list(set(lexicon) | set(tokens))
	for document in collection_of_documents:
		tokens = tokenize(document)
		BoW = makeBoW(tokens,lexicon)
		collection_of_BoWs.append(BoW)
	return(collection_of_BoWs)
	
collection_of_documents = ['./nyt-collection-text/art/' + \
							document for document in os.listdir('./nyt-collection-text/art')] + \
							['./nyt-collection-text/music/' + \
							document for document in os.listdir('./nyt-collection-text/music')]
collection_of_BoWs = analyzeCorpus(collection_of_documents)

with open("corpus.csv", 'wb') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerows(collection_of_BoWs)


