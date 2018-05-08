###########
####
## Logging the movies I've seen and I wanna see
#
#

class Movie:

	title = ""

	def __init__(self, title):
		self.title = title

movie_strings = ["Captain Fantastic", "Swiss Army Man", "Synecdoche, New York", "Inside Llewyn Davis", "Primer", "Jackie Brown", "Death Proof", "Hateful 8", "Groundhog Day", "Blazing Sadles", "Trainspotting", "Dazed and Confused", "Super Troopers", "Get Out", "Cavin in the Woods", "Spirited Away", "Adaptation", "They Live", "Wolf of Wall Street", "John Mullany standup"]
all_movies = []

for movstr in movie_strings:
	all_movies += [Movie(movstr)]

for movie in all_movies:
	print(movie.title)