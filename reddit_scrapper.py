# -*- coding: utf-8 -*-
import requests
import re
import time
subs=['science','gaming','movies','Music','worldnews','books','television','gadgets','sports','technology','politics','space','painting','nba','Jokes','food','comics','cricket','history','europe','hockey','marvelstudios','nintendoswitch','GlobalOffensive','dbz','Android','anime','cars','CryptoCurrency','StarWars','FIFA','philosophy','Art','Fitness','gameofthrones','travel','Programming','soccer','iphone','PS4','scifi','pokemon','olympics','harrypotter','environment','formula1','india','Fantasy','literature','pcmasterrace']
def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
n=10000
for s in subs:
	i=0
	utc=int(time.time())
	print("now gathering Submission data from ",s,"::::::::::::::\n\n\n\n\n")
	f=open("data/"+s+".txt",'w',encoding="utf-8")
	while i<n:
		url='https://api.pushshift.io/reddit/submission/search/?sort=desc&filter=title,created_utc&size=1001'
		r=requests.get(url+"&before="+ str(utc)+"&subreddit="+s)
		data=r.json()
		data=data['data']
		if len(data)==0:
			break;
		utc=data[-1]['created_utc']
		#utc=utc[-1]
		data=[j['title']for j in data]
		for d in data:
			d=re.sub("[\[].*?[\]]",'',d) 
			if(isEnglish(d)):
				f.write(d+"\n******\n")
				print(d)
				i+=1
				print(i)