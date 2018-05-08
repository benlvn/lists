"""
    ____        _ __             __      __            
   / __ \____ _(_) /_  __       / /___  / /_____  _____
  / / / / __ `/ / / / / /  __  / / __ \/ //_/ _ \/ ___/
 / /_/ / /_/ / / / /_/ /  / /_/ / /_/ / ,< /  __(__  ) 
/_____/\__,_/_/_/\__, /   \____/\____/_/|_|\___/____/  
                /____/                                 

"""

from datetime import datetime
from dateutil import parser
import csv

class Joke:

	def __init__(self, content, date):
		self.content = content
		self.date = date

all_jokes = []
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
abr_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]



## TODO: Create Joke
	# Select date
		# Presents 5 choices at a time
		# First choice is today's date, then the next four available dates
		# All dates shown chronologically, with prev and next options
		# If current date not available, start list at first available
		# Mark today
	# Enter Joke
		# Newlines via returns are valid
		# End joke with \d
		# (For done)

## TODO: Read jokes
	# Selecting jokes
		# Dates will be presented as weeks (Week of date)
		# Date ranges will be presented
		# The modulo five will be the earliest dates
		# 10 options will be presented at a time with prev/next options
	# Printing jokes
		# Print some word art
		# Print List of {date}\n{joke}\n\n
		# Then a pre/next option
"""
with open("jokes.csv", 'rb') as data_file:
	joke_reader = csv.reader(data_file, delimiter='\t')
	for row in joke_reader:
		new_joke = Joke(row[0], parser.parse(row[1]))
		all_jokes += [new_joke]

while True:
	week_start_indices = []
	selection = 1
	for i in reversed(range(len(all_jokes))):
		joke = all_jokes[i]
		j = i
		if(i < len(all_jokes) - 1): j += 1
		if(i == 0 or all_jokes[j].date.weekday() < joke.date.weekday()):
			print(str(selection) + ". Week of " + str(abr_months[joke.date.month - 1]) + 
				" " + str(joke.date.day) + ", " + str(joke.date.year))
			selection += 1
			week_start_indices += [i]

	selection = raw_input("> ")
	if(selection == 'q'): break
	start_index = week_start_indices[int(selection) - 1]

	for i in range(7):
		index = i + start_index
		if(index >= len(all_jokes)): break
		joke = all_jokes[index]
		timestamp = weekdays[joke.date.weekday()] + ", " + months[joke.date.month-1] + " " + str(joke.date.day)
		print
		print(timestamp)
		print(joke.content)

with open("jokes.csv", 'wb') as data_file:
	joke_writer = csv.writer(data_file, delimiter='\t')
	for joke in all_jokes:
		joke_writer.writerow([joke.content, joke.date])
"""

"""
Menu spec
Menu's should display in this format:
 ____________
|Menu
|1. Week of Apr 29, 2018
|2. Week of Apr 22, 2018
|3. Week of Apr 15, 2018
|4. Week of Apr 9, 2018
|> ffffffffffffffffffffffffff
"""





"""
while unlisted_dates >= 5:
	date2 = all_jokes[unlisted_dates-1].date
	date1 = all_jokes[unlisted_dates-5].date
	display_dates += [[date1, date2]]
	unlisted_dates -= 5
"""

"""
for i in range(len(display_dates)):
	pair = display_dates[i]
	date1 = pair[0]
	date2 = pair[1]
	print(str(i+1) + ": " + date1.strftime("%m/%d/%Y") + " - " + date2.strftime("%m/%d/%Y"))	
"""

	


