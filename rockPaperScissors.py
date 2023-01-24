import random

def play():
    user = input("Rock ('r'), Paper ('p'), or Scissors ('s'): ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It was a tie!"

    if checkWin(user, computer):
        return "You won!"
    
    return "You lost."
    
# r > s, s > p, p > r
def checkWin(p1, p2):
    if (p1 == 'r' and p2 == 's') or (p1 == 's' and p2 == 'p') or (p1 == 'p' and p2 == 'r'):
        return True
    return False

print(play())