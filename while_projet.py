from random import randint

nbr_a_deviner = randint(1, 100)
nbr_essai = 5
i = 0
while i < nbr_essai:
    essai = input('Entrez un nombre ({0} essai): '.format(i +1))
    if int(essai) > nbr_a_deviner:
        print('Le nombre à deviner est plus petit que ' + essai)
    elif int(essai) < nbr_a_deviner:
        print('Le nombre à deviner est plus grand que ' + essai)
    else:
        print('Bravo vous avez gagner en {0} essai(s).'.format(i+1))
        break
    i += 1
if int(essai) != nbr_a_deviner:
    print('Vous avez perdu.')
    print('Le nombre à deviner était {0}.'.format(nbr_a_deviner))

print('Fin du jeu.')