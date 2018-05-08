############
####
## For keeping track of all the things I need to do
#
#

from datetime import datetime

todo = ["Running goals",
		"Start brass guides",
		"Facebook family recruiter",
		"Mailchimp jobs", "Listen to dad's records", "Work on fcd",
		"Compile Torch Passing notes", 
		"Add comp2 to soundcloud", "Add bopit breakdown to soundcloud",
		"Make schedule email", "Record show dates in Calendar",
		"Read Hannah's Blog", "Clean contacts",
		"Purchase requests, diag board, poster (Mere, Amber), trucks (Darin)",
		"Groove Facebook ads", "Groove snapchat filter", "Show poster outside of Michi theat",
		"Turn in receipts", "Reply to gus"]


daily_lists = {
	datetime(2018, 4, 30): [0,1,2,3,6],
	datetime(2018, 5, 1): [0, 1, 2, 4, 5, 7, 11, 12],
	datetime(2018, 5, 5): [3, 9, 12, 19, 20],
	datetime(2018, 5, 7): [2, 8, 11, 12, 17, 18]	
}

now = datetime.now()
today = datetime(now.year, now.month, now.day)
today_list = daily_lists[today]

for ind in today_list:
	print(todo[ind])
print