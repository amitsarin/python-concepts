import random
color=["green","red","yellow","violet","indigo","blue","orange"]

while True:
    col= color[random.randint(0,len(color)-1)]
    guess=input("I am thinking about a color, can you guess it: ")

    while True:
        if(col==guess.lower()):
               break
        else:
               guess=input("nope.. try again: ")
    print("you guessed it correct, I was thinking of ",col)
    play_again=input("lets play again? type 'no' to quit.")
    if play_again.lower()=='no':
        break
print("it was fun")
