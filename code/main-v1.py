#imports
import pandas as pd 
import csv
from numpy import loadtxt

verified_tweets = []
# reads the list of seed words and writes it to a tuple 
def seed_list_reader(name):
    with open(name,"r") as file:
        lines = tuple(file.read().split())
        return lines

def tweet_csv_parser(name):
    tweets = []
    all_tweets = pd.read_csv(name).columns
    for tweet in all_tweets:
        tweets.append(tuple(tweet.split()))
    return tweets


def compare_tweet_to_seeds(seeds,candidates):
    for tweet in candidates: 
        test = list(set(tweet)&set(seeds))
        if len(test) >= 1:
            verified_tweets.append(tweet)
        else: 
            continue

        


seed_words = seed_list_reader("seed_words.txt")
tweets = tweet_csv_parser("negative.csv")

compare_tweet_to_seeds(seed_words,tweets)
print(verified_tweets)
#print(tweet_csv_parser("negative.csv"))
#print(seed_words)
