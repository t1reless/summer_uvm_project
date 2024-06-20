import csv

"""
tweets = []

df = pd.read_csv("negative.csv")
col = df.columns
for tweet in col: 
    if " hi " in tweet: 
        tweets.append(tweet)

if len(tweets) == 0:
    print("No dice")
else: 
        print(tweets)
        print(len(tweets))
"""
# create a function to load in a list of seed words into memory
# as a list

# create a function to load a given csv into memory 
# 
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