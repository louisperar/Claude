def main():
    while True:
        print("\nCeci est un programme pour calculer des formes en 2 ou en 3 dimensions\n\n"
              "que voulez-vous faire? \"2 dimensions\" ou en \"3 dimensions\"\n"
              "écrire \"2\" pour les calculs en 2 dimensions ou "
              "\"3\" pour les calculs en 3 dimensions ou "
              "\"stop\" pour arréter le programme")
        decision = input("")
        if decision == "2" or decision == "3" or decision == "stop":
            if decision == "2":
                deux()
                while True:
                    choix = input("Avez-vous d'autre calculs? ")
                    if choix == "oui" or choix == "non":
                        if choix == "oui":
                            print("")
                            break
                        elif choix == "non":
                            stop(2)
                        else:
                            print("erreur")
                    else:
                        print("Veuillez écrire correctement\nMerci !!!\n\n")
            elif decision == "3":
                trois()
                while True:
                    choix = input("Avez-vous d'autre calculs? ")
                    if choix == "oui" or choix == "non":
                        if choix == "oui":
                            print("")
                            break
                        elif choix == "non":
                            stop(2)
                        else:
                            print("erreur")
                    else:
                        print("Veuillez écrire correctement\nMerci !!!\n\n")
            elif decision == "stop":
                stop(1)
            else:
                print("erreur")
        else:
            print("Veuillez écrire correctement\nMerci !!!\n\n")


from vérif_dimension import dimension
from calcul2d import deux
from calcul3d import trois
from stop import stop


if __name__ == "__main__":
    main()