from datetime import datetime
from dateutil import parser
import csv


class Joke:

	def __init__(self, content, date):
		self.content = content
		self.date = date

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = ["January", "Febuary", "March", "April", "May"]


read_jokes = []
with open("jokes.csv", 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='\t')
	for row in spamreader:
		date = parser.parse(row[1])
		new_joke = Joke(row[0],date)
		read_jokes += [new_joke]


print
for joke in read_jokes:
	timestamp = weekdays[joke.date.weekday()] + ", " + months[joke.date.month-1] + " " + str(joke.date.day)
	print
	print(timestamp)
	print(joke.content)

print