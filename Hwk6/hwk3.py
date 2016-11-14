#input : words--list of words (from document), 
#		 lexicon--list of words (to count)
#output: bagOfWords--list of numbers counting number of each word
#					 in lexicon
def makeBoW(words,lexicon):
	bagOfWords = []
	for word in lexicon:
		bagOfWords.extend([words.count(word)])
	return(bagOfWords)
	
