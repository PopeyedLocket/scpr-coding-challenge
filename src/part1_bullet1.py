import time
import pymongo
from bson import json_util


# PART 1: BULLET 1: Top 5 repos by commit activity (# of commits)


# get the commit data from the mongo db database
start_time = time.time()
client = pymongo.MongoClient("localhost", 27017)
db = client["scpr_db"]
commit_collection = db["commits"]
result = commit_collection.find({})

# count the number of commits for each repo
print('\nCalculating the number of commits for each repo ...')
commit_shas = set()
repo_commit_counts = {} # key: <string> repo_url, value: <int> number of commits
num_commits, num_unique_commits = 0, 0
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

	# parse repo_url from commit_url
	repo_url = commit['url'].split('/')
	repo_url = repo_url[:repo_url.index('commits')] # remove "commits" and everything after
	repo_url.remove("repos") # remove "repos"
	repo_url[repo_url.index("api.github.com")] = "github.com" # change "api.github.com" to "github.com"
	repo_url = '/'.join(repo_url)

	# increment the number of commits for this repo
	if repo_url not in repo_commit_counts.keys():
		repo_commit_counts[repo_url] = 0
	repo_commit_counts[repo_url] += 1
print('Done.')
print('Number of Commits        = %d' % num_commits)
print('Number of Unique Commits = %d\n' % num_unique_commits)

# sort the repos and use the top n repos
n = 5
repo_commit_counts = sorted(
	repo_commit_counts.items(),
	key=lambda item : item[1],
	reverse=True)[:n]

# output the top n repos by number of commits
print('The Top %d repos by commit activity (# of commits) are:' % n)
for i, (repo_name, num_commits) in enumerate(repo_commit_counts):
	print('    %d. repo %s has %d commits.' % (i+1, repo_name, num_commits))
print()

# output how long the program took to run
end_time = time.time()
duration = end_time - start_time
print('\nProgram duration: %d minutes and %d seconds\n' % (
	duration // 60, duration % 60))


