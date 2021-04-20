# Please be aware that if you decide to use the subreddits below, some posts will be NSFW
# Browse at your own risk. This bot was made for education rather than the content of those subreddits.

import re
import requests
import praw
import pprint
import schedule
import time

# PRAW settings that authenticate our application through Reddit's API
# I am pulling important account information by using my_bot, which is the name of the bot in my praw.ini file
reddit = praw.Reddit("my_bot")

# The setting that determines if your account is authenticated and can post things to subreddits. Other option = True
reddit.read_only = False 

subreddit1 = reddit.subreddit("TIHI")
subreddit2 = reddit.subreddit("awfuleverything")
subreddit3 = reddit.subreddit("atbge")
subreddit4 = reddit.subreddit("all")
subreddit5 = reddit.subreddit("makemesuffer")

# The three lines below will display the information of the subreddit tag above, uncomment to use.
# print(subreddit1.display_name)
# print(subreddit1.title)
# print(subreddit1.description)

# This def is the meat and potatos of this bot, it executes a statement for each subreddit given above
def job():
    for submission in subreddit1.top("hour", limit=1):                                                          # subreddit1 = TIHI (Thanks I Hate It), this gives the top post of the hour
        print(submission.title, "| Has a score of: ", submission.score, "| Link: ", submission.url)             # Prints the output (Title | Has a score of: # | Link: "imageurl") to the terminal
        cross_post = submission.crosspost(subreddit="WtWBBot", title= submission.title, send_replies=True)      # Crossposts the post to the WtWBBot subreddit (reddit.com/r/WtWBBot)
        # pprint.pprint(vars(submission))
    
    for submission in subreddit2.top("hour", limit=1):                                                          # subreddit2 = AwfulEverything
        print(submission.title, "| Has a score of: ", submission.score, "| Link: ", submission.url)             
        cross_post = submission.crosspost(subreddit="WtWBBot", title= submission.title, send_replies=True)      

    for submission in subreddit3.top("hour", limit=1):                                                          # subreddit3 = atbge (Awful taste but good execution)
        print(submission.title, "| Has a score of: ", submission.score, "| Link: ", submission.url)             
        cross_post = submission.crosspost(subreddit="WtWBBot", title= submission.title, send_replies=True)
    
    for submission in subreddit4.top("hour", limit=1):                                                          # subreddit4 = all (Because reddit is a dumpster fire)
        print(submission.title, "| Has a score of: ", submission.score, "| Link: ", submission.url)
        cross_post = submission.crosspost(subreddit="WtWBBot", title= submission.title, send_replies=True)
    
    for submission in subreddit5.top("hour", limit=1):                                                          # subreddit4 = all (Because reddit is a dumpster fire)
        print(submission.title, "| Has a score of: ", submission.score, "| Link: ", submission.url)
        cross_post = submission.crosspost(subreddit="WtWBBot", title= submission.title, send_replies=True)

# job() runs the program before the scheduler below begins, so that you can tell right away that it is functional
job()           

# Runs job() every 1 hours
schedule.every(1).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
