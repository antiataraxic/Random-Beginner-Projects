import random
def rps():
    user = input("'r' for rock,'s' for scissors,'p' for paper :")
    comp = random.choice(['r', 'p', 's'])
    if user == comp:
        return "Draw"
    elif is_winner(user, comp):
        return "Player wins"

    return "Computer wins"

def is_winner(player,opp):
    if (player == 'r' and opp == 's') or (player == "s" and opp == "p") or (player == "p" and opp == 'r'):
        return True

print(rps())





