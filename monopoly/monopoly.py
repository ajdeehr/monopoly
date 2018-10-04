#import libraries
import random
import time

#set up global variables
board = ['Go', 'Mediterranean Avenue', 'Community Chest', 'Baltic Avenue','Income Tax', 'Reading Railroad','Oriental Avenue', 'Chance', 'Vermont Avenue','Connecticut Avenue','Jail','St. Charles Place', 'Electric Company', 'States Avenue', 'Virginia Avenue', 'Pennsylvania Railroad', 'St. James Place', 'Community Chest', 'Tennessee Avenue', 'New York Avenue', 'Free Parking', 'Kentucky Avenue', 'Chance', 'Indiana Avenue','Illinois Avenue','B. & O. Railroad', 'Atlantic Avenue', 'Ventnor Avenue', 'Water Works', 'Marvin Gardens', 'Go To Jail', 'Pacific Avenue', 'North Carolina Avenue', 'Community Chest', 'Pennsylvania Avenue', 'Short Line Railroad', 'Chance', 'Park Place', 'Luxury Tax', 'Boardwalk']
property_info = {'Mediterranean Avenue':{'cost':60,'rent':2,'ownerID':0},'Baltic Avenue':{'cost':60,'rent':2,'ownerID':0},'Oriental Avenue':{'cost':100,'rent':6,'ownerID':0},'Vermont Avenue':{'cost':100,'rent':6,'ownerID':0},'Connecticut Avenue':{'cost':120,'rent':8,'ownerID':0}, 'St. Charles Place':{'cost':140,'rent':10,'ownerID':0},'States Avenue':{'cost':140,'rent':10,'ownerID':0},'Virginia Avenue':{'cost':160,'rent':12,'ownerID':0},'St. James Place':{'cost':180,'rent':14,'ownerID':0},'Tennessee Avenue':{'cost':180,'rent':14,'ownerID':0},'New York Avenue':{'cost':200,'rent':16,'ownerID':0}, 'Kentucky Avenue':{'cost':220,'rent':18,'ownerID':0},'Indiana Avenue':{'cost':220,'rent':18,'ownerID':0},'Illinois Avenue':{'cost':240,'rent':20,'ownerID':0},'Atlantic Avenue':{'cost':260,'rent':22,'ownerID':0},'Ventnor Avenue':{'cost':260,'rent':22,'ownerID':0},'Marvin Gardens':{'cost':280,'rent':24,'ownerID':0},'Pacific Avenue':{'cost':300,'rent':26,'ownerID':0}, 'North Carolina Avenue':{'cost':300,'rent':26,'ownerID':0},'Pennsylvania Avenue':{'cost':320,'rent':28,'ownerID':0},'Park Place':{'cost':350,'rent':35,'ownerID':0},'Boardwalk':{'cost':400,'rent':50,'ownerID':0}}
railroad_info =  {'Reading Railroad':{'cost':200, 'rent':0,'ownerID':0},'Pennsylvania Railroad':{'cost':200,'rent':0,'ownerID':0},'B. & O. Railroad':{'cost':200, 'rent':0,'ownerID':0},'Short Line Railroad':{'cost':200, 'rent':0,'ownerID':0}}
utilites_info = {'Electric Company':{'cost':200,'rent':75,'ownerID':0},'Water Works':{'cost':200,'rent':75,'ownerID':0}}
railroads = ['Reading Railroad', 'Pennsylvania Railroad', 'B. & O. Railroad', 'Short Line Railroad']
railroads_rent = [25,50,100,200]
ulilities = ['Electric Company', "Water Works"]
player = {'position':0,'money':1500,'playerID': 1,'inJail':False, 'jailRolls':0}
computer = {'position':0,'money':1500,'playerID': 2,'inJail':False, 'jailRolls':0}
game_over = False

