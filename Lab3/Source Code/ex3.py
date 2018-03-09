import nltk
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr=WordNetLemmatizer()


file_1=open("file_to_read",'r')
for i in file_1:
    print(lmtzr(i))


