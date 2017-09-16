import sys
import json
import operator
scores = {}

states = {
'AK': 'Alaska',
'AL': 'Alabama',
'AR': 'Arkansas',
'AS': 'American Samoa',
'AZ': 'Arizona',
'CA': 'California',
'CO': 'Colorado',
'CT': 'Connecticut',
'DC': 'District of Columbia',
'DE': 'Delaware',
'FL': 'Florida',
'GA': 'Georgia',
'GU': 'Guam',
'HI': 'Hawaii',
'IA': 'Iowa',
'ID': 'Idaho',
'IL': 'Illinois',
'IN': 'Indiana',
'KS': 'Kansas',
'KY': 'Kentucky',
'LA': 'Louisiana',
'MA': 'Massachusetts',
'MD': 'Maryland',
'ME': 'Maine',
'MI': 'Michigan',
'MN': 'Minnesota',
'MO': 'Missouri',
'MP': 'Northern Mariana Islands',
'MS': 'Mississippi',
'MT': 'Montana',
'NA': 'National',
'NC': 'North Carolina',
'ND': 'North Dakota',
'NE': 'Nebraska',
'NH': 'New Hampshire',
'NJ': 'New Jersey',
'NM': 'New Mexico',
'NV': 'Nevada',
'NY': 'New York',
'OH': 'Ohio',
'OK': 'Oklahoma',
'OR': 'Oregon',
'PA': 'Pennsylvania',
'PR': 'Puerto Rico',
'RI': 'Rhode Island',
'SC': 'South Carolina',
'SD': 'South Dakota',
'TN': 'Tennessee',
'TX': 'Texas',
'UT': 'Utah',
'VA': 'Virginia',
'VI': 'Virgin Islands',
'VT': 'Vermont',
'WA': 'Washington',
'WI': 'Wisconsin',
'WV': 'West Virginia',
'WY': 'Wyoming'
}

stateSentimentScore = dict.fromkeys(states.keys(), 0);

def afinn_dict():
    sent_file = open(sys.argv[1])
    for line in sent_file:
	term, score = line.split("\t")
	scores[term]=int(score)
    #print scores.items()

def happiestState():
	tweet_file = open(sys.argv[2])
	for line in tweet_file:
		tweets = json.loads(line)
		total_Sentiment_score = 0
		if 'text' in tweets:
			tweet = tweets['text'].encode('utf-8').split()
			for word in tweet:
				if word in scores:
					total_Sentiment_score += scores[word]
		if 'user' in tweets and 'location' in tweets:
			location = tweets['text'].encode('utf-8').split(", ")
			if len(location)==2:
				for stateAbbv,stateName in states:
					if location[1]==stateAbbv or location[1]==stateName:
						stateSentimentScore[stateAbbv] += total_Sentiment_score
        happiestState = sorted(stateSentimentScore.items(),key=operator.itemgetter(1),reverse=True)[0]
        stateAbbv,StateName = happiestState
        print(stateAbbv)


def main():
	happiestState()

if __name__ == 'main':
	main()

       

	


if __name__ == '__main__':
    main()	
