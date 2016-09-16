#input : document--file of text
#output: words--list of all words in order of appearance
def tokenize(document):
	words = []
	file = open(document,'r')
	lines = file.readlines()
	for line in lines:
		words.extend(line.split())
	return(words)
