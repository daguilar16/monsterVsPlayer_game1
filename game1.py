#playerName = "Dave"
#playerAttack = 10
#playerHeal = 16
#playerHealth = 100

#LIST:
#player = ['Dave', 10, 16, 100]

#DICTIONARY: 
player = {'name': 'Dave', 'attack': 10, 'heal': 16, 'health': 100}
monster = {'name':'Maximus', 'attack': 12, 'health': 100}
gameRunning = True

while gameRunning == True:

    print('Please select action')
    print('1. Attack')
    print('2. Heal')

    playerChoise = input()

    if playerChoise == str(1): 
        monster['health'] = monster['health'] - player['attack']
        player['health'] = player['health'] - monster['attack']
        print (monster['health'])
        print (player['health'])

    elif playerChoise == str(2):
        print('Heal player')
    else: 
        print('Invalid input')

    if player['health'] <= 0:
        gameRunning = False

