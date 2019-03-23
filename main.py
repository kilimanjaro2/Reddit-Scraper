import praw
from praw.models import MoreComments

reddit = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)', client_id='mslOZtKlprikhQ', client_secret='Hhe0vuQDqF7lWOYGLmRe2nKejJg')

submission = reddit.submission(url='https://www.reddit.com/r/cscareerquestions/comments/b469n3/why_are_recruiters_insistent_on_having_phone/')
print(submission.title)
print(submission.selftext)
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)
