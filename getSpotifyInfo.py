import requests
import base64
import json
from sys import exit

client_id = "21061c8a1abd4a97b12967c4035c07af"
client_secret = "fd9c3250365a4fd48525e97fb5c2eb9a"


def authorize(cli_ID, cli_s):
	encoded = base64.b64encode((cli_ID+ ":" + cli_s).encode("ascii")).decode("ascii")
	headers = {
    	 "Content-Type": "application/x-www-form-urlencoded",
    	 "Authorization": "Basic " + encoded
	}
 
	payload = {
     	"grant_type": "client_credentials"
	}
 
	response = requests.post("https://accounts.spotify.com/api/token", data=payload, headers=headers)

	if response.status_code != 200:
		print(response)
		quit()
	else:
		print("Access token received.")
		return response

def getArtist(accessToken, tokenType, artistURI, artist):
	#print("Access Token: " + accessToken)
	print("Getting " + artist + "'s information")

	authHeader = {"Authorization": tokenType + " " + accessToken}
	
	artist = {"URL": "https://api.spotify.com/v1/artists/" + artistURI}
	
	getResponse = requests.get(artist["URL"], headers=authHeader)
	
	if getResponse.status_code != 200:
		print(getResponse)
		quit()
	else:
		print("Artist data received.")
		return getResponse.json()

def searchArtist(accessToken, tokenType, artist):
	print("----------------------------------")
	print("Searching for " + artist)

	authHeader = {"Authorization": tokenType + " " + accessToken}
	params = {"q" : artist, "type" : ["artist"]}
	
	getResponse = requests.get("https://api.spotify.com/v1/search",params=params, headers=authHeader)

	if getResponse.status_code != 200:
		print(getResponse)
		quit()

	info = getResponse.json()['artists']['items']
	
	if info[0]['name'].lower() != artist:
		print(info[0]['name'] + " does not match " + artist)
		exit()
	
	print("Artist " + info[0]['name'] + " found.")
	return info[0]['id']	

class artist:
	def __init__(self, name, followers, popularity, uri):
		self.name = name
		self.followers = followers
		self.popularity = popularity
		self.uri = uri

	def getArtistInfo(self):
		print("----------------------------------")
		print("|Artist: " + self.name + "|")
		print("----------------------------------")
		print("Followers: ", self.followers)
		print("Popularity: ", self.popularity)
		print("URI: " + self.uri)

response = authorize(client_id, client_secret)

userSearch = input("Enter artist name:")

info = getArtist(response.json()["access_token"], response.json()["token_type"], searchArtist(response.json()["access_token"], response.json()["token_type"], userSearch), userSearch)

artist1 = artist(info["name"], info["followers"]["total"], info["popularity"], info["uri"])

artist1.getArtistInfo()