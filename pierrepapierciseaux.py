import random

# ajout d'un message d'accueil
print("Bienvenue dans Pierre-Papier-Ciseaux !")

# ajout d'une boucle pour jouer plusieurs parties
while True:
    # initialisation des scores et des choix
    player_score = 0
    computer_score = 0
    choices = {'p': 'pierre', 'a': 'papier', 'c': 'ciseaux'}
    
    # ajout d'une option pour choisir le nombre de manches jouées
    while True:
        try:
            num_rounds = int(input("Combien de manches voulez-vous jouer ? "))
            break
        except ValueError:
            print("Entrez un nombre entier valide.")
    
    # ajout d'une option pour choisir le niveau de difficulté de l'ordinateur
    while True:
        difficulty = input("Choisissez le niveau de difficulté de l'ordinateur (facile/moyen/difficile) : ")
        if difficulty in ['facile', 'moyen', 'difficile']:
            break
        else:
            print("Entrez une réponse valide.")
    
    # ajout d'une boucle pour jouer chaque manche
    for round_num in range(1, num_rounds+1):
        # ajout d'un message pour afficher le numéro de la manche
        print(f"\nManche {round_num} :")
        
        # ajout d'un message pour indiquer le score actuel
        print(f"Score : joueur {player_score} - {computer_score} ordinateur")
        
        # ajout d'une fonction pour valider l'entrée du joueur
        while True:
            player_choice = input("Entrez votre choix (pierre/p, papier/a, ciseaux/c) : ")
            if player_choice in ['p', 'a', 'c']:
                break
            else:
                print("Entrez une réponse valide.")
        
        # ajout d'une fonction pour choisir le choix de l'ordinateur en fonction du niveau de difficulté
        if difficulty == 'facile':
            computer_choice = random.choice(['p', 'a', 'c'])
        elif difficulty == 'moyen':
            if player_score > computer_score:
                computer_choice = random.choice(['a', 'c'])
            elif player_score < computer_score:
                computer_choice = random.choice(['p', 'a'])
            else:
                computer_choice = random.choice(['p', 'a', 'c'])
        else:
            if player_choice == 'p':
                computer_choice = 'a'
            elif player_choice == 'a':
                computer_choice = 'c'
            else:
                computer_choice = 'p'
        
        # ajout d'un message pour afficher les choix
        print(f"Joueur : {choices[player_choice]}")
        print(f"Ordinateur : {choices[computer_choice]}")
        
        # ajout de la logique pour déterminer le gagnant
        if player_choice == computer_choice:
            print("Egalité !")
        elif (player_choice == 'p' and computer_choice == 'c') or \
             (player_choice == 'a' and computer_choice == 'p') or \
             (player_choice == 'c' and computer_choice == 'a'):
            print("Le joueur gagne cette manche !")
            player_score += 1
        else:
            print("L'ordinateur gagne cette manche !")
            computer_score += 1
    
    # ajout d'un message pour indiquer le gagnant final
    print("\nPartie terminée !")
if player_score > computer_score:
    print("Le joueur remporte la partie !")
elif player_score < computer_score:
    print("L'ordinateur remporte la partie !")
else:
    print("Match nul !")

# ajout d'une boucle pour demander si le joueur veut rejouer
while True:
    replay = input("Voulez-vous rejouer ? (o/n) : ")
    if replay == 'o':
        break
    elif replay == 'n':
        print("Merci d'avoir joué, à bientôt !")
        exit()
    else:
        print("Entrez une réponse valide.")

