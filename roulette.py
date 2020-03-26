# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 09:43:28 2020
@author: Doryan DAGUIN

"""

#################
## Importation ##
#################

import random
from math import ceil

############
## Classe ##
############

class Joueur_Roulette:

    def __init__(self, prenom, argent):
        self.prenom = str(prenom)
        self.argent = argent
        self.numero = 0
        self.mise = 0


###############
## Fonctions ##
###############

#Fonction de Bienvenue
def bienvenue():
	print ("-----[JEU DE LA ROULETTE]-----")
	print ("    Bienvenue sur le jeu !    ")
	print ("       Cree par Doryan        ")
	print ("           Jouons !           ")
	print ("------------------------------")

#Fonction qui demande la somme d'argent que les joueurs vont avoir
def porte_monnaie_f(Nombre_joueurs):
    argents = 0
    while argents < 20:
        print("\nVous êtes ",Nombre_joueurs," pour jouer à la roulette, il faut au moins un budget de 20€ par personne.")
        argents = int(input("Avec combien d'argent voulez vous jouer à notre roulette ? : "))   
    return argents
    
#Fonction qui crée le jeu de la roulette
def partie_roulette(joueurs, Nombre_joueurs, porte_monnaie):
    for x in range(0, Nombre_joueurs):
        joueurs.append(Joueur_Roulette(input("Nom du joueur " + str(x+1) + " : "), porte_monnaie))
    continuer_jouer = True
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
        print("\n * les jeux sont fait...Rien ne vas plus... * \n")
        print(" ___      ___      ___")
        print("\n ***       ", numero_gagnant, "      ***")
        print(" ___      ___      ___\n")
    
        for x in range(0, Nombre_joueurs):
            if joueurs[x].numero == numero_gagnant:
                print("Bravo " + joueurs[x].prenom + " vous avez le bon numéro, vous obtenez ",  joueurs[x].mise * 35, "€ !\n")
                joueurs[x].argent = joueurs[x].argent + joueurs[x].mise * 35
                
            elif joueurs[x].numero % 2 == numero_gagnant % 2: #Même couleur
                print("Bravo " + joueurs[x].prenom + " vous avez la bonne couleur, vous obtenez ", ceil(joueurs[x].mise * 0.5), "€ !\n")
                joueurs[x].argent = joueurs[x].argent + ceil(joueurs[x].mise * 0.5)         
           
            else:
                print("Pas de chance " + joueurs[x].prenom + " , vous perdez votre mise qui est de", joueurs[x].mise, "€\n")
                joueurs[x].argent = joueurs[x].argent - joueurs[x].mise
    
        for x in range(0, Nombre_joueurs):
            if joueurs[x].argent <= 0:
                print(joueurs[x].prenom + ", vous n'avez plus d'argent ! La partie est finie.\n")
                continuer_jouer = False           
            else:
                print(joueurs[x].prenom + " a maintenant", joueurs[x].argent, "€\n")
                
        if continuer_jouer:
          rester = str(input("Voulez vous rejouer à la roulette (Oui/Non) ? \n"))
          if rester.lower() == "non":         
              for x in range(0, Nombre_joueurs):
                  gains_quitter = joueurs[x].argent - porte_monnaie
                  if gains_quitter < 0 :
                      gains_quitter = -gains_quitter
                      print(joueurs[x].prenom + ", vous quittez le casino. En arrivant vous aviez",porte_monnaie,"€, vous avez perdu ",gains_quitter, "€ et vous repartez donc avec,",joueurs[x].argent,"€.\n")
                  else :
                      print(joueurs[x].prenom + ", vous quittez le casino. En arrivant vous aviez",porte_monnaie,"€, vous avez gagné ",gains_quitter, "€ et vous repartez donc avec,",joueurs[x].argent,"€.\n")
              continuer_jouer = False
     
         
########################################################################
################################PROGRAMME DU JEU########################
########################################################################
              
bienvenue()
Nb_joueurs = int(input("Bienvenue au Casino Paris Descartes, combien de personnes veulent jouer à la roulette : "))
joueur = []
montant_argent = porte_monnaie_f(Nb_joueurs)
partie_roulette(joueur, Nb_joueurs, montant_argent)
