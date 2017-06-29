import praw

# reddit wrapper
reddit = praw.Reddit(client_id='',
                     client_secret='',
                    user_agent='snip_snap_snop bot v1.0 by snip_snap_snop') # throwaway account

# subreddit
subreddit_name = 'Running'
subreddit = reddit.subreddit(subreddit_name)

questions = []
question_details = []
top_comments = []

# traverse top 30 submissions of 'hot' category in subreddit
for submission in subreddit.hot(limit=30):

    title = submission.title

    # store submission and self text if it is a question and not already in questions list
    if '?' in title and title not in questions:
        questions.append(title)
        question_details.append(submission.selftext)
    

        # traverse comments in each submission to find top scoring comment
        comments = submission.comments
        top_score = 0
        top_comment = ''
        
        for comment in comments:

            comment_score = comment.score
            comment_details = comment.body
            
            if comment_score > top_score:
                top_score = comment_score
                top_comment = comment_details

        # store the top comment as the answer to the question       
        top_comments.append(top_comment)



# create or open file for writing
handler = open('running.txt','w')

# what the txt file is about
handler.write('Questions and top comments in ' + subreddit_name + '\n')
handler.write('_____________________________________' + '\n')

# write the question, question details, and answers for each question found in the file
for i in range(0, len(questions)):
    handler.write('Question:\n' + questions[i].encode('utf-8') + '\n\n')
    handler.write('Question details:\n' + question_details[i].encode('utf-8') + '\n\n')
    handler.write('Answer:\n' + top_comments[i].encode('utf-8') + '\n\n')
    handler.write('================================' + '\n\n')

# close the file after writing is done
handler.close()

        
