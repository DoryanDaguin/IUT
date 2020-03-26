"""

On vérifie que la valeur est supérieur à 20

>>> montant_argent > 20
True

On verifie que si on a le meme chiffre on gagne
>>> gagne_ou_perdu(15,15)
Bravo

On verifie que si on a pas le meme chiffre on perd
>>> gagne_ou_perdu(15,13)
Perdu

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

if __name__ == '__main__':

    import doctest

    if True:

        doctest.testmod(verbose=True, optionflags=512)

    else:

        doctest.testmod(verbose=True)
