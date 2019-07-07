import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--player', required=True, help='input Mets player')
parser.add_argument('--type', required=True, choices=['bat','pitch'], help='bat or pitch')
parser.add_argument('--sing', required=False, default=0, help='input true for hit')
parser.add_argument('--k', required=False, default=0, help='strikeout')
parser.add_argument('--doub', required=False, default=0, help='double')
parser.add_argument('--trip', required=False, default=0, help='triple')
parser.add_argument('--hr', required=False, default=0, help='home run')
parser.add_argument('--bb', required=False, default=0, help='walk')
parser.add_argument('--out', required=False, default=0, help='groundout / flyout / forceout')
parser.add_argument('--hbp', required=False, default=0, help='hit by pitch')
parser.add_argument('--lob', required=False, default=0, type=int, help='left on base')
parser.add_argument('--rbi', required=False, default=0, type=int, help='runs batted in')
parser.add_argument('--sacf',required=False, default=0, help='sacrifice fly')
parser.add_argument('--sacb',required=False, default=0, help='sacrifice bunt')
parser.add_argument('--fc',required=False,default=0,help='fielders choice')
args = parser.parse_args()

player = args.player
batPitch = args.type
sing = args.sing
k = args.k
doub = args.doub
trip = args.trip
hr = args.hr
bb = args.bb
out = args.out
hbp = args.hbp
lob = args.lob
rbi = args.rbi
sacf = args.sacf
sacb = args.sacb
fc = args.fc
bool_outcomes = {'sing':sing,'k':k,'doub':doub,'trip':trip,'hr':hr,'bb':bb,'out':out,'hbp':hbp}
int_outcomes = {'lob':lob,'rbi':rbi}

if batPitch == 'bat':
	f = open((player + '_bat') + '.txt','a')
else: f = open((player + '_pitch') + '.txt','a')


for key in bool_outcomes.keys():
	if bool_outcomes[key]:
		f.write('\n' + key)
for key in int_outcomes.keys():
	if int_outcomes[key] > 0:
		count = 0
		while count < int_outcomes[key]:
			f.write('\n' + key)
			count += 1

f.close()