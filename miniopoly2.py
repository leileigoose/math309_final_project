import random
import matplotlib.pyplot as plt

# Miniopoly Board Initialization
ttl_spaces = 40 # 0-39 --> 0 == 40
card_spaces = [2, 7, 17, 22, 33, 36]
card_values = [50, 100, 200, -100, -150]

# Roll initialization
dice = [1, 2, 3, 4, 5, 6]

# Recorded values
money_record = []

def play_game():
    # Player information
    player_space = 0 # current space player is on
    player_bank = 200 
    total_rolls = 1 
    player_roll = []
    in_jail = False
    
    while total_rolls <= 20 and player_bank > 0:       
        while in_jail and total_rolls <=20:
            player_roll = random.choices(dice, k=2)
            
            # If they do not roll a double, keep them in jail
            if len(set(player_roll)) == 2:
                # Did not roll doubles
                player_bank -= 10
            else:
                in_jail = False
            total_rolls+=1
        
        if total_rolls > 20:
            break
        
        # roll the dice
        player_roll = random.choices(dice, k=2)
        total_rolls+=1
        player_space += sum(player_roll)
        
        # Check if the player is going to pass Go
        if player_space > 40:
            player_space -= 40
            player_bank += 200
        
        # Go to jail!
        if player_space == 30:
            player_space = 10
            in_jail = True
        else:
            # Landed on a card spacce
            if player_space in card_spaces:
                player_bank += random.choice(card_values)
            else:
                player_bank -= player_space
        
    return(player_bank)


for i in range(9999):
    money_record.append(play_game())
    
plt.hist(money_record)
plt.show()