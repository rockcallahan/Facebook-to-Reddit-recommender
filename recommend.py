from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
#from sklearn.linear_model import SGDClassifier
#from sklearn.svm import SVC,LinearSVC, NuSVC
from collections import Counter
from sklearn.naive_bayes import MultinomialNB,BernoulliNB, GaussianNB
#from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import numpy as np
import pickle
from get_likes import likes
from timeit import default_timer as timer
text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])
ch={0:'science', 1:'gaming', 2:'movies', 3:'Music', 4:'worldnews', 5:'books', 6:'television', 7:'gadgets', 8:'sports', 9:'technology', 10:'politics', 11:'space', 12:'painting', 13:'nba', 14:'Jokes', 15:'food', 16:'comics', 17:'Futurology', 18:'history', 19:'europe', 20:'hockey', 21:'marvelstudios', 22:'nintendoswitch', 23:'GlobalOffensive', 24:'dbz', 25:'Android', 26:'anime', 27:'car', 28:'CryptoCurrency', 29:'StarWars', 30:'FIFA', 31:'philosophy', 32:'Art', 33:'Fitness', 34:'gameofthrones', 35:'travel', 36:'Programming', 37:'soccer', 38:'iphone', 39:'PS4', 40:'scifi', 41:'pokemon', 42:'olympics', 43:'harrypotter', 44:'environment', 45:'formula1', 46:'india', 47:'Fantasy', 48:'literature', 49:'pcmasterrace' }
with open("model_data/trained_classifer.pickle",'rb') as f:
		text_clf=pickle.load(f)
print("model loaded")		
def reco(id):
	print("now in recommend")
	start=timer()
	user_data=likes(id)
	if user_data=="*2*2":
		return user_data,0,0,0,0
	end=timer()
	l_time=end-start
	#print("number of likes:",len(user_data))
	if len(user_data) is 0:
	    return(["Sorry, we can not access your likes :(<br> Either you have insufficient likes or did not give the permission to access your likes. please like at least one subject on facebook or log out and give us permission :)."])
	#print(list(train_x))
	#clf=SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42)
	#text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42))])
	#text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])
	#text_clf.fit(train_x,train_y)
	#p=text_clf.predict(test_x)
	#acc=np.mean(p==test_y)
	
	#print(acc)
	start=timer()
	q=text_clf.predict(user_data)
	q=p=[ch[i] for i in q]
	p=Counter(q)
	tyy=dict(p)
	p=p.most_common(6)
	p=[item[0] for item in p]
	t=[]
	for i in range(len(q)):
		dd=user_data[i]+" --> "+q[i]
		t.append(dd)
	end=timer()
	r_time=end-start	
	#print(l_time)
	#print(r_time)
	return p,t,l_time,r_time,tyy
'''
id='EAACEdEose0cBAHyZCKrrjYhzUlZA7SpRrH4zpJposJNYY9pZCNM9rjCCz9fKZCH5vXGIp5i0SUROPHdsBk1JhymhQyafQIcoKWFZBk0A5v6nZAaIqXQT9ULvMEARlCRYsjZCNqIMP7gvz0YWF8SxjvEjAJJc4c7xyWU1A1RrNkZBAIR6wQO0USFcUXFwlWSXccNKtgHwfhi6gwZDZD'
p,t,r,z,gr=reco(id)
print (p)
print(gr)
'''