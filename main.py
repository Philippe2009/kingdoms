'''
Ordi pour le prototype du jeu kingdoms inventé par Philippe Chevelev et Raphael Thiriot
'''
# Programme par Philippe Chevelev

import time
import random
class Player:
    def __init__(self, name, silver, wood):
        self.name = name
        self.silver = silver
        self.wood = wood
    def print_silver(self):
        print("Silver de "+self.name+' :'+ str(self.silver))

    def set_silver(self, new_silver):
        self.silver = new_silver

    def transaction_to(self,amount,destination):
        self.silver = self.silver-amount
        destination.set_silver(destination.silver + amount)
        pass


players:Player
DEFAULT_SILVER = 30
DEFAULT_WOOD = 30
# La liste qui va contenir tous les joueurs
players = []
def start_game():
    # imprime le titre du jeu en ASCII art
    # généré avec le site https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20 
    print('____  __.__                   .___                     ')
    print('|    |/ _|__| ____    ____   __| _/____   _____   ______')
    print('|      < |  |/    \  / ___\ / __ |/  _ \ /     \ /  ___/')
    print('|    |  \|  |   |  \/ /_/  > /_/ (  <_> )  Y Y  \\___ \ ')
    print('|____|__ \__|___|  /\___  /\____ |\____/|__|_|  /____  >')
    print('        \/       \//_____/      \/            \/     \/ ')
    print("Bonjour ! Combien de joueurs y-a-t'il dans la partie ?")
    player_number = input()
    for i in range(int(player_number)):
        print('nom du joueur ' + str(i) + ' ?')
        new_player_name = input()
        players.append(Player(new_player_name,DEFAULT_SILVER,DEFAULT_WOOD))
    for i in players:
        print('Bienvenue ' + i.name)
    print('vous pouvez désormais entrer des commandes dans le ***** terminal *****')
    print('Tapez la commande /help pour voir toutes les commandes possibles')

start_game()
# chaque élément du tableau est une ligne à afficher à l'écran
commands_explainations = ["la commande '/help' permet de voir toutes les commandes possibles. C'est la commande que vous venez d'entrer.",
                          "la commande '/money' permet d'obtenir l'argent contenu dans le compte de chaque joueur. A noter que la valeur des entreprises et actions ne sont pas incluses.  ",
                          "la commande '/transaction' permet d'effectuer une transaction entre deux joueurs ou avec la banque. Les instructions pour effectuer la transaction sont fournises lorsque la commande est appelée",
                          "la commande '/mine' permet de miner dans les mines de chaque joueur respectif",
                          "la commande '/quit' permet de quitter la partie (A noter: pour relancer le programme il faut d'abord quitter la partie)"


                          ]
