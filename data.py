types = ['Aberrations',
'Beasts',
'Celestials',
'Constructs',
'Dragons',
'Elementals',
'Fey',
'Fiends',
'Giants',
'Humanoids',
'Monstrosities',
'Oozes',
'Plants',
'Undead'
]

monster_stats = [
'Name',
'Size',
'Type',
'Alignment',
'Armor Class (Tuple: Value, Type)',
'Hit Points',
'Speed (Array/Tuple Types)',
'STR (Value, Modifier)',
'DEX',
'CON',
'INT',
'WIS',
'CHA',
'Skills - String',
'Challenge Rating (Value, XP Value)',
'Actions String'
]

def TestMonster():
	goblin = {
		'name':'Goblin',
		'size':'Small',
		'type':'Humanoid',
		'Alignment':'Neutral Evil',
		'Armor Class': (15, 'leather armor', 'shield'),
		'Speed': (30,),
		'STR': (8, -1),
		'DEX': (14, 2),
		'CON': (10, 0),
		'INT': (10, 0),
		'WIS': (8, -1),
		'CHA': (8, -1),
		'skills': "Senses: Darkvision 60ft.\nSkills Stealth +6\nLanguages Common, Goblin\n",
		'challenge':(0.25, 50),
		'actions': "Nimble Escape. The goblin can take the Disengage or Hide action as a bonus action on each of its turns.\nScimitar. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.\nShortbow. Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage"
	}

	monsters = [goblin]
	#monsters.append(goblin)

	return monsters
# end of testMonster
