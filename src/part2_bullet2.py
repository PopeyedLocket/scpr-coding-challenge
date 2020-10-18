import requests
import json


# PART 2: BULLET 2: Most active contributor in terms of commits


# get the contributor data from the github api
repo_owner = 'vuejs'
repo_name = 'vue'
url = 'https://api.github.com/repos/%s/%s/stats/contributors' % (repo_owner, repo_name)
response = requests.get(url)

# find the most active contributor
most_commits = 0
contributor = {
	"username"    : None,
	"profile_url" : None
}
for c in response.json():
	# # view contributor data
	# print(json.dumps(x, indent=4))
	# input()
	if c['total'] > most_commits:
		most_commits = c["total"]
		contributor = {
			"username"    : c["author"]["login"],
			"profile_url" : c["author"]["html_url"]
		}

# output the results
print("\nMost active contributor in terms of commits:")
print("    Username:    %s"   % contributor["username"])
print("    Profile URL: %s\n" % contributor["profile_url"])


