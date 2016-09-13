#input : document--file of text
#output: words--list of all words in order of appearance
def tokenize(document):
	words = []
	file = open(document,'r')
	lines = file.readlines()
	for line in lines:
		words.extend(line.split())
	return(words)

#input : words--list of words (from document), 
#		 lexicon--list of words (to count)
#output: bagOfWords--list of numbers counting number of each word
#					 in lexicon
def makeBoW(words,lexicon):
	bagOfWords = []
	for word in lexicon:
		bagOfWords.extend([words.count(word)])
	return(bagOfWords)

