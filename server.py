from flask import Flask, render_template, request, redirect
from collections import namedtuple
app = Flask(__name__)
Post = namedtuple('Post', ['title'])



# Create the database:

user_to_posts = {
    'Game ID':[],
    'Player X':[
        Post('Welcome to TicTacToe'),
    ],
    'Player O':[
        Post('Welcome to TicTacToe'),
    ],
    'Winner':[]
}



# route user/name:

@app.route('/user/<name>')
def play(name):
    posts = user_to_posts[name]
    return render_template('play.html', name=name, posts=posts)



# route /login:

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect('/user/' + request.form['player_X_name'])
    else:
        return render_template('login.html', method=request.method)



# Initial board:

theboard = {
    '1': ' ', '2': ' ', '3': ' ', 
    '4': ' ', '5': ' ', '6': ' ', 
    '7': ' ', '8': ' ', '9': ' ', 
}

board_keys = []

for key in theboard:
    board_keys.append(key)



# Print the board:

@app.route('/user/<name>', methods=['GET', 'POST'])

def print_board(board):
    if request.method == 'POST':
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        return redirect('/user/' + request.form['player_X_name'])
    else:
        return render_template('login.html', method=request.method)



# Tictactoe function:

@app.route('/login', methods=['GET', 'POST'])

def tictactoe():

    if request.method == 'POST':
    
        turn = 'X'
        count = 0

        # Enter player name:
        player_X_name = input("Enter player X name:")
        player_O_name = input("Enter player O name:")

        for i in range(10):

            print_board(theboard)

            if turn == 'X':
                print("It's you turn,", player_X_name, ". Move to which place?")
            else:
                print("It's you turn,", player_O_name, ". Move to which place?")
        
            def player_name(turn):
                if turn == 'X':
                    return (player_X_name)
                else:
                    return (player_O_name)

            move = input()

            if theboard[move] == ' ':
                theboard[move] = turn
                count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue
            
            # Check the winner:
            if count >= 5:
                if theboard['1'] == theboard['2'] == theboard['3'] != ' ':
                    print_board(theboard)
                    print("\nGame Over.\n")
                    print(player_name(turn), "wins")
                    break
                elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':
                    print_board(theboard)
                    print("\nGame Over.\n")
                    print(player_name(turn), "wins")
                    break
                elif theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                    print_board(theboard)
                    print("\nGame Over.\n")
                    print(player_name(turn), "wins")
                    break
                elif theboard['1'] == theboard['4'] == theboard['7'] != ' ':
                    print_board(theboard)
                    print("\nGame Over.\n")
                    print(player_name(turn), "wins")
                    break
                elif theboard['2'] == theboard['5'] == theboard['8'] != ' ':
                    print_board(theboard)
                    print("\nGame Over.\n")
                    print(player_name(turn), "wins")
                    break
                elif theboard['3'] == theboard['6'] == theboard['9'] != ' ':
                    print_board(theboard)
                    print("\nGame Over.\n")
                    print(player_name(turn), "wins")
                    break
                elif theboard['1'] == theboard['5'] == theboard['9'] != ' ':
                    print_board(theboard)
                    print("\nGame Over.\n")
                    print(player_name(turn), "wins")
                    break
                elif theboard['3'] == theboard['5'] == theboard['7'] != ' ':
                    print_board(theboard)
                    print("\nGame Over.\n")
                    print(player_name(turn), "wins")
                    break

            # Define the draw:
            if count == 9:
                print("\nGame Over.\n")
                print("It's a draw!")

            # Change the turn after each move:
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

        # Restart the game:
        restart = input("Do want to play Again?(y/n)")
        if restart == "y" or restart == "Y":  
            for key in board_keys:
                theboard[key] = " "

            tictactoe()

        return redirect('/user/' + request.form['player_X_name'])
    else:
        return render_template('login.html', method=request.method)
