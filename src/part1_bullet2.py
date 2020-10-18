import time
import re
import pymongo
from bson import json_util


# PART 1: BULLET 2: Top 5 most frequent words used in the commit messages


# get the commit data from the mongo db database
start_time = time.time()
client = pymongo.MongoClient("localhost", 27017)
db = client["scpr_db"]
commit_collection = db["commits"]
result = commit_collection.find({})

# count the frequency of each word in the commit messages
print('\nCalculating the frequency of each word in the commit messages ...')
commit_shas = set()
word_counts = {} # key: <string> word, value: <int> number of commits
num_commits, num_unique_commits, num_words = 0, 0, 0
for commit in result:
	num_commits += 1

	# # view commit data
	# print(json_util.dumps(commit, indent=4))
	# input()

	# skip duplicate commits
	if commit['sha'] in commit_shas:
		continue
	num_unique_commits += 1
	commit_shas.add(commit['sha'])

	# increment the count for all the words used in the commit message
	# replace all non alphabetical characters with space
	for word in re.sub(r'[^a-zA-Z]+', ' ', commit["commit"]["message"]).split(' '):
		if word == "": continue
		word = word.lower()
		if word not in word_counts.keys():
			word_counts[word] = 0
		word_counts[word] += 1
		num_words += 1
print('Done.')
print('Number of Commits        = %d' % num_commits)
print('Number of Unique Commits = %d' % num_unique_commits)
print('Number of Words          = %d\n' % num_words)

# sort the words and use the top n words
n = 5
word_counts = sorted(
	word_counts.items(),
	key=lambda item : item[1],
	reverse=True)[:n]

# output the top n words by frequency
print('The top %d most frequent words used in the commit messages are:' % n)
for i, (word, frequency) in enumerate(word_counts):
	print('    %d. word \"%s\" occurs %d times.' % (i+1, word, frequency))
print()

# output how long the program took to run
end_time = time.time()
duration = end_time - start_time
print('\nProgram duration: %d minutes and %d seconds\n' % (
	duration // 60, duration % 60))


