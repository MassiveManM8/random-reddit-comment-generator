print("running")

from flask import Blueprint, render_template
import praw
import os
from datetime import datetime


views = Blueprint(__name__, "views")

reddit = praw.Reddit(
    client_id = "212NMcQ3ncmh8GZdBdc2WQ",
    client_secret = "w7DEh2I57ZDXnlFhnSTgDQHiA0JO8w",
    username = "is-this-person-funny",
    password = "markiplier_fan13",
    user_agent = "<ReplyCommentBot1.0>"
)

subreddit = reddit.subreddit("all")

comments = ""
auth = ""
score = ""
time = ""
link = ""

for comment in subreddit.comments():
    comments = comment.body
    auth = comment.author
    score = comment.score
    time = comment.created_utc
    link = "https://www.reddit.com" + comment.permalink

rand_com = comments
rand_com_auth = auth
rand_com_score = score
ts = int(time)
rand_com_time = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
rand_com_link = link


#here is where the code is supposed to be so that the template gets expanded with the text but i ran out of time
#... just pretend you didn't notice

@views.route("/")
def home():
    return render_template("index.html", comment=rand_com, auth=rand_com_auth, score=rand_com_score, time=rand_com_time, link=rand_com_link)