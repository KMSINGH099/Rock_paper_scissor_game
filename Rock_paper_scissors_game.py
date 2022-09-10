import random
n = int(input("enter how many times you want to play game:"))
count = 0
for i in range(0, n):

    def play():
        print("'R for rock','P for paper','S for scissors'")
        user = input("Enter your choice:")
        computer = random.choice(['R', 'S', 'P'])
        print("Computer choice is:", computer)

        if user == computer:
            return "tie"
        if is_win(user, computer):
            return "win"
        else:
            return "lose"

    def is_win(user, computer):
        if (user == 'S' and computer == 'P') or (user == 'P' and computer == 'R') or (user == 'R' and computer == 'S'):
            return True

    r = play()
    if r == "tie":
        print("Match tie,play again")
    elif r == "lose":
        print("You Lost!,next time")
    else:
        print("Congratulations, You Won!")
        count += 1

print("You won the game", count, "times")