#handle players turn
def player_move(player):
    global game_over
    diceRolls = []
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print('You rolled a {} and a {}'.format(dice1, dice2))
    diceRolls.append(dice1 + dice2)
    if dice1 == dice2:
        input('You rolled a double. Press enter to roll again:')
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print('You rolled a {} and a {}'.format(dice1, dice2))
        diceRolls.append(dice1 + dice2)
        if dice1 == dice2:
            input('You rolled a double. Press enter to roll again:')
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            print('You rolled a {} and a {}'.format(dice1, dice2))
            diceRolls.append(dice1 + dice2)
            if dice1 == dice2:
                input('You rolled a double again. You must go to Jail')
                player['inJail'] = True
                player['position'] = 10
    if player['inJail'] == False:
        for i in range(len(diceRolls)):
            player['position'] = (player['position']+diceRolls[i])
            if player['position'] > len(board):
                player['position'] = player['position']%len(board)
                player['money']+= 200
                print("You collected $200. You now have ${}.".format(player['money']))
            print("You landed on {}".format(board[player['position']]))
            print()
            if board[player['position']] in property_info:
                if property_info[board[player['position']]]['ownerID'] == 0:
                    print("The cost of {} is ${}. The rent is ${}".format(board[player['position']],property_info[board[player['position']]]['cost'],property_info[board[player['position']]]['rent']))
                    answer = input("Would you like to buy {}? (y or n)  ".format(board[player['position']]))
                    if answer == "y":
                        property_info[board[player['position']]]['ownerID'] = player['playerID']
                        player['money'] -= property_info[board[player['position']]]['cost']
                        print("You bought {}. You now have ${}.".format(board[player['position']], player['money']))
                        print()
                    else:
                        print("You passed up a great opportunity :(")
                elif property_info[board[player['position']]]['ownerID'] != player['playerID']:
                    player['money'] -= property_info[board[player['position']]]['rent']
                    computer['money'] += property_info[board[player['position']]]['rent']
                    if player['money'] < 0:
                        game_over = True
                        print("You went bankrupt. The computer wins.")
                        return
                    print("Rent is ${}. You now have ${}.".format(property_info[board[player['position']]]['rent'], player['money']))
            elif board[player['position']] in railroad_info:
                if railroad_info[board[player['position']]]['ownerID'] == 0:
                    print("The cost of {} is ${}. The rent is ${}".format(board[player['position']],railroad_info[board[player['position']]]['cost'],railroad_info[board[player['position']]]['rent']))
                    answer = input("Would you like to buy {}? (y or n)  ".format(board[player['position']]))
                    if answer == "y":
                        railroad_info[board[player['position']]]['ownerID'] = player['playerID']
                        player['money'] -= railroad_info[board[player['position']]]['cost']
                        print("You bought {}. You now have ${}.".format(board[player['position']], player['money']))
                        print()
                    else:
                        print("You passed up a great opportunity :(")
                elif railroad_info[board[player['position']]]['ownerID'] != player['playerID']:
                    owner = railroad_info[board[player['position']]]['ownerID']
                    owned = 0
                    for ele in railroads:
                        if railroad_info[ele]['ownerID'] == owner:
                            owned += 1
                    player['money'] -= railroads_rent[owned+1]
                    computer['money'] += railroads_rent[owned+1]
            elif board[player['position']] in utilites_info:
                if utilites_info[board[player['position']]]['ownerID'] == 0:
                    print("The cost of {} is ${}. The rent is ${}".format(board[player['position']],utilites_info[board[player['position']]]['cost'],utilites_info[board[player['position']]]['rent']))
                    answer = input("Would you like to buy {}? (y or n)  ".format(board[player['position']]))
                    if answer == "y":
                        utilites_info[board[player['position']]]['ownerID'] = player['playerID']
                        player['money'] -= utilites_info[board[player['position']]]['cost']
                        print("You bought {}. You now have ${}.".format(board[player['position']], player['money']))
                        print()
                    else:
                        print("You passed up a great opportunity :(")
                elif utilites_info[board[player['position']]]['ownerID'] != player['playerID']:
                    owner = utilites_info[board[player['position']]]['ownerID']
                    owned = 0
                    for ele in ulilities:
                        if utilites[ele]['ownerID'] == owner:
                            owned += 1
                        
                    
                    
            elif board[player['position']] == 'Jail':
                print("You're just visiting though.")
            elif board[player['position']] == 'Go to Jail':
                player['inJail'] = True
                player['position'] = 10
            print()
            print()
    if player["inJail"] == True:
        print("You are in jail. ")
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 == dice2:
            player["jailRolls"] = player["jailRolls"] + 1
        
            

#handle computer's turn
def ai_move(computer):
    global game_over
    spaces = random.randint(1,6)
    computer['position'] = (computer['position']+spaces)%len(board)
    print("The computer landed on {}.".format(board[computer['position']]))
    if board[computer['position']] in property_info:
        if property_info[board[computer['position']]]['ownerID'] == 0:
            if computer['money'] > property_info[board[computer['position']]]['cost']:
                computer['money'] -= property_info[board[computer['position']]]['cost']
                property_info[board[computer['position']]]['ownerID'] = computer['playerID']
                print("The computer bought {}".format(board[computer['position']]))
        elif property_info[board[computer['position']]]['ownerID'] != computer['playerID']:
            player['money'] += property_info[board[computer['position']]]['rent']
            computer['money'] -= property_info[board[computer['position']]]['rent']
            if computer['money'] < 0:
                game_over = True
                print("The computer went bankrupt. You win!");
                return
            print("The computer payed you ${} in rent money and now has ${}. You now have ${}.".format(property_info[board[computer['position']]]['rent'], computer['money'], player['money']))
    elif board[computer['position']] == "Go":
        computer['money']+= 200
    print()
    
#main method, alternates between player and computer turns
def main():
    print("Welcome to Monopoly\n")
    while not game_over:
        input("press enter to continue:")
        print()
        player_move(player)
        if game_over:
            break
        time.sleep(.5)
        ai_move(computer)
        time.sleep(.5)

if __name__ == '__main__':
    main()
