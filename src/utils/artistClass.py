class artist:
	#albumArr = []

	def __init__(self, name, followers, popularity, id, albums):
		self.name = name
		self.followers = followers
		self.popularity = popularity
		self.id = id
		self.albumArr = albums

	def getArtistInfo(self):
		print("----------------------------------")
		print("|" + self.name + "|")
		print("----------------------------------")
		print("Followers: ", self.followers)
		print("Popularity: ", self.popularity)
		print("ID: " + self.id)
		print("----------------------------------")
		print("|Albums|")
		print("----------------------------------")
		for al in self.albumArr:
			print("Album: " + al['name'])
			print("Released on: " + al['release_date'])