from flask import Flask, session, redirect, url_for, escape, request, render_template
from python.game import *

app = Flask(__name__)
board = [None for i in range(9)]

# player is 1, computer is 0

first_moves = {
    0:4,
    1:0,
    2:5,
    3:0,
    4:0,
    5:2,
    6:4,
    7:1,
    8:4
}

def computer_move():
    count_of_moves = 0
    
    for position, square in enumerate(board):
        if square != None:
            count_of_moves += 1
            last_square = position

    if count_of_moves <= 1:
        board[first_moves[last_square]] = 0
    else:
        if check_win(board)[0]:
            return check_win(board)

        print '\nNow, computer goes...\n'

        move = move_helper(board, 0)
        print 'this was the move that computer tried:', move[1]
        board[move[1]] = 0

        if check_win(board)[0]:
            return check_win(board)

# def computer_move():
#     if check_win(board)[0]:
#         return check_win(board)

#     print '\nNow, computer goes...\n'

#     move = move_helper(board, 0)
#     print 'this was the move that computer tried:', move[1]
#     board[move[1]] = 0

#     if check_win(board)[0]:
#         return check_win(board)

@app.route('/')
def index():
    for i in range(9):
        board[i] = None
    return render_template('index.html', board=enumerate(board, 1), win=[False])

@app.route('/1')
def one():
    board[0] = 1
    win = computer_move()
    return render_template('index.html', board=enumerate(board, 1), win=win)

@app.route('/2')
def two():
    board[1] = 1
    win = computer_move()
    return render_template('index.html', board=enumerate(board, 1), win=win)

@app.route('/3')
def three():
    board[2] = 1
    win = computer_move()
    return render_template('index.html', board=enumerate(board, 1), win=win)

@app.route('/4')
def four():
    board[3] = 1
    win = computer_move()
    return render_template('index.html', board=enumerate(board, 1), win=win)

@app.route('/5')
def five():
    board[4] = 1
    win = computer_move()
    return render_template('index.html', board=enumerate(board, 1), win=win)

@app.route('/6')
def six():
    board[5] = 1
    win = computer_move()
    return render_template('index.html', board=enumerate(board, 1), win=win)

@app.route('/7')
def seven():
    board[6] = 1
    win = computer_move()
    return render_template('index.html', board=enumerate(board, 1), win=win)

@app.route('/8')
def eight():
    board[7] = 1
    win = computer_move()
    return render_template('index.html', board=enumerate(board, 1), win=win)

@app.route('/9')
def nine():
    board[8] = 1
    win = computer_move()
    return render_template('index.html', board=enumerate(board, 1), win=win)

# set the secret key.  keep this really secret:
app.secret_key = 'alex'

if __name__ == '__main__':
    app.run(debug=True)