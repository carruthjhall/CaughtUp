import requests
from sys import exit

def searchArtist(header, artist):
	print("----------------------------------")
	print("Searching for " + artist)
	print("----------------------------------")

	params = {"q" : artist, "type" : ["artist"]}
	
	getResponse = requests.get("https://api.spotify.com/v1/search",params=params, headers=header)

	if getResponse.status_code != 200:
		print(getResponse)
		quit()

	info = getResponse.json()['artists']['items']
	#print(info[0]['id'])
	
	check = input("Is " + info[0]['name'] + ' correct?(y/n): ')
	
	if check == 'n' or check == 'N' :
		print("Artist not found.")
		exit()
        
	return info[0]['id']		
			
			
def getArtist(accessToken, tokenType, artist):
	#print("Access Token: " + accessToken)
	
	info = {
		"artist": "",
		"albums": []
    }

	authHeader = {"Authorization": tokenType + " " + accessToken}

	id=searchArtist(authHeader, artist)
	#print("fs")
	
    

	artist = {"URL": "https://api.spotify.com/v1/artists/" + id}
	
	getResponse = requests.get(artist["URL"], headers=authHeader)
	
	if getResponse.status_code != 200:
		print(getResponse)
		quit()
	
	#print("Artist data received.")	
	info["artist"] = getResponse.json()
	print("Getting " + info["artist"]['name'] + "'s information")
		
	params = {"id" : id, "limit": 3}
	
	url = {
        "URL" : "https://api.spotify.com/v1/artists/" + id + "/albums"
    }
	
	alResponse = requests.get(url["URL"],params=params, headers=authHeader)
	
	if alResponse.status_code != 200:
		print(alResponse)
		quit()
		
	#print("Artist album data received.")
	info['albums'] = alResponse.json()['items']
	
	return info

    

