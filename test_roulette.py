"""

On vérifie que la valeur est supérieur à 20

>>> montant_argent > 20
True

"""

def porte_monnaie_f_reussie(Nombre_joueurs):
    argents = 0
    while argents < 20:
        argents = 30  
    return argents
montant_argent = porte_monnaie_f_reussie(2)


if __name__ == '__main__':

    import doctest

    if True:

        doctest.testmod(verbose=True, optionflags=512)

    else:

        doctest.testmod(verbose=True)