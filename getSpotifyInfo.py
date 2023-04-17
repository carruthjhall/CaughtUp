import requests
import base64
import json

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

	#accessToken = response.json()["access_token"]
	#tokenType = response.json()["token_type"]
	#expiry = response.json()["expires_in"]

	#print(json.dumps(accessToken, indent=4))
	#print(tokenType)
	#print(expiry)


def getArtist(accessToken, tokenType):
	#print("Access Token: " + accessToken)

	authHeader = {"Authorization": tokenType + " " + accessToken}
	
	artistURI = "4hz8tIajF2INpgM0qzPJz2"
	
	artist = {"URL": "https://api.spotify.com/v1/artists/" + artistURI}
	
	getResponse = requests.get(artist["URL"], headers=authHeader)
	
	if getResponse.status_code != 200:
		print(getResponse)
		quit()
	else:
		print("Artist data received.\nPrinting: \n")
		return getResponse.json()

client_id = "21061c8a1abd4a97b12967c4035c07af"
client_secret = "fd9c3250365a4fd48525e97fb5c2eb9a"

response = authorize(client_id, client_secret)

artistInfo = getArtist(response.json()["access_token"], response.json()["token_type"])
print(artistInfo)


