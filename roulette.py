import random
from math import ceil

class Joueur_Roulette:

    def __init__(self, prenom, argent):
        self.prenom = str(prenom)
        self.argent = int(argent)
        self.numero = 0
        self.mise = 0


Nombre_joueurs = int(input("Bienvenue au Casino Paris Descartes, combien de personnes veulent jouer à la roulette : "))
joueurs = []

porte_monnaie = 0
while porte_monnaie < 20:
    print("Vous êtes ",Nombre_joueurs," pour jouer à la roulette, il faut au moins un budget de 20€ par personne.")
    porte_monnaie = int(input("Avec combien d'argent voulez vous jouer à notre roulette ? : "))
    porte_monnaie_debut = porte_monnaie

continuer_jouer = True

for x in range(0, Nombre_joueurs):
    joueurs.append(Joueur_Roulette(input("Nom du joueur " + str(x+1) + " : "), porte_monnaie))

while continuer_jouer:
    print("Faites vos jeux !")
    for x in range(0, Nombre_joueurs):
        joueurs[x].numero = -1
        while joueurs[x].numero < 0 or joueurs[x].numero > 36:
            joueurs[x].numero = input((joueurs[x].prenom + ", sur quel numéro voulez-vous miser (entre 0 et 36): "))
            try:
                joueurs[x].numero = int(joueurs[x].numero)
            except ValueError:
                print("Vous n'avez pas saisi de nombre")
                joueurs[x].numero = -1
                continue
            if joueurs[x].numero < 0:
                print("Ce nombre est négatif")
            if joueurs[x].numero > 36:
                print("Ce nombre est supéieur à 36")
        
       
        joueurs[x].mise = 0
        while joueurs[x].mise <= 0 or joueurs[x].mise > porte_monnaie:
            joueurs[x].mise = input(joueurs[x].prenom 
                   + ", combien voulez-vous miser ? : ")
            try:
                joueurs[x].mise = int(joueurs[x].mise)
            except ValueError:
                print("Vous n'avez pas saisi de nombre")
                joueurs[x].mise = -1
                continue
            if joueurs[x].mise <= 0:
                print("La mise saisie est négative ou nulle.")
            if joueurs[x].mise > porte_monnaie:
                print("Vous ne pouvez miser autant, vous n'avez que", porte_monnaie, "€")
            
    numero_gagnant = random.randint(0,36)
    print("La roulette tourne,.... , .... , .... , et s'arrête sur le numéro", numero_gagnant)

    for x in range(0, Nombre_joueurs):
        if joueurs[x].numero == numero_gagnant:
            print("Bravo " + joueurs[x].prenom + " vous avez le bon numéro, vous obtenez ",  joueurs[x].mise * 35, "€ !")
            joueurs[x].argent = joueurs[x].argent + joueurs[x].mise * 35
            
        elif joueurs[x].numero % 2 == numero_gagnant % 2: #Même couleur
            print("Bravo " + joueurs[x].prenom + " vous avez la bonne couleur, vous obtenez ", ceil(joueurs[x].mise * 0.5), "€ !")
            joueurs[x].argent = joueurs[x].argent + ceil(joueurs[x].mise * 0.5)         
       
        else:
            print("Pas de chance " + joueurs[x].prenom + " , vous perdez votre mise qui est de", joueurs[x].mise, "€")
            joueurs[x].argent = joueurs[x].argent - joueurs[x].mise

    for x in range(0, Nombre_joueurs):
        if joueurs[x].argent <= 0:
            print(joueurs[x].prenom + ", vous n'avez plus d'argent ! La partie est finie.")
            continuer_jouer = False           
        else:
            print(joueurs[x].prenom + " a maintenant", joueurs[x].argent, "€")
            
    if continuer_jouer:
      rester = str(input("Voulez vous rejouer à la roulette (Oui/Non) ? "))
      if rester == "Non" or rester == "non" or rester == "NON":         
          for x in range(0, Nombre_joueurs):
              gains_quitter = joueurs[x].argent - porte_monnaie_debut
              if gains_quitter < 0 :
                  gains_quitter = -gains_quitter
                  print(joueurs[x].prenom + ", vous quittez le casino. En arrivant vous aviez",porte_monnaie_debut,"€, vous avez perdu ",gains_quitter, "€ et vous repartez donc avec,",joueurs[x].argent,"€")
              else :
                  print(joueurs[x].prenom + ", vous quittez le casino. En arrivant vous aviez",porte_monnaie_debut,"€, vous avez gagné ",gains_quitter, "€ et vous repartez donc avec,",joueurs[x].argent,"€")
          continuer_jouer = False