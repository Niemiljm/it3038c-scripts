import praw
user_agent = ("Python,Get Most Downvoted Comment 0.1")
r = praw.Reddit('By /u/HappyZombies v 1.0. ')
subreddit = r.get_subreddit("stayawaysub")
for comment in subreddit.get_comments(limit = 2):
	if(comment.ups <= -100):
		print ("Text: ' "+str(comment.body)+"'\nUpvotes: "+str(comment.ups)+"\nAuthor: "+str(comment.author))