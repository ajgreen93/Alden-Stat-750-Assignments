import numpy as np
import csv
import scipy.misc
import matplotlib.pyplot as plt
from sklearn import manifold

def d2(BoW1,BoW2):
	return np.sum(np.square(np.array(BoW1)-np.array(BoW2)))
	
def dcos(BoW1,BoW2):
	if (BoW1 == BoW2).all():
		return 1
	else:
		return np.true_divide(np.dot(BoW1,BoW2),np.linalg.norm(BoW1)*np.linalg.norm(BoW2))
	

#~ BoWcorpus = np.genfromtxt('corpus.csv',delimiter = ',')

#~ distanceMatrix2 = np.zeros((BoWcorpus.shape[0],BoWcorpus.shape[0]))
#~ for i in range(distanceMatrix2.shape[0]):
	#~ for j in range(distanceMatrix2.shape[0]):
		#~ distanceMatrix2[i,j] = d2(BoWcorpus[i,:],BoWcorpus[j,:])

#~ distanceMatrixcos = np.zeros((BoWcorpus.shape[0],BoWcorpus.shape[0]))
#~ for i in range(distanceMatrixcos.shape[0]):
	#~ for j in range(distanceMatrixcos.shape[0]):
		#~ distanceMatrixcos[i,j] = dcos(BoWcorpus[i,:],BoWcorpus[j,:])

#~ mds2 = manifold.MDS()
#~ mdscos = manifold.MDS()
#~ positions2 = mds2.fit(distanceMatrix2)
#~ positionscos = mdscos.fit(distanceMatrixcos)

#~ plt.scatter(positions2.embedding_[:,0],positions2.embedding_[:,1])
#~ plt.show()

#~ plt.scatter(positionscos.embedding_[:,0],positionscos.embedding_[:,1])
#~ plt.show()

#~ scipy.misc.imsave('dist_2.png', distanceMatrix2)
#~ scipy.misc.imsave('dist_cos.png', distanceMatrixcos)

#~ with open("d_2.csv", 'wb') as myfile:
	#~ wr = csv.writer(myfile)
	#~ wr.writerows(collection_of_BoWs)
	
#~ with open("distanceMatrixcos.csv", 'wb') as myfile:
	#~ wr = csv.writer(myfile)
	#~ wr.writerows(collection_of_BoWs)



		


	
