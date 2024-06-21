#imports
import pandas as pd 
import csv
from numpy import loadtxt
from collections import Counter
import sys

#arguments
seed_file = sys.argv[1]
tweet_candidate_file = str(sys.argv[2])
lower_bound = int(sys.argv[3])

#storage 
verified_tweets = []
temp_list = []
grand_list = []

#functions

# reads the list of seed words and writes it to a tuple 
def seed_list_reader(name):
    with open(name,"r") as file:
        lines = tuple(file.read().split())
        return lines

# reads csv of input tweets and returns a list of tuples
def tweet_csv_parser(name):
    tweets = []
    all_tweets = pd.read_csv(name).columns
    for tweet in all_tweets:
        tweets.append(tuple(tweet.split()))
    return tweets

# accepts a tuple of seed words and a list of tuples and checks for intersection
# if there is intersection then it adds them to a list of verified tweets
def compare_tweet_to_seeds(seeds,candidates):
    for tweet in candidates: 
        test = list(set(tweet)&set(seeds))
        if len(test) >= 1:
            verified_tweets.append(tweet)
        else: 
            continue

# converts the list of verified tweets into a list containing all words
def corpus_maximus():
    for tweet in verified_tweets:
        for word in tweet:
            grand_list.append(word)

#returns a new list excluding words that occur under n number of times
def lower_bound_filter(lower_bound):
    working_dict = Counter(grand_list)
    new_dict = {key:val for key, val in working_dict.items() if val >= lower_bound}
    print(Counter(new_dict))

seed_words = seed_list_reader(seed_file)
tweets = tweet_csv_parser(tweet_candidate_file)

compare_tweet_to_seeds(seed_words,tweets)

corpus_maximus()

# prints a dictionary of all words in all tweets which contain the seed words 
# and their counts
lower_bound_filter(lower_bound)