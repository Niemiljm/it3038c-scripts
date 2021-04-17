--------------------------------
|     Watch the World Burn     |        
--------------------------------

WtWB is a python script that takes 4 subreddits from reddit.com and grabs the top post of the hour.
When let run, it will continuously pull posts and submit them to the WtWB subreddit at reddit.com/r/wtwbbot.
This is my first true experience working with reddit's API and although this is relatively simple, it took me a while to figure out what I was doing.

--------------------------------
|          Motivation          |        
--------------------------------

I have had minimal experience with API's and creating bots, however after I completed the API lab I wanted to learn some more. On top of this, I used to browse reddit daily and
came across some grotesque things that I wanted to share! I can always count on people to continuously post horrible things. Now I have a place I can view them without having to dive into
the cesspool that is Reddit.com.

--------------------------------
|         Installation         |        
--------------------------------
Things you'll need:
1. An API account with Reddit which can be acquired by going to: https://www.reddit.com/wiki/api
    a. An API account with Reddit is a necessary part of this project because otherwise we would not be able to pull information from their servers.
    b. By going to their page: https://www.reddit.com/wiki/api and selecting the *read the terms and register* page, you will be able to fill out thier form and gain access
        to the API wiki and its tools.
    c. The next step to getting an API account setup properly is by browsing to: https://ssl.reddit.com/prefs/apps/ while logged into your account, 
        and selecting the *create app* button towards the bottom of the page. Add a name, select script, add a description and set the redirect URL to: http://localhost:8080
        Lastly, submit that form.
    d. Take note of the client ID and Secret code that is within your application banner:(https://github.com/Niemiljm/it3038c-scripts/blob/main/Project3/Images/ApplicationCodes.png)
2. Reddit Account that is able to create it's own subreddit, an account can be created here: https://www.reddit.com/register/
3. Base knowledge of how Reddit as a whole functions. (Subreddits, commenting, karma, etc.)
4. An IDE (I used Visual Studio Code)
5. Assorted Python Libraries
    requests        pip install requests
    praw            pip install praw
    pprint          pip install pprint
    schedule        pip install schedule
    time            installed with Python
    re              installed with Python
6. Python 3.6+
7. PRAW: The Python Reddit API Wrapper

-------------------------------------------------------------------------------------------------------

Time to actually get some work done.
1. Open up your IDE and change directory to your working directory for the project.
2. In the working directory terminal, execute these commands separately and without quotations.
    "pip install praw"
    "pip install requests"
    "pip install pprint"
    "pip install schedule"
3. Within the wtwbbot.py file, change the following:
    user_agent="Your Name Here",
    client_id="Your ClientID Here",
    client_secret="Your Secret Code Here",
    username="USERNAME",
    password="PASSWORD"
4. You can also change the subreddits that are queried by changing:
        subreddit1 = reddit.subreddit("SUBREDDIT NAME WITHOUT /r/")
5. Lastly, to submit posts to your own subreddit, change the subreddit tag to the name of your subreddit.
        cross_post = submission.crosspost(subreddit="YOURSUBREDDIT", title= submission.title, send_replies=True)

If all is well and configured properly, you should be able to run the code. 

*NOTE* If you would like to test this environment without posting the links, the function below can be set to TRUE:
        reddit.read_only = False

--------------------------------
|        API References        |        
--------------------------------

Reddit is allowing developers to use their API, so please be kind and review the rules and follow them closely. Not doing so could get your account/project terminated.
https://github.com/reddit-archive/reddit/wiki/API

The build-in API list can be found here: https://www.reddit.com/dev/api
Posting all of the methods here would take up too much space!




    




