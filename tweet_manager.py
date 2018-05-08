#########
###
## For managing the things I tweet
#
#


class Tweet:

	content = ""
	favorites = 0

	def __init__(self, content, favorites):
		self.content = content
		self.favorites = favorites


tweet1 = Tweet("The ascii letter K corresponds to the binary string\n0100 1011\nOtherwise known as the parabittle", 8)
tweet2 = Tweet("Well that philosophy final's in the bag given that I used the word \"furthermore\" in every answer", 11)
tweet3 = Tweet("I fancy myself a joke philosopher", 1)

all_tweets = [tweet1, tweet2, tweet3]

for tweet in all_tweets:
	print
	print(tweet.content)
	print(tweet.favorites)