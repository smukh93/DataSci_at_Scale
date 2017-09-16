import sys
import json


"""

A dictionary that maps a word with it's score

"""

word_scores = {}

"""
sentiment_Score(): 
Reads a word from AFINN.txt and creates a word sentiment score dictionary

"""
def sentiment_Score():
    sent_file = open(sys.argv[1])
    for line in sent_file:
        term,sentiment_score = line.split("\t")
        word_scores[term]=int(sentiment_score)

"""
tweet_sentiment_scorer():
Picks each word in a particular text, finds sentiment scores in word_scores. 
The sentiment of a tweet is equivalent to the sum of the sentiment scores
for each term in the tweet.

"""

def tweet_sentiment_scorer():
    output_tweets = open(sys.argv[2])
    for line in output_tweets:
        tweets = json.loads(line)
        tweet_sentiment_score = 0
        if 'text' in tweets:
            for word in (tweets['text'].encode('utf-8').split()):
                if word in word_scores:
                    tweet_sentiment_score+= word_scores[word]
            print(tweet_sentiment_score)
		
		
def main():
    sentiment_Score()
    tweet_sentiment_scorer()

if __name__ == '__main__':
    main()	
