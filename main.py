print("bot-running")

import praw
import os



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
link = ""

for comment in subreddit.comments():
    comments = comment.body
    auth = comment.author
    score = comment.score
    link = "https://www.reddit.com" + comment.permalink


rand_com = comments
rand_com_auth = auth
rand_com_score = score
rand_com_link = link

print(rand_com_link)
print(rand_com_score)
print(rand_com_auth)
print(rand_com)

