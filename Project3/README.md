--------------------------------
|     Watch the World Burn     |        
--------------------------------

WtWB is a python script that takes four subreddits from reddit.com and grabs the top posts of the hour.
When ran, it will continuously pull posts and submit them to the WtWB subreddit at reddit.com/r/wtwbbot.
This is my first true experience working with reddit's API and although this is relatively simple, it took me a while to figure out what I was doing.

*Update* I added a secondary feature to this reddit bot. I created a function that searches through the comments posted on my subreddit, and have it reply a set phrase if it meets certain requirements.

```python
def comment_bot(reddit, comments_replied_to):
    print("--------------------")
    print("|Searching Comments|") 
    print("--------------------")

    for comment in reddit.subreddit('WtWBBot').comments(limit=75):                                                  # Searches my sub with a limit of 75 comments
        if "I" in comment.body and comment.id not in comments_replied_to and comment.author != reddit.user.me():    # My restrictions to the search
            print("I found \"user comment\" in your subreddit! From user: " + comment.id)                           # Terminal print with comment.id
            comment.reply("You're doing a good job! Keep it up.")                                                   # Reply
            print("Hey boss, I replied to the comment from " + comment.id + "| They said: " + comment.body)                                          # Exit terminal reply

            # There is a file in this dir that gets printed to. Comments_replied_to.txt
            comments_replied_to.append(comment.id)                                                                 

            # This writes to the file
            with open ("comments_replied_to.txt", "a") as f:                                                        
                f.write(comment.id + "\n" + comment.body)
```
--------------------------------
|          Motivation          |        
--------------------------------

I have had minimal experience with API's and creating bots, however after I completed the API lab I wanted to learn some more. 
On top of this, I used to browse reddit daily and came across some grotesque things that I wanted to share! 
I can always count on people to continuously post horrible things. Now I have a place I can view them without having to dive into the cesspool that is reddit.com.

--------------------------------
|         Installation         |        
--------------------------------

Things you'll need:
1. An API account with Reddit which can be acquired by going to: https://www.reddit.com/wiki/api
    * An API account with Reddit is a necessary part of this project because otherwise we would not be able to pull information from their servers.
    * By going to their page: https://www.reddit.com/wiki/api and selecting the *read the terms and register* page, you will be able to fill out their form and gain access
        to the API wiki and its tools.
    * The next step to getting an API account set up properly is by browsing to: https://ssl.reddit.com/prefs/apps/ while logged into your account, 
        and selecting the *create app* button towards the bottom of the page. Add a name, select script, add a description and set the redirect URL to: http://localhost:8080
        Lastly, submit that form.
    * Take note of the client ID and secret code that is within your application banner:![alt text](https://github.com/Niemiljm/it3038c-scripts/blob/main/Project3/Images/ApplicationCodes.png)

2. Reddit account that is able to create it's own subreddit, an account can be created here: https://www.reddit.com/register/
3. Base knowledge of how Reddit as a whole functions. (Subreddits, commenting, karma, etc.)
4. An IDE (I used Visual Studio Code)
5. Assorted Python Libraries
    * requests        pip install requests
    * praw            pip install praw
    * pprint          pip install pprint
    * schedule        pip install schedule
    * time            installed with Python
    * re              installed with Python
6. Python 3.6+
7. PRAW: The Python Reddit API Wrapper

-------------------------------------------------------------------------------------------------------

Time to actually get some work done.
1. Open up your IDE and change directory to your working directory for the project.
2. In the working directory terminal, execute these commands separately and without quotations.
```python
    "pip install praw"
    "pip install requests"
    "pip install pprint"
    "pip install schedule"
```
3. Wherever you installed python, you will need to copy and paste the praw.ini file from there to your wtwbbot working directory.
4. Within the praw.ini file, change the following to match your information:
```python
    user_agent=
    client_id=
    client_secret= 
    password=
    username=
```
5. You can also change the subreddits that are queried by changing:
```python
        subreddit1 = reddit.subreddit("SUBREDDIT NAME WITHOUT /r/")
```
6. Lastly, to submit posts to your own subreddit, change the subreddit tag to the name of your subreddit.
```python
        cross_post = submission.crosspost(subreddit="YOURSUBREDDIT", title= submission.title, send_replies=True)
```

If all is well and configured properly, you should be able to run the code.
An example of the output that you should see is shown here (3 hours of runtime): ![alt text](https://github.com/Niemiljm/it3038c-scripts/blob/main/Project3/Images/Output.png)
Another example from the second type of output from the comment bot is seen here: ![alt text](https://github.com/Niemiljm/it3038c-scripts/blob/main/Project3/Images/commentOutput.png)

To exit the program use (Control + C) in the terminal window.

*NOTE* If you would like to test this environment without posting the links, the function below can be set to TRUE:

```python    
    reddit.read_only = False
```

--------------------------------
|        API References        |        
--------------------------------

Reddit is allowing developers to use their API, so please be kind and review the rules and follow them closely. Not doing so could get your account/project terminated.
https://github.com/reddit-archive/reddit/wiki/API

The built-in API list can be found here: https://www.reddit.com/dev/api
Posting all of the methods here would take up too much space!

--------------------------------
|           Credits            |        
--------------------------------

I would be lying if I said I did this completely on my own and without guidance from other sources.

1. This link taught me how to get started with the application setup: https://www.instructables.com/Reddit-Reply-Bot/

2. This link taught me how to properly write a README: https://meakaakka.medium.com/a-beginners-guide-to-writing-a-kickass-readme-7ac01da88ab3
    Also: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#headers

3. This github project gave some good direction after I had been struggling to get the comment api to work: https://github.com/yashar1/reddit-comment-bot

4. The tutorial in the PRAW documentation helped me get the hang of calling the API and just writing Python in general: https://praw.readthedocs.io/en/latest/tutorials/reply_bot.html






