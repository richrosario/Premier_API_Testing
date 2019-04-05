#/usr/bin/python
from sportmonks import *

token = 'nUUgH5WyYmqtksHD5pbCAFq0xaRrXYXHswOum5FfU4p7zEl9unl3xplmTOtF'
init(token)

#Prem ID: 8
#Prem SID: 12962

#League ID + NAME

'''
print('Leagues:')
for l in leagues():
	print(l['id'], l['name'])
'''

print('Teams:')
for t in teams(12962):
	print(t['id'], t['name'])

