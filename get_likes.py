import facepy
import requests
def likes(id):
    print("now in get_likes")
    graph = facepy.GraphAPI(id)
    try:
        likes = graph.get('me/likes')
    except facepy.exceptions.OAuthError:
        return "*2*2"
    alike = []
    while(True):
	    try:
	        for l in likes['data']:
	            alike.append(l['name'])
	        likes=requests.get(likes['paging']['next']).json()
	    except KeyError:
	        break
    #print(name)
    print(alike)
    return alike


