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
2. Reddit Account that is able to create it's own subreddit
3. Base knowledge of how Reddit as a whole functions. (Subreddits, commenting, karma, etc.)
4. An IDE (I used Visual Studio Code)
5. PRAW
6. Python 3.6+
7. Assorted Python Libraries
    requests        pip install requests
    praw            pip install praw
    pprint          pip install pprint
    schedule        pip install schedule
    time            installed with Python
    re              installed with Python

1. An API account with Reddit is a necessary part of this project because otherwise we would not be able to pull information from their servers.
    a. By going to their page: https://www.reddit.com/wiki/api and selecting the *read the terms and register* page, you will be able to fill out thier form and gain access
        to the API wiki and its tools.
    b. The next step to getting an API account setup properly is by browsing to: https://ssl.reddit.com/prefs/apps/ while logged into your account, 
        and selecting the *create app* button towards the bottom of the page. Add a name, select script, add a description and set the redirect URL to: http://localhost:8080
        Lastly, submit that form.
    c. Take note of the client ID and Secret code that is within your application banner: ![ClientID and Secret](https://github.com/Niemiljm/it3038c-scripts/blob/main/Project3/Images/ApplicationCodes.png "ClientID and Secret")

PRAW: The Python Reddit API Wrapper

    Praw is the backbone of many bots created for Reddit. It is relatively easy to pick up, and the documentation is incredible.
    After following the tutorials that are available on their website, I was able to write this bot to compile posts from multiple subreddits.

    Here is the documentation website for PRAW: https://praw.readthedocs.io/en/stable/index.html


    Dependancies:
    - Python 3.6+ is required
        https://www.python.org/downloads/
    - pip (which is already included in python 2 >=2.7.9 or python 3 >=3.4)

    




