# Please be aware that if you decide to use the subreddits below, some posts will be NSFW.
# Browse at your own risk. This bot was made for education rather than the content of those subreddits.
# If you would like to see the bot in action, please browse to https://www.reddit.com/r/WtWBBot/ 
# I will leave the bot running for a while after this assignment is turned in just to show it works!

import re
import requests
import praw
import pprint
import schedule
import time
import os

# PRAW settings that authenticate our application through Reddit's API.
# I am pulling important account information by using my_bot, which is the name of the bot in my praw.ini file.
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

# This def is the meat and potatos of this bot, it executes a statement for each subreddit given above.
def job():
    for submission in subreddit1.top("hour", limit=1):                                                          # subreddit1 = TIHI (Thanks I Hate It), this gives the top post of the hour.
        print(submission.title, "| Has a score of: ", submission.score, "| Link: ", submission.url)             # Prints the output (Title | Has a score of: # | Link: "imageurl") to the terminal.
        cross_post = submission.crosspost(subreddit="WtWBBot", title= submission.title, send_replies=True)      # Crossposts the post to the WtWBBot subreddit (reddit.com/r/WtWBBot).
        # pprint.pprint(vars(submission))
    
    for submission in subreddit2.top("hour", limit=1):                                                          # subreddit2 = AwfulEverything.
        print(submission.title, "| Has a score of: ", submission.score, "| Link: ", submission.url)             
        cross_post = submission.crosspost(subreddit="WtWBBot", title= submission.title, send_replies=True)      

    for submission in subreddit3.top("hour", limit=1):                                                          # subreddit3 = atbge (Awful taste but good execution).
        print(submission.title, "| Has a score of: ", submission.score, "| Link: ", submission.url)             
        cross_post = submission.crosspost(subreddit="WtWBBot", title= submission.title, send_replies=True)
    
    for submission in subreddit4.top("hour", limit=1):                                                          # subreddit4 = all (Because reddit is a dumpster fire)
        print(submission.title, "| Has a score of: ", submission.score, "| Link: ", submission.url)
        cross_post = submission.crosspost(subreddit="WtWBBot", title= submission.title, send_replies=True)
    
    for submission in subreddit5.top("hour", limit=1):                                                          # subreddit4 = makemesuffer
        print(submission.title, "| Has a score of: ", submission.score, "| Link: ", submission.url)
        cross_post = submission.crosspost(subreddit="WtWBBot", title= submission.title, send_replies=True)

# This is a secondary function of this bot. It will find comments in my subreddit with "I" in it, (something broad since there aren't many comments on my sub).
# It searches for those comments, and if the user is not me, and not in my previously replied to list, then it comments something!
def comment_bot(reddit, comments_replied_to):
    print("--------------------")
    print("|Searching Comments|") 
    print("--------------------")

    for comment in reddit.subreddit('WtWBBot').comments(limit=75):                                                  # Searches my sub with a limit of 75 comments.
        if "I" in comment.body and comment.id not in comments_replied_to and comment.author != reddit.user.me():    # My restrictions to the search.
            print("I found \"user comment\" in your subreddit! From user: " + comment.id)                           # Terminal print with comment.id
            comment.reply("You're doing a good job! Keep it up.")                                                   # Reply
            print("Hey boss, I replied to the comment from " + comment.id + "| They said: " + comment.body)         # Exit terminal reply

            # There is a file in this dir that gets printed to. Comments_replied_to.txt
            comments_replied_to.append(comment.id)                                                                 

            # This writes to the file.
            with open ("comments_replied_to.txt", "a") as f:                                                        
                f.write(comment.id + "\n" + comment.body)
    
    print("I'm done for now, nothing else was found...")
    print("-------------------------------------------")
    time.sleep(600)

# This def is what the above looks at to ensure it is written to that file, and that the comment.id is not already in there.
def save_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
    
    return comments_replied_to

# job() runs the program before the scheduler below begins, so that you can tell right away that it is functional.
job()           
comments_replied_to = save_saved_comments()

# Runs job() every 1 hours.
schedule.every(1).hours.do(job)

while True:
    comment_bot(reddit, comments_replied_to)
    time.sleep(1)

while True:
    schedule.run_pending()
    time.sleep(1)
