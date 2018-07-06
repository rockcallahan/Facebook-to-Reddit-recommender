import numpy as np
import random
from collections import Counter
from sklearn.externals import joblib
import pickle as pickle
import numpy as np
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
ch={'science':0, 'gaming':1, 'movies':2, 'Music':3, 'worldnews':4, 'books':5, 'television':6, 'gadgets':7, 'sports':8, 'technology':9, 'politics':10, 'space':11, 'painting':12, 'nba':13, 'Jokes':14, 'food':15, 'comics':16, 'Futurology':17, 'history':18, 'europe':19, 'hockey':20, 'marvelstudios':21, 'nintendoswitch':22, 'GlobalOffensive':23, 'dbz':24, 'Android':25,'anime':26, 'cars':27, 'CryptoCurrency':28, 'StarWars':29, 'FIFA':30, 'philosophy':31, 'Art':32, 'Fitness':33, 'gameofthrones':34, 'travel':35, 'Programming':36, 'soccer':37, 'iphone':38,'PS4':39,'scifi':40, 'pokemon':41, 'olympics':42, 'harrypotter':43, 'environment':44, 'formula1':45, 'india':46, 'Fantasy':47, 'literature':48, 'pcmasterrace':49}
subs=['science','gaming','movies','Music','worldnews','books','television','gadgets','sports','technology','politics','space','painting','nba','Jokes','food','comics','Futurology','history','europe','hockey','marvelstudios','nintendoswitch','GlobalOffensive','dbz','Android','anime','cars','CryptoCurrency','StarWars','FIFA','philosophy','Art','Fitness','gameofthrones','travel','Programming','soccer','iphone','PS4','scifi','pokemon','olympics','harrypotter','environment','formula1','india','Fantasy','literature','pcmasterrace']
subs_cmts=[i+"_comments" for i in subs]
subs_cmts=subs+subs_cmts
def create_data():
	data=[]
	##u=int(input("\nMunging data\n\n1.from Head1ines.\n2.From comments\n"))
	u=1;
	sud=[]
	if u is 1:
		sud=subs
	elif u is 2:
		sud=subs_cmts
	for s in sud:
		#print("*****************\ncurrently encoding subreddit",s,"\n***************************")
		try:
			f=open("data/"+s+".txt",'r',encoding="utf-8")
		except:
			break
		te=f.read().split("\n******\n")
		for t in te:
			#print("currently reading sentence :",t,"sub code:",ch[s],"\n\n")
			data.append([[t],[ch[s]]])
	return data

def create_train_test_data(split=0.1):
	#print("creating Data\n")
	data=create_data()
	random.shuffle(data)
	#print("data Created \n")
	#print(data)
	#data=data[:850000]
	#data=np.array(data)
	#print((data))
	k=len(data)
	n=int((len(data)*(1-split)))
	train_data=data[:n]
	data=data[n:]
	print("total number of data rows",k)
	train_x=[item[0] for item in train_data]
	train_y=[item[1] for item in train_data]
	test_x=[item[0] for item in data]
	test_y=[item[1] for item in data]
	#test_y=test_y.tolist()
	train_x=[item for su in train_x for item in su]
	train_y=[item for su in train_y for item in su]
	test_x=[item for su in test_x for item in su]
	test_y=[item for su in test_y for item in su]
	print("training feature created with length:",len(train_x))
	print("training label created with length:",len(train_y))
	print("testing feature created with length:",len(test_x))
	print("testing label created with length:",len(test_y))
	return train_x,train_y ,test_x, test_y