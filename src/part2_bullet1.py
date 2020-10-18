import requests
from datetime import datetime, timedelta


# PART 2: BULLET 1: All of 2020’s commit activity


# get the commit data from the github api
year = 2020
repo_owner = 'vuejs'
repo_name = 'vue'
url = 'https://api.github.com/repos/%s/%s/stats/commit_activity' % (repo_owner, repo_name)
response = requests.get(url)

# filter out commits not during year
# and output the results
print('\nCommit activity of the year %d:\n' % year)
for w in response.json():
	first_day_of_week = datetime.utcfromtimestamp(w["week"])
	last_day_of_week = first_day_of_week + timedelta(days=6)
	if first_day_of_week.year == year or last_day_of_week.year == year:
		print('    %d  commit%s occured in the week of   %s - %s   on the days: %s' % (
			w['total'],
			' ' if w['total'] == 1 else 's',
			first_day_of_week.strftime('%Y/%m/%d'),
			last_day_of_week.strftime('%Y/%m/%d'),
			w['days']))
print()


