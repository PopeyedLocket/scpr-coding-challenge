import time
import re
from datetime import datetime
import pymongo
from bson import json_util


# PART 1: BULLET 3: Both of the above sliced by year, i.e. "Top 5 repos for 2019"


# get the commit data from the mongo db database
start_time = time.time()
client = pymongo.MongoClient("localhost", 27017)
db = client["scpr_db"]
commit_collection = db["commits"]
result = commit_collection.find({})

# count the number of commits for each repo
# and the frequency of each word in the commit messages
print('\nCalculating the number of commits for each repo for each year and')
print('the frequency of each word in the commit messages for each year ...')
commit_shas = set()
repo_commit_counts = {} # key: <int> year, value: <dictionary> (key: <string> repo_url, value: <int> number of commits)
word_counts = {} # key: <int> year, value: <dictionary> (key: <string> word, value: <int> number of commits)
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

	# parse year from commit data
	year = datetime.strptime(
		commit["commit"]["author"]["date"],
		'%Y-%m-%dT%H:%M:%SZ').year
	if year not in repo_commit_counts.keys():
		repo_commit_counts[year] = {}
	if year not in word_counts.keys():
		word_counts[year] = {}

	# parse repo_url from commit_url
	repo_url = commit['url'].split('/')
	repo_url = repo_url[:repo_url.index('commits')] # remove "commits" and everything after
	repo_url.remove("repos") # remove "repos"
	repo_url[repo_url.index("api.github.com")] = "github.com" # change "api.github.com" to "github.com"
	repo_url = '/'.join(repo_url)

	# increment the number of commits for this repo
	if repo_url not in repo_commit_counts[year].keys():
		repo_commit_counts[year][repo_url] = 0
	repo_commit_counts[year][repo_url] += 1

	# increment the count for all the words used in the commit message
	# replace all non alphabetical characters with space
	for word in re.sub(r'[^a-zA-Z]+', ' ', commit["commit"]["message"]).split(' '):
		if word == "": continue
		word = word.lower()
		if word not in word_counts[year].keys():
			word_counts[year][word] = 0
		word_counts[year][word] += 1
		num_words += 1
print('Done.')
print('Number of Commits        = %d' % num_commits)
print('Number of Unique Commits = %d' % num_unique_commits)
print('Number of Words          = %d\n' % num_words)

# output the top repos and words for each year
n = 5
for year in sorted(repo_commit_counts.keys(), reverse=True):
	print('\nYear: %d' % year)

	# top repos by commits
	top_repos_this_year = sorted(
		repo_commit_counts[year].items(),
		key=lambda item : item[1],
		reverse=True)[:n]
	print('\n    Top %d repos of %d (out of %d total repos):' % (n, year, len(repo_commit_counts[year].keys())))
	for i, (repo_name, num_commits) in enumerate(top_repos_this_year):
		print('        %d. repo %s has %d commits.' % (i+1, repo_name, num_commits))

	# top words by frequency
	top_words_this_year = sorted(
		word_counts[year].items(),
		key=lambda item : item[1],
		reverse=True)[:n]
	print('\n    Top %d most frequent words of %d (out of %d total words):' % (n, year, len(word_counts[year].keys())))
	for i, (word, frequency) in enumerate(top_words_this_year):
		print('        %d. word \"%s\" occurs %d times.' % (i+1, word, frequency))
	print()

# output how long the program took to run
end_time = time.time()
duration = end_time - start_time
print('\nProgram duration: %d minutes and %d seconds\n' % (
	duration // 60, duration % 60))


