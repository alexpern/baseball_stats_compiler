import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--player',required=True,help='input player to see stats')
parser.add_argument('--stat',required=False,default='',help='specific stat to return')
parser.add_argument('--batPitch',required=True,choices=['bat','pitch'],help='is this a batting or pitching stat')
parser.add_argument('--agstat',required=False,default='',choices=['hits','obp','slug','ops','avg'],help='select aggregate stat')
args=parser.parse_args()

player = args.player
stat = args.stat
batPitch = args.batPitch
agstat = args.agstat

f = open(player + '_' + batPitch + '.txt','r')
stats = f.readlines()
count = 0
nums = ['1','2','3','4']
statTypes = ['sing','k','doub','trip','hr','bb','out','hbp','lob','rbi']

def grabStat(stat,playerStats):
	count = 0
	if stat:
		for item in playerStats:
			if item.strip('\n') == stat:
				count += 1
		return count
		print(count)

def getStatline(playerStats,countedStats):
	for each in countedStats:
		count = 0
		for item in playerStats:
			if item.strip('\n') == each:
				count += 1
		print(each + ': ' + str(count))

if stat:
	print(grabStat(stat,stats))
else:
	print(getStatline(stats,statTypes))

if agstat != '':
	hitsStat = grabStat('sing',stats) + grabStat('doub',stats) + grabStat('trip',stats) + grabStat('hr',stats)
	walkStat = grabStat('bb',stats) + grabStat('hbp',stats)
	ab = hitsStat + grabStat('k',stats) + grabStat('out',stats) + grabStat('fc',stats)
	pa = ab + grabStat('bb',stats) + grabStat('hbp',stats) + grabStat('sacf',stats) + grabStat('sacb',stats)
	tb = (grabStat('sing',stats) + (2 * (grabStat('doub',stats))) + (3 * (grabStat('trip',stats))) + (4 * (grabStat('hr',stats))))

	if agstat == 'hits':
		print(hitsStat)
	elif agstat == 'obp':
		print(str(float(hitsStat + walkStat) / pa))
	elif agstat == 'avg':
		print(str(float(hitsStat / ab)))
	elif agstat == 'slug':
		print(str(float(tb / ab)))
	elif agstat == 'ops':
		print(str(float((tb / ab) + ((hitsStat  + walkStat) / pa))))

f.close()