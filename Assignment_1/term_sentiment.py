import sys
import json

"""

A dictionary that maps a word with it's score from AFINN.txt

The file AFINN-111.txt contains a list of pre-computed sentiment scores.
Each line in the file contains a word or phrase followed by a sentiment score.
Each word or phrase that is found in a tweet but not found in AFINN-111.txt 
should be given a sentiment score of 0. 
See the file AFINN-README.txt for more information.

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
unknown_words_sentiment_generate():

Finds sentiments of word that do not appear in the AFINN.txt

Picks each word in a particular text, finds sentiment scores from word_scores. 
The sentiment of a tweet is equivalent to the sum of the sentiment scores
for each term in the tweet.

if word is not found in word_Scores, then, we find using the idea that a message
is positive if it has any positive word, but negative if it has negative words.
http://www.cs.cmu.edu/~nasmith/papers/oconnor+balasubramanyan+routledge+smith.icwsm10.pdf


"""        


def unknown_words_sentiment_generate():
    output_tweets = open(sys.argv[2])
    newScores = {}
    for line in output_tweets:
        tweets = json.loads(line)
        tweet_sentiment_score = 0
        if 'text' in tweets:
            #Tweet score of the entire tweet
            tweet = (tweets['text'].encode('utf-8').split())
            for word in tweet:
                if word in word_scores:
#                    print tweet
                    tweet_sentiment_score+= word_scores[word]
    
            for word in tweet:
    		#print(tweet_sentiment_score)
                if word not in word_scores:
                    #tweet score calculation for words not in the word corpus
                    if word not in newScores:
                        newScores[word] = float(tweet_sentiment_score/len(tweet))
                    else:
                        newScores[word] += float(tweet_sentiment_score/len(tweet))																																																												
        for newWord,newScore in newScores.items():
            print (str(newWord) + " " + str(newScore))
		
		
def main():
    sentiment_Score()
    unknown_words_sentiment_generate()

if __name__ == '__main__':
    main()	
