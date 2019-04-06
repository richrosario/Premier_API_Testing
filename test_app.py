#/usr/bin/python
from sportmonks import *

token = 'nUUgH5WyYmqtksHD5pbCAFq0xaRrXYXHswOum5FfU4p7zEl9unl3xplmTOtF'
init(token)

#Prem ID: 8
#Prem SeasonID: 12962(SID)
#LEI_ID: 42
#Vardy ID: 1182

######################################

## Finds the League ID + NAME of all league ##-------------

'''
print('Leagues:')
for l in leagues():
	print(l['id'], l['name'])
'''

## List of all seaons in DB, match with above league ID##-------------

'''
print('Seasons:')
for s in seasons():
	print(s['id'], s['name'],s['league_id'])
'''

##Finds teams in a specified season given a season ID ##-------------

'''
print('Teams:')
for t in teams(12962):
	print(t['id'], t['name'])
'''

## List of players with stats in a team within a season ID ##-------------


print('Player Data:')
for ts in team_squad(12962,42):
	print (player(ts['player_id'])['lastname'], ts, '\n')


## Data for a specific player ##-------------

'''
print('Player Data:')
for ts in team_squad(12962,42):
		if ts['player_id'] == 1182:
			print (player(ts['player_id'])['lastname'], ts, '\n')

'''

## Specific Data for a specific player ##-------------

'''
print('Player Data:')
for ts in team_squad(12962,42):
		if ts['player_id'] == 1182:
			print (player(ts['player_id'])['lastname'], ts['goals'], '\n')
'''

