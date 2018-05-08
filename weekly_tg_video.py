########
###
## Every Monday, post a video to tasty Groove
#
#

class weekly_vid:

	link = ""
	caption = ""

	def __init__(self, link, caption):

		self.link = link
		self.caption = caption


post1 = weekly_vid("https://www.youtube.com/watch?v=W1ffhLt6FlA", "Happy Monday y'all")
post2 = weekly_vid("https://www.youtube.com/watch?v=WzucpFgi7Xk",
	"Hey guys, check out the Fearless Flyers on Spotify with Cory Wong and others.")
post3 = weekly_vid("https://www.youtube.com/watch?v=InbaU387Wl8", 
	"TGIMAMFAAOIGRSOT\n(thank god it's Monday and my finals are almost over I'm gettin' real sick of this)",)
post4 = weekly_vid("https://www.youtube.com/watch?v=m86ae_e_ptU", "For anyone looking for a little change in perspective")
post5 = weekly_vid("https://www.youtube.com/watch?v=kLRrIf4L80A")

all_posts = [post1, post2, post3]

for post in all_posts:
	print
	print(post.caption)
	print(post.link)


