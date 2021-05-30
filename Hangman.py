word_list=["velvet","volt","qlwa","hades","pendual","copula","red","dynamite",
"rampage","usao","sinobuz",]
import random
ans=random.choice(word_list)

def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\\    ",
             "|       / \\     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong<len(stages)-2:
        print("\n")
        print(" ".join(board))
        letter=input("Geuss a single letter\n")
        if len(letter)>1:
            print("Only one! Try again.")
        elif letter in rletters:
            number=rletters.index(letter)
            board[number]=letter
            rletters[number]="$"
            if "__" not in board:
                win=True
                break
        elif letter not in rletters:
            wrong+=1
            print("\n".join(stages[0:wrong+2]))

    if win:
        print("You win!\nThe answer is {}.".format(word))
    else:
        print("\n".join(stages))
        print("You lose.\nThe answer is {}.".format(word))

hangman(ans)
        


        
