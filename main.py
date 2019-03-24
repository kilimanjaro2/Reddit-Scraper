import praw
import sys
from praw.models import MoreComments

reddit = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)', client_id='mslOZtKlprikhQ', client_secret='Hhe0vuQDqF7lWOYGLmRe2nKejJg')


arguments = sys.argv[1:]
for url in arguments:
    submission = reddit.submission(url)
    print(submission.title)
    print(submission.selftext)
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        print(top_level_comment.body)
