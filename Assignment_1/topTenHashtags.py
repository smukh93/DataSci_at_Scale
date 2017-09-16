import sys
import json
import operator

"""

Compute the top ten hashtags 

"""

hashtagFreq = {}


def topTenHashtags():
	tweets = open(sys.argv[1])
	for line in tweets:
		tweet = json.loads(line)
		if 'entities' in tweet and 'hashtags' in tweet['entities']:
				hashtagList = tweet['entities']['hashtags']
				for hashtag in hashtagList:
					hashtag_value = hashtag['text'].encode('utf-8')
					if hashtag_value not in hashtagFreq:
						hashtagFreq[hashtag_value] = 1
					else:
						hashtagFreq[hashtag_value] += 1
      #Sort in Desc order 
	sorted_hashtagFreq = sorted(hashtagFreq.items(), key = operator.itemgetter(1), reverse=True)
	i = 0
	for hashtag,hashFreq in sorted_hashtagFreq:
		print (str(hashtag) + " " + str(hashFreq))
		i+=1
		if i == 10:
			break		
		
def main():
    topTenHashtags()

if __name__ == '__main__':
    main()		
