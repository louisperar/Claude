def variable():
    # récolter le porte monnaie d'une personne
    wallet = int(input("valeur du porte feuille : "))
    print("La valeur du porte feuille est de " + str(wallet) + "€")
    # créer un produit qui aura pour valeur 50
    product = 50
    print("Le prix du produit est de " + str(product) + "€")
    # afficher la nouvelle valeur du porte monnaie, après son achat
    if wallet >= product:
        if wallet == 50:
            choix = input("Vous avez pile de quoi acheté voulez-vous acheter le "
                          "produit quand-même? ")
            if choix == "oui" or choix == "Oui" or choix == "oUi" or choix == "ouI" \
                    or choix == "OUi" or choix == "OuI" or choix == "oUI" or choix == "OUI":
                wallet -= product
                print("achat réussi")
                print("Vous avez acheté le produit")
                print("Vous n'avez plus d'argent")
                exit()
            else:
                print("Achat échoué")
                print("Vous avez annulé l'achat")
                print("Il vous reste " + str(wallet) + "€")
                exit()
        else:
            wallet -= product
            print("Achat réussi")
            print("Vous avez désormais plus que " + str(wallet) + "€")
            exit()
    else:
        print("Achat échoué")
        print("Vous n'avez pas assez d'argent")
        print("Il vous reste " + str(wallet) + "€")
        exit()


def portefeuille():
    wallet = int(input("Combien avez-vous d'argent? "))
    computer_price = int(input("Combien coûte l'ordinateur? "))
    if computer_price < wallet:
        print("l'achat est possible")
        choix = str(input("Voulez vous acheter l'odinateur? "))
        if choix == "oui" or choix == "Oui" or choix == "oUi" or choix == "ouI" \
                or choix == "OUi" or choix == "OuI" or choix == "oUI" or choix == "OUI":
            wallet -= computer_price
            print("Achat effectué")
            print("Il vous reste désormais {}€".format(wallet))
            boolean = "True"
        else:
            print("")
            print("vous avez annulé l'achat")
            print("Il vous reste toujours {}€".format(wallet))
            boolean = "false"
    elif computer_price == wallet:
        print("Vous avez pile assez d'argent")
        choix = str(input("Voulez vous acheter l'odinateur? "))
        if choix == "oui" or choix == "Oui" or choix == "oUi" or choix == "ouI" \
                or choix == "OUi" or choix == "OuI" or choix == "oUI" or choix == "OUI":
            wallet -= computer_price
            print("Achat effectué")
            print("Il vous ne vous reste plus rien")
            print("{}€".format(wallet))
            boolean = "True"
        else:
            print("vous avez annulé l'achat")
            print("Il vous reste toujours {}€".format(wallet))
            boolean = "false"
    else:
        print("Vous n'avez pas assez d'argent pour acheter l'ordinateur")
        boolean = "false"
    achat = ("Vous possédez désormais un ordinateur", "Vous avez annulé l'achat "
                                                      "de l'ordinateur")[boolean == "True"]
    print(achat)


if __name__ == "__main__":
    portefeuille()