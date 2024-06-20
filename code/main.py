import csv
import pandas as pd 

seed_words_list = []
tweets = []
word_matches_and_frequency = {"unhappy":1}

def words_surrounding_key_word_in_tweet(word,tweet_as_list):
    position = tweet_as_list.index(word)
    next_words = []
    try:
        next_words.append(tweet_as_list[position+1])
        next_words.append(tweet_as_list[position+2])
    except:
        IndexError
    else: 
        return next_words

# create a function to load in a list of seed words into memory
def seed_lexicon_reader(txt_file_name):
    with open(txt_file_name) as file:
        lines = file.readlines()
        for word in lines:
            seed_words_list.append(word.strip())


def tweet_csv_reader(file_name):
    all_tweets = pd.read_csv(file_name).columns
    for tweet in all_tweets:
        tweets.append(tweet.split())

def finding_seed_words_in_tweets():
    words = set(seed_words_list)
    for tweet_list in tweets:
        result = [x for x in tweet_list if x in words]
        if len(result) == 0:
            continue
        else:
            close_words = words_surrounding_key_word_in_tweet(result[0],tweet_list)
            if close_words == None:
                continue
            else:
                for i in range(0,2):
                    word = close_words[i]
                    keys = word_matches_and_frequency.keys()
                    print(word)
                    if word in keys:
                        word_matches_and_frequency.update({word:word_matches_and_frequency[word]+1})
                    else:
                        word_matches_and_frequency[word] = 1
seed_lexicon_reader("seed_words.txt")
tweet_csv_reader("negative.csv")
finding_seed_words_in_tweets()
print(word_matches_and_frequency)
# create a function to load a given csv into memory 
# then iterate over the values 
# 1. chunk the tweet into a list splitting on spaces
# 2. compare the words in the list with the list of seed words 
# 
# ctrl flow:
# if there is a match then check the next two indices against the output
# dictionary. 
#   if already in the dictionary increase the count val by 1, 
# else:
#   add it and set the val to one. 


# create a function to print the complete dictionary with all words that occur over 
# n times