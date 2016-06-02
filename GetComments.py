'''
This code grabs the comments from the reddit comment stream using praw.
'''


import praw
from praw.helpers import comment_stream

def getComments():

    user_agent = "User-Agent: CommentGrabber v0.1 (by /u/sjuha and /u/teefour)"
    r = praw.Reddit(user_agent=user_agent)

    comments = list()

    for comment in comment_stream(r, 'all', limit=100):
        comments.append(comment)

        if len(comments) > 100:
            return comments
            break


comments = getComments()
for comment in comments:
    print(comment)
