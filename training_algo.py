from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC,LinearSVC, NuSVC
from sklearn.naive_bayes import MultinomialNB,BernoulliNB, GaussianNB
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import numpy as np
import pickle
from create_train_and_test import create_train_test_data

train_x,train_y ,test_x, test_y = create_train_test_data()
#print(list(train_x))
#clf=SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42)
ch={0:'science', 1:'gaming', 2:'movies', 3:'Music', 4:'worldnews', 5:'books', 6:'television', 7:'gadgets', 8:'sports', 9:'technology', 10:'politics', 11:'space', 12:'painting', 13:'nba', 14:'Jokes', 15:'food', 16:'comics', 17:'Futurology', 18:'history', 19:'europe', 20:'hockey', 21:'marvelstudios', 22:'nintendoswitch', 23:'GlobalOffensive', 24:'dbz', 25:'Android', 26:'anime', 27:'car', 28:'CryptoCurrency', 29:'StarWars', 30:'FIFA', 31:'philosophy', 32:'Art', 33:'Fitness', 34:'gameofthrones', 35:'travel', 36:'Programming', 37:'soccer', 38:'iphone', 39:'PS4', 40:'scifi', 41:'pokemon', 42:'olympics', 43:'harrypotter', 44:'environment', 45:'formula1', 46:'india', 47:'Fantasy', 48:'literature', 49:'pcmasterrace' }
#text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42))])
text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])
text_clf.fit(train_x,train_y)
print("loading")
with open("model_data/trained_classifer.pickle",'wb') as f:
	pickle.dump(text_clf,f)
with open("model_data/trained_classifer.pickle",'rb') as f:
	text_clf=pickle.load(f)
p=text_clf.predict(test_x)
acc=np.mean(p==test_y)

#print(acc)
while 1:
	to=input("Enter text:")
	p=text_clf.predict([to])
	print(ch[int(p[0])])