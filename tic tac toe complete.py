import random
current="X"
gamefinished=None
game=True
board=["_","_","_",
       "_","_","_",
       "_","_","_"]
def pboard(board):
    print(board[0]+"|"+board[1]+"|"+board[2]+"|")
    print(board[3]+"|"+board[4]+"|"+board[5]+"|")
    print(board[6]+"|"+board[7]+"|"+board[8]+"|")

def you(board):
    global pos
    a=int(input("Enter a Number from 1 to 9 : "))
    if a>=1 and a<=9 and board[a-1]=="_":
        board[a-1]=current
    else:
        print("position already occupied")
            
def check(board):
    global game
    global gamefinished
    if game==True:
        if board[0]==board[1]==board[2] and board[0]!="_":
            gamefinished=board[0]
            game=False
            return True
        elif board[3]==board[4]==board[5] and board[3]!="_":
            gamefinished=board[3]
            game=False
            return True
        elif board[6]==board[7]==board[8] and board[6]!="_":
            gamefinished=board[6]
            game=False
            return True
        elif board[0]==board[3]==board[6] and board[0]!="_":
            gamefinished=board[0]
            game=False
            return True
        elif board[1]==board[4]==board[7] and board[3]!="_":
            gamefinished=board[1]
            game=False
            return True
        elif board[2]==board[5]==board[8] and board[2]!="_":
            gamefinished=board[2]
            game=False
            return True
        elif board[0]==board[4]==board[8] and board[0]!="_":
            gamefinished=board[0]
            game=False
            return True
        elif board[6]==board[4]==board[2] and board[6]!="_":
            gamefinished=board[6]
            game=False
            return True
def win():
    global game
    if game==True:
        if check(board)==True:
            pboard(board)
            print("The Winner is ",gamefinished)
            game=False
def tie():
    global game
    if game==True:
        if "_" not in board:
            pboard(board)
            print("ITS A TIE")
            game=False
def switch():
    global current
    if current=="X":
        current="O"
    else:
        current="X"
def PC():
    while current=="O":
        a=[0,1,2,3,4,5,6,7,8]
        b=random.choice(a)
        if board[b]=="_":
            board[b]=current
            switch()
while game==True:
    pboard(board)
    you(board)
    win()
    tie()
    switch()
    PC()
    win()
    tie()