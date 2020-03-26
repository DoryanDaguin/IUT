"""

Test 1 : On vérifie que la valeur est supérieur à 20

>>> montant_argent > 20
True

Test 2 : On verifie que si on a le meme chiffre on gagne
>>> gagne_ou_perdu(15,15)
Bravo

Test 3 : On verifie que si on a pas le meme chiffre on perd
>>> gagne_ou_perdu(15,13)
Perdu

Test 4 :On verifie que si on a la meme couleur on gagne
>>> bonnecouleur_oupas(26,14)
Bravo meme couleur

Test 5 :On verifie que si on le numero mise est >36 il y a un message d'erreur
>>> numero_mise(39)
Nombre >36

Test 6 :On verifie que si on on mise plus que l'argent qu'on a il y a un message d'erreur
>>> argent_mise(150,100)
Mise > argent possede

Test 7 :On verifie que si on on mise 0 ou moins il y a un message d'erreur
>>> argent_mise(-20,100)
Mise negative

"""


def porte_monnaie_f_reussie(Nombre_joueurs):
    argents = 0
    while argents < 20:
        argents = 30  
    return argents
montant_argent = porte_monnaie_f_reussie(2)

def gagne_ou_perdu(joueurs_numero,numero_gagnant):
    if joueurs_numero == numero_gagnant:
        return print("Bravo")
    return print("Perdu")

def bonnecouleur_oupas(joueurs_numero,numero_gagnant):
    if joueurs_numero % 2 == numero_gagnant % 2:
        return print("Bravo meme couleur")
    return print("Perdu")

def numero_mise(numero):
  try:
    numero = int(numero)
  except ValueError:
    print("Erreur")
  if numero < 0:
    print("Nombre négatif")
  if numero > 36:
    print("Nombre >36")

def argent_mise(mise, porte_monnaie):
  try:
    mise = int(mise)
  except ValueError:
    print("Erreur")
  if mise <= 0:
    print("Mise negative")
  if mise > porte_monnaie:
    print("Mise > argent possede")

if __name__ == '__main__':

    import doctest

    if True:

        doctest.testmod(verbose=True, optionflags=512)

    else:

        doctest.testmod(verbose=True)
