# import randint for random a number between a min and a max value
from random import randint

gameRunning = True
#en la siguente lista se van a almacenar los resultados de los ganadores
gameResults = []

#Function: 
def monterAttak_Value():
    return randint(monster['attackMin'], monster['attackMax'])

def gameEnds(winnerName):
    print('The winner of the game is: ' + winnerName)
    

while gameRunning == True: 
    counter = 0
    newRound = True
    #DICTIONARY: 
    player = {'name': 'Dave', 'attack': 13, 'heal': 17, 'health': 100}
    monster = {'name':'Maximus', 'attackMin': 12, 'attackMax': 20, 'health': 100}

    print('-#-' * 25)
    print('Enter player name: ')
    player['name'] = input()
    print(player['name'] + ' has ' + str(player['health']) + ' of health' )
    print(monster['name'] + ' has ' + str(monster['health']) + ' of health' )
    print()
    while newRound == True:

        counter = counter + 1 
        playerWon = False
        monsterWon = False

        print('-#-' * 25)
        print('Please select action')
        print('1. Attack')
        print('2. Heal')
        print('3. Exit game')
        print('4. Show Results')

        playerChoise = input()

        if playerChoise == str(1): 
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                playerWon = True

            else:
                player['health'] = player['health'] - monterAttak_Value()
                if player['health']<= 0:
                    monsterWon = True

        elif playerChoise == str(2):
            player['health'] =  player['health'] + player['heal']
            player['health'] = player['health'] - monterAttak_Value()
            if player['health'] <= 0:
                monsterWon = True
                    
        elif playerChoise == str(3):
            gameRunning = False
            newRound = False
        
        # para iterar sobre cada lista de informacion de jugadores y mostrarla individualmente por linea: 
        elif playerChoise == str(4):
            for i in gameResults:
                print(i)

            
        else: 
            print('Invalid input')

        if playerWon == False and monsterWon == False:
            print(player['name'] + ' has ' + str(player['health']) + ' of health left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' of health left')
            print()
        
        elif playerWon: 
            gameEnds(player['name'])
            roundRsult = {'name ': player['name'], 'health ': player['health'], 'rounds ': counter}
            # con el .append se agrega el resultado del ganador a la lista de gameResults
            gameResults.append(roundRsult)
            newRound = False

        elif monsterWon: 
            gameEnds(monster['name'])
            roundRsult = {'name ': monster['name'], 'health ': monster['health'], 'rounds ': counter}
            # con el .append se agrega el resultado del ganador a la lista de gameResults
            gameResults.append(roundRsult)
            newRound = False