# la boucle infinie 
while True:
    command = input()
    if command == '/money':
        for i in players:
            print('Argent de '+i.name+': '+str(i.silver)+' silver'+'.')
    elif command == '/transaction':
        print('******* bienvenue sur le terminal de la banque mondiale *******')
        print('voici les index des comptes de chaque joueur')
        for i in players:
            print(i.name+': '+ str(players.index(i)))
        print('Banque mondiale: -1')
        print('')
        print("Entrez l'index du joueur/entité qui effectue la transaction(celui à qui le jeui enlèvera l'argent)")
        transaction_from_index = input()
        print("Entrez désormais la somme d'argent que vous souhaitez transferer")
        transaction_ammount = input()
        # On vérifie si la transaction est avec la banque ou non
        if int(transaction_from_index) != -1:
            # On vérifie si le joueur a assez d'argent
            if players[int(transaction_from_index)].silver - int(transaction_ammount) >= 0:
                # Le joueur a assez d'argent, on lui enlève alors l'argent de la transaction
                players[int(transaction_from_index)].silver -= int(transaction_ammount)
                players[int(transaction_from_index)].print_silver()

                print('A qui voulez vous effectuer la transaction ?')
                # On réaffiche les index
                for i in players:
                    print(i.name+': '+ str(players.index(i)))
                print('Banque mondiale: -1')
                destination_index = input()
                if int(destination_index) != -1:
                    # On ajoute l'argent au destinataire
                    players[int(destination_index)].silver += int(transaction_ammount)
                    players[int(destination_index)].print_silver()
                    print('Transaction effectuée avec succès')
                else:
                    print('transaction à la banque effectuée avec succès.')
                    players[int(transaction_from_index)].print_silver()              
            
            else:
                # On informe le joueur de son incapacité financière à effectuer la transaction 
                print(players[int(transaction_from_index)].name + " ne possède pas assez d'argent pour effectuer la transaction ")
        else:
            # Dans ce cas, la banque envoie l'argent. Alors on ajoute juste l'argent au compte
            print('A qui voulez vous effectuer la transaction ?')
                # On réaffiche lles index
            for i in players:
                print(i.name+': '+ str(players.index(i)))
            destination_index = input()
            # On ajoute l'argent au destinataire
            players[int(destination_index)].silver += int(transaction_ammount)
            players[int(destination_index)].print_silver()
            
            pass
    elif command == '/quit':
        print('vous allez quitter la partie  Etes vous sûr de vouloir le faire ?')
        print("tapez 'Y' pour dire oui")
        print("tapez 'N' pour dire non")
        answer = input()
        if answer == 'Y':
            print('La partie est terminée')
            break
        else:
            print('La partie continue')
        break
    elif command == '/mine':
        print("Bienvenue dans la mine. Un nombre entre 1 et 100 va être généré.")
        print('Souhaitez vous un rappel des gains possibles selon le nombre choisi ?')
        print("tapez 'Y' pour dire oui")
        print("tapez 'N' pour dire non")
        answer = input()
        if answer == 'Y':
            print('Voici un rappel: ')
            
            print('mine de niveau 1')
            print(' Entre 0 et 25: rien ')
            print(' Entre 25 et 75 : 10 silver ')
            print(' Entre 75 et 100 : 20 silver, soit 1 gold ')
            print('')
            
            print('mine de niveau 2')
            print(' Entre 0 et 20: rien ')
            print(' Entre 20 et 70 : 10 silver ')
            print(' Entre 70 et 95 : 20 silver, soit 1 gold ')
            print(' Entre 95 et 100 : 40 silver, soit 1 diamond ')
            print('')

            print('mine de niveau 3')
            print(' Entre 0 et 15: rien ')
            print(' Entre 15 et 65 : 10 silver ')
            print(' Entre 65 et 90 : 20 silver, soit 1 gold ')
            print(' Entre 90 et 100 : 40 silver, soit 1 diamond ')
            print('')

            print('mine de niveau 4')
            print(' Entre 0 et 10: rien ')
            print(' Entre 10 et 60 : 10 silver ')
            print(' Entre 60 et 80 : 20 silver, soit 1 gold ')
            print(' Entre 80 et 100 : 40 silver, soit 1 diamond ')
            print('')

            print('mine de niveau 5')
            print(' Entre 0 et 15: rien ')
            print(' Entre 10 et 55 : 10 silver ')
            print(' Entre 55 et 75 : 20 silver, soit 1 gold ')
            print(' Entre 75 et 100 : 40 silver, soit 1 diamond ')
            print('')

        else:
            print("D'accord.")
        print("Procédons au minage")
        for i in range(len(players)):
            print(players[i].name + ", Combien de mines avez vous ?")
            mines_number = int(input())
            for j in range(mines_number):
                print('Mine de ' + players[i].name+ ' n° ' + str(j) + ': ' + str(random.randint(0,100)))
        print("vous pouvez désormais rajouter l'argent gagné dans vos comptes à l'aide de la commande '/transaction'. ")
    elif command == '/help':
        for i in commands_explainations:
            print(i)
            #print('')
    else:
        print('commande inconnue')
        print('la commande: "'+command+'" '+"est inconnue. Vérifiez l'orthographe.")
        print('Tapez la commande /help pour voir toutes les commandes possibles')
        pass
