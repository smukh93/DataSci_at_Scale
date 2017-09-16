import sys
import json



""" 

Coputing Term Frequency of each word

The frequency of a term can be calculated as
[# of occurrences of the term in all tweets]/[# total number of terms in all tweets]

"""
def termFrequency():
    output_tweets = open(sys.argv[1])
    term_frequency = {}
    for line in output_tweets:
        tweets = json.loads(line)
        total_frequency = 0
        if 'text' in tweets:
            tweet = tweets['text'].encode('utf-8').split()
            for word in tweet:
                total_frequency+=1
                if word not in term_frequency:
                    term_frequency[word] = 1
                else:
                    term_frequency[word] += 1
    for word,term_freq in term_frequency.items():
        print (str(word) + "  " + str(float(term_freq)/total_frequency))
		
		
def main():
    termFrequency()

if __name__ == '__main__':
    main()	
