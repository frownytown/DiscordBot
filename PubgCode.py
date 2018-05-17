from pubg_python import PUBG, Shard


player_name = ""


api = PUBG("", Shard.PC_NA)

def iterator_func(player_name, api):
	players = api.players().filter(player_names=[player_name])
	player = players[0]

	for index, match in enumerate(player.matches):
		match_data = api.matches().get(player.matches[index].id)
		#print(match_data)
		match_roster = match_data.rosters
		print("-----------------MATCH NUMBER %s ---------------" %(index+1))
		print("Game Mode -", match_data.game_mode)
		print("Match Duration -", match_data.duration)
		participant_filtering(match_roster)
		print("\n")

def participant_filtering(match_roster):
	# Filter the list of participants for the one I want
	for squads in match_roster:
		participant = squads.participants[0]
		#print(participant.name)
		if participant.name == player_name:
			print("Player Name -----", participant.name)
			print("Kills -", participant.kills)
			print("Assists -", participant.assists)
			print("Revives -", participant.revives)
			print("Boosts -", participant.boosts)
			print("Damage Dealt -", participant.damage_dealt)
			print("Death Type -", participant.death_type)
			print("Win Place -", participant.win_place)

iterator_func(player_name, api)