import src.utils.auth as at
import src.utils.search as sr
import src.utils.artistClass as ac

#TO-DO: Make keys private, make visual representation
auth = at.authorize()

userSearch = input("Enter artist name:")
info = sr.getArtist(auth["token"],auth["type"],userSearch)
#print(info)

artist1 = ac.artist(info['artist']["name"], info['artist']["followers"]["total"], info['artist']["popularity"], info['artist']["id"], info['albums'])

artist1.getArtistInfo()