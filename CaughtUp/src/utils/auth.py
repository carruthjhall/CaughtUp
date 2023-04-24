import requests
import requests
import base64

def authorize():
	client_id = "21061c8a1abd4a97b12967c4035c07af"
	client_secret = "fd9c3250365a4fd48525e97fb5c2eb9a"

	encoded = base64.b64encode((client_id+ ":" + client_secret).encode("ascii")).decode("ascii")
	headers = {
    	 "Content-Type": "application/x-www-form-urlencoded",
    	 "Authorization": "Basic " + encoded
	}
 
	payload = {
     	"grant_type": "client_credentials"
	}
 
	response = requests.post("https://accounts.spotify.com/api/token", data=payload, headers=headers)

	auth = {
		"token" : response.json()["access_token"],
		"type" : response.json()["token_type"]
	}

	if response.status_code != 200:
		print(response)
		quit()
	else:
		print("Access token received.")
		return auth
