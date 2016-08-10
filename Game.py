import random

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 'It is not a valid name!'

def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'It is not a valid number!'

def rpsls(player_choice): 
    print "\n Player chooses %s" % player_choice
    
    player_number = name_to_number(player_choice) 
    comp_number = random.randrange(5)
    
    print " Computer chooses %s" % number_to_name(comp_number)
    
    if (player_number - comp_number) % 5 == 0:
        print ' Player and computer tie!'
    elif (player_number - comp_number) % 5 == 1 or (player_number - comp_number) % 5 == 2:
        print ' Player wins!'
    else:
        print ' Computer wins!'
             
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
