import random

def create_game_string():
	game_string = " $ $ $ $ "
	count = 0
	while count < 7:
		game_string = jumble_game_line(game_string)
		count += 1
	return game_string
	
def jumble_game_line(game_line):
	random_index = random.randrange(0, len(game_line))
	string_part1 = game_line[:random_index]
	string_part2 = game_line[random_index + 1:]
	string_part3 = game_line[random_index]
	game_line = string_part1 + string_part2 + string_part3
	return game_line
	
def display_game_string(game_string):
	print("")
	print("    1     2     3     4     5     6     7     8     9    ")
	print("||     |     |     |     |     |     |     |     |     ||")
	print("||  "+str(game_string[0])+"  |  "+str(game_string[1])+"  |  "+str(game_string[2])+"  |  "+str(game_string[3])+"  |  "+str(game_string[4])+"  |  "+str(game_string[5])+"  |  "+str(game_string[6])+"  |  "+str(game_string[7])+"  |  "+str(game_string[8])+"  ||")
	print("||     |     |     |     |     |     |     |     |     ||")
	print("")
	
def get_user_position_num(player_num):
	print("PLAYER NUMBER: " + str(player_num))
	position_number = int(input("Enter position number: "))
	return position_number
	
def get_num_to_move():
	number_to_move = int(input("Enter number to move: " ))
	return number_to_move
	
def move_dollar_to_the_left(game_string, position_number, to_move):
	index = position_number - 1
	new_position = index - to_move
	string1 = game_string[:new_position]
	string2 = game_string[new_position + 1 + to_move:]
	final_string = string1 + "$" + " " * to_move + string2
	return final_string
	
def get_next_player_num(player_num):
	if player_num is 1:
		player_num = 2
	else:
		player_num = 1
	return player_num
	
def congratulate_player(player_num):
	print("=========================")
	print("** Y O U H A V E W O N **")
	print("     PLAYER NUMBER: " + str(player_num) + "     ")
	print("** Y O U H A V E W O N **")
	print("=========================")
	
def display_menu():
	print("1. PLAY COINSTRIP")
	print("2. EXIT")
	selection = int(input("Enter selection: "))
	if selection == 1:
		play_one_game()

# CHECK IF THE GAME HAS FINISHED
def check_game_finished(game_string):
	first_four_symbols = game_string[0:4]
	if first_four_symbols == "$$$$":
		return True
	return False

# PLAY ONE GAME OF COIN STRIP
def play_one_game():
	player_num = 1
	game_finished = False
	game_string = create_game_string()
	while game_finished == False:
		display_game_string(game_string)
		position_num = get_user_position_num(player_num)
		move_num = get_num_to_move()
		game_string = move_dollar_to_the_left(game_string,
		position_num, move_num)
		game_finished = check_game_finished(game_string)
		if game_finished:
			display_game_string(game_string)
			congratulate_player(player_num)
			display_menu()
		else:
			player_num = get_next_player_num(player_num)

def main():
	display_menu()
	play_one_game()
	print()
	print("BYE FROM COIN STRIP")

main()
