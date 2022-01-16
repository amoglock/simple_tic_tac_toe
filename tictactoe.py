XO = ('X', 'O')
counter = 0
winner = ''
game_state = []
user_input = '000000000'
player = 0


def _game_state(string):
    print('---------')
    global game_state
    state_change = ''.join([' ' if symbol == '0' else symbol for symbol in string])
    game_state = [list(state_change[x: x + 3]) for x in range(0, 7, 3)]
    for line in range(len(game_state)):
        print('|', game_state[line][0], game_state[line][1], game_state[line][2], '|')
    print('---------')
    checking()


def checking():
    global counter, winner
    check_list = [int(element) if element.isdigit() else element for element in user_input]
    # check diagonals
    if all([check_list[0], check_list[4], check_list[8]]) or \
            all([check_list[2], check_list[4], check_list[6]]):
        if check_list[0] == check_list[4] == check_list[8] or check_list[2] == check_list[4] == check_list[6]:
            counter += 1
            winner = check_list[4]
            return print(f'{winner} wins')
    for line in range(0, 7, 3):
        if all([check_list[line], check_list[line + 1], check_list[line + 2]]):
            if check_list[line] == check_list[line + 1] == check_list[line + 2]:  # check lines
                counter += 1
                winner = check_list[line]
                return print(f'{winner} wins')
    for row in range(3):
        if all([check_list[row], check_list[row + 3], check_list[row + 6]]):
            if check_list[row] == check_list[row + 3] == check_list[row + 6]:  # check rows
                counter += 1
                winner = check_list[row]
                return print(f'{winner} wins')
    if 0 not in check_list:
        return print('Draw')
    gameplay()


def gameplay():
    global user_input, player
    user_movie = input('Enter the coordinates: ').split()
    if ''.join(user_movie).isdigit():
        if 1 <= int(user_movie[0]) <= 3 and 1 <= int(user_movie[1]) <= 3:
            if game_state[int(user_movie[0]) - 1][int(user_movie[1]) - 1] not in XO:
                element = int(user_movie[0]) * 3 - 3 + int(user_movie[1]) - 1
                player += 1
                if player % 2 == 0:
                    user_input = user_input[: element] + 'O' + user_input[element + 1:]
                else:
                    user_input = user_input[: element] + 'X' + user_input[element + 1:]
                return _game_state(user_input)
            else:
                print('This cell is occupied! Choose another one!')
        else:
            print('Coordinates should be from 1 to 3!')
    else:
        print('You should enter numbers!')
    gameplay()


_game_state(user_input)







