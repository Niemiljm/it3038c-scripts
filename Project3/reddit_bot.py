#!/usr/bin/python
import re
import time
import praw
import sqlite3


#Enter your correct Reddit information into the variable below
# userAgent = 'WtWBBot'
# cID = 'Lrxjx1E-T0a_EA'
# cSC = '00mEZRkFK_i7XnwMe0WLwelUSx_9Sw'
# userN = 'WtWBBot'
# userP ='This1Reddit'
# numFound = 0
# reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

SOURCE_SUB = 'TIHI'
POST_SUB = 'WtWBBot'

KEYWORDS = []

# This section is intended to send a message stating that a post has been crossposted to my subreddit, and also
# to give credit where it is due "author"
def send_message(r, author):
    subject = 'Hello! Your post has been crossposted to /r/{}'.format(POST_SUB)
    msg = 'Your post has been crossposted. Thank you for the content, I appreciate it!'
    r.send_message(author, subject, msg)

    print('I sent a message to ' + author)

# This is where the posts are actually submitted, and a notification is sent to the OP to give credit, and show them
# where their post is going.
def xpost_subm(r, subm, sql, c):
    title = '[/u/{}] {}'.format(subm.author, subm.title)

    print('Just wanted you to know that I am submitting that post now.')
    r.submit(POST_SUB, title, url=subm.permalink)
    send_message(r, subm.author)
    
    #This adds our submission to the db
    c.execute('Insert posted values', [subm.id])
    sql.commit()

def find_posts(r, sql, c):
    print('Searching for posts...')
    # pattern to match keywords in the title
    pattern = re.compile(r'\b({})\b'.format(r'|'.join(KEYWORDS)), re.IGNORECASE)

    subm_stream = reddit.subreddit(r, SOURCE_SUB).stream.submissions()
    for subm in subm_stream:  # check submissions
        c.execute('SELECT * FROM posted WHERE subm_id = ?', [subm.id])
        if c.fetchone():  # skip the submission if it's already been posted
            continue

        # then search for keywords
        if pattern.search(subm.title):
            xpost_subm(r, subm, sql, c)


def main():
    r = praw.Reddit("DEFAULT", user_agent="default user agent")
    # o = OAuth2Util.OAuth2Util(r, print_log=True)

    print('I am currently loading stuff from DB, please wait...')
    sql = sqlite3.connect('WtWBBot.db')
    c = sql.cursor()


    c.execute('Create table if not exists posted(subm_id TEXT)')
    sql.commit()

    print('I am done loading the DB.')

    while True:
        try:
            find_posts(r, sql, c)
        except Exception as e:
            print('There has been an error: {}'.format(e))

        print('I go to sleep now ZZzzZZzzz')
        time.sleep(500)

if __name__ == '__main__':
    main()