ppdbDict = {}
ppdbSim = 0.9
theta1 = 0.9


import nltk
from nltk.corpus import stopwords

from nltk import SnowballStemmer
stemmer = SnowballStemmer('english')
stemmeres = SnowballStemmer('spanish')

punctuations = ['(','-lrb-','.',',','-','?','!',';','_',':','{','}','[','/',']','...','"','\'',')', '-rrb-']
stopwords = stopwords.words('english')+stopwords.words('spanish')

