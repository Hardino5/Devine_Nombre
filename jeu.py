from random import randint
continuer ='o'
while continuer == 'o':
    print('Bienvenue dans le jeu du plus ou moins')
    
    N_a_D = randint(1,100)
    print(N_a_D)
    compteur = 0
    while compteur < 3:
        essai1 = input('Entrez un nombre :')
        if N_a_D < int(essai1):
            print('Plus grand que nombre a deviner')
        elif N_a_D > int(essai1):
            print('Plus petit que nombre a deviner')
        else:
            print('Bravo, vous avez gagner')
            print('Fin du jeu')
            break
        compteur += 1

    if compteur == 3:
        print('Vous avez épuisé vos chances!')

continuer = input('Voulez-vous rejouer? (o/n)')