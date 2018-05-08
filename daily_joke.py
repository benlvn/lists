###############
####
## For tracking my daily jokes
#
#


from datetime import datetime
from dateutil import parser
import csv

class Joke:

	def __init__(self, content, date):
		self.content = content
		self.date = date


all_jokes = [Joke("Ya know I just found out that I snore so loudly, it scares everyone in the car I'm driving", datetime(2018, 4, 9)),
Joke("Hey why don't you ever see elephants hiding in trees?\nIt's because they're really good at it", datetime(2018, 4, 10)),
Joke("So this guy walks into a library is asks the librarian \"I'd like the fish and chips.\"\nShe says \"Sir, this is a library.\"\nSo he whispers \"I'd like the fish and chips\"", datetime(2018, 4, 11)),
Joke("It's hard to explain puns to kleptomaniacs because they're always taking things literally", datetime(2018, 4, 12)),
Joke("Hey what's blue and smells like red paint?\nBlue paint", datetime(2018, 4, 13)),
Joke("So I was standing there in the park, wondering why that frisbee looked like it was getting bigger, and then it hit me!", datetime(2018, 4, 14)),
Joke("Hey ya know people say that smoking causes diseases\nBut it actually cures salmon", datetime(2018, 4, 15)),
Joke("Yo so the world tongue twister champion got arrested yesterday.  I hear they're gonna give him a really tough sentence", datetime(2018, 4, 16)),
Joke("A Ham Sandwich walks into a bar. The bartender says \"I'm sorry, We don't serve food here\".", datetime(2018, 4, 17)),
Joke("I find a duck's opinion of me is very much influenced over whether or not I have bread", datetime(2018, 4, 18)),
Joke("And god said unto John \"Come forth, and ye shall receive eternal life\"\nBut John came in fifth, and only won a toaster", datetime(2018, 4, 19)),
Joke("Some people are afraid of heights.  Not me, I'm afraid of widths", datetime(2018, 4, 20)),
Joke("You know how birds fly in a V all the time?\nYou ever wonder why one side is always shorter than the other?\nIt's cause there are fewer birds in it", datetime(2018, 4, 21)),
Joke("Ya know there's JVC, Panasonic, Toshiba.\nMan, what's with all these stereotypes?", datetime(2018, 4, 22)),
Joke("What do you call a cow without legs?\nGround beef", datetime(2018, 4, 24)),
Joke("Saying \"I'm sorry\" means the same thing as \"I apologize\"\nExcept at a funeral", datetime(2018, 4, 25)),
Joke("Hey yo once I saw a sign that said \"Watch for children\" and I thought that sounded like a fair trade", datetime(2018, 4, 27)),
Joke("Ya know I own the absolute worst thesaurus.  Not only is it terrible, but it's terrible", datetime(2018, 4, 29)),
Joke("What would you do if you cracked an egg for breakfast and a mouse came out and then time froze and God came down and said to forget what you saw or else?\nI'd tell everyone, but I'd make it seem like a joke", datetime(2018, 4, 30)),
Joke("Can a kangaroo jump higher than a house?\nOf course not, a house can't jump at all", datetime(2018, 5, 1)),
Joke("Why couldn't the bicycle stand up on its own?\nBecause it was two-tired", datetime(2018, 5, 2)),
Joke("I wouldn't buy anything with velcro. It's a total rip-off", datetime(2018, 5, 3)),
Joke("Yesterday a clown held the door open for me.  It was such a nice Jester!", datetime(2018, 5, 4)),
Joke("Have you heard the one about the bad pole-vaulter? It never goes over very well", datetime(2018, 5, 4)),
Joke("What country's capital has the fastest growing population?\nIreland, every day it's Dublin", datetime(2018, 5, 6)),
Joke("How many cats can you put in an empty box?\nJust one.  After that the box isn't empty anymore!", datetime(2018, 5, 7))
]

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = ["January", "Febuary", "March", "April", "May"]
"""print
print
for joke in all_jokes:
	timestamp = weekdays[joke.date.weekday()] + ", " + months[joke.date.month-1] + " " + str(joke.date.day)
	print
	print(timestamp)
	print(joke.content)

print
print"""



with open("jokes.csv", 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter='\t')
	for joke in all_jokes:
		spamwriter.writerow([joke.content, joke.date])
"""
read_jokes = []
with open("jokes.csv", 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='\t')
	for row in spamreader:
		date = parser.parse(row[1])
		new_joke = Joke(row[0],date)
		read_jokes += [new_joke]


print
print
for joke in read_jokes:
	timestamp = weekdays[joke.date.weekday()] + ", " + months[joke.date.month-1] + " " + str(joke.date.day)
	print
	print(timestamp)
	print(joke.content)

print
print
	
"""


