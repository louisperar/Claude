from math import *


def cercle():
    print("que voulez vous calculer?\nrayon, diamètre, air, périmètre")
    calcul = input("")
    diametre = None
    air = None
    rayon = None
    perimetre = None
    if calcul == "rayon" or calcul == "diamètre" or calcul == "air" or calcul == "périmètre":
        print("rentré les valeurs que vous avez.\n Merci de mettre \"0\" si vous n'avez pas cette mesure")
        print("diamètre : ")
        diametre = float(input())
        print("air : ")
        air = float(input())
        print("rayon : ")
        rayon = float(input())
        print("périmètre : ")
        perimetre = float(input())
        if calcul == "rayon":
            if str(air) == "0":
                if str(perimetre) == "0":
                    if str(diametre) != "0":
                        rayon = diametre/2
                        print("le rayon de votre cercle est le diamètre/2 donc"
                              + str(diametre) + "/2 = " + str(rayon))
                    else:
                        print("Vous n'avez pas donné de valeur ou"
                              " alors vous n'avez pas écris correctement "
                              "bien évidemment mettre 0 dans rayon puisque "
                              "vous calculez le rayon")
                        cercle()
                else:
                    rayon = perimetre/(2*pi)
                    print("le rayon de votre est le périmètre/(2*π) donc" +
                          str(perimetre) + "/(2*π) = " + str(rayon))
            else:
                rayon = sqrt(air/pi)
                print("le rayon de votre est le √(air/π) donc √(" +
                      str(air) + "/π) = " + str(rayon))
        elif calcul == "diamètre":
            if str(air) == "0":
                if str(perimetre) == "0":
                    if str(rayon) != "0":
                        diametre = rayon*2
                        print("le diametre de votre cercle est le diamètre/2 donc"
                           + str(rayon) + "/2 = " + str(diametre))
                    else:
                        print("Vous n'avez pas donné de valeur ou"
                              " alors vous n'avez pas écris correctement \n"
                                "bien évidemment mettre 0 dans diamètre puisque "
                              "vous calculez le rayon\n\nVous êtes prié de me "
                              "donner des chiffres ou nombres et non du texte")
                        cercle()
                else:
                    diametre = perimetre/(2*pi)
                    print("le diametre de votre est le périmètre/(2*π) donc" +
                          str(perimetre) + "/(2*π) = " + str(diametre))
            else:
                diametre = sqrt(air/pi)
                print("le diametre de votre est le √(air/π) donc √(" + str(air) + "/π) = " + str(diametre))
        elif calcul == "air":
            print("Vous avez le \"diamètre\" ou le \"rayon\"?\n")
        elif calcul == "périmètre":
            print("Vous avez le \"diamètre\" ou le \"rayon\"?\n")
        else:
            print("erreur")
            while True:
                break
    else:
        print("Veuillez écrire correctement\nMerci !!!\n\n")


def carre():
    print("que voulez vous calculer?\nrayon, diamètre, air, périmètre")
    calcul = input("")
    arete = None
    rayon = None
    perimetre = None
    if calcul == "rayon" or calcul == "diamètre" or calcul == "air" or calcul == "périmètre":
        print("rentré les valeurs que vous avez.\n Merci de mettre \"0\" si vous n'avez pas cette mesure")
        print("diamètre : ")
        diametre = int(input())
        print("air : ")
        air = int(input())
        print("rayon : ")
        rayon = int(input())
        print("périmètre : ")
        perimetre = int(input())
        if calcul == "rayon":
            if str(air) == "0":
                if str(perimetre) == "0":
                    if str(diametre) != "0":
                        rayon = diametre/2
                        print("le rayon de votre cercle est le diamètre/2 donc"
                              + str(diametre) + "/2 = " + str(rayon))
                    else:
                        print("Vous n'avez pas donné de valeur ou"
                              " alors vous n'avez pas écris correctement "
                              "bien évidemment mettre 0 dans rayon puisque "
                              "vous calculez le rayon")
                        cercle()
                else:
                    rayon = perimetre/(2*pi)
                    print("le rayon de votre est le périmètre/(2*π) donc" +
                          str(perimetre) + "/(2*π) = " + str(rayon))
            else:
                rayon = sqrt(air/pi)
                print("le rayon de votre est le √(air/π) donc √(" +
                      str(air) + "/π) = " + str(rayon))
        elif calcul == "diamètre":
            if str(air) == "0":
                if str(perimetre) == "0":
                    if str(rayon) != "0":
                        diametre = rayon*2
                        print("le diametre de votre cercle est le diamètre/2 donc"
                           + str(rayon) + "/2 = " + str(diametre))
                    else:
                        print("Vous n'avez pas donné de valeur ou"
                              " alors vous n'avez pas écris correctement \n"
                                "bien évidemment mettre 0 dans diamètre puisque "
                              "vous calculez le rayon\n\nVous êtes prié de me "
                              "donner des chiffres ou nombres et non du texte")
                        cercle()
                else:
                    diametre = perimetre/(2*pi)
                    print("le diametre de votre est le périmètre/(2*π) donc" +
                          str(perimetre) + "/(2*π) = " + str(diametre))
            else:
                diametre = sqrt(air/pi)
                print("le diametre de votre est le √(air/π) donc √(" + str(air) + "/π) = " + str(diametre))
        elif calcul == "air":
            print("Vous avez le \"diamètre\" ou le \"rayon\"?\n")
        elif calcul == "périmètre":
            print("Vous avez le \"diamètre\" ou le \"rayon\"?\n")
        else:
            print("erreur")
            while True:
                break
    else:
        print("Veuillez écrire correctement\nMerci !!!\n\n")


def rectangle():
    print("que voulez-vous calculer?\nlargeur, longueur, air")
    calcul = input("")
    if calcul == "largeur" or calcul == "longueur" or calcul == "air":
        if calcul == "largueur":
            print("Quel est l'air?")
            air = input("")
        #elif calcul == "longueur"
        elif calcul == "air":
            print("Vous avez le \"diamètre\" ou le \"coté\"?")
        else:
            print("erreur")
            while True:
                break
    else:
        print("Veuillez écrire correctement\nMerci !!!\n\n")


def triangle():
    print("que voulez-vous calculer?\nlargeur, longueur, air")
    calcul = input("")
    if calcul == "largeur" or calcul == "longueur" or calcul == "air":
        if calcul == "largueur":
            print("Quel est l'air?")
            air = input("")
        #elif calcul == "longueur"
        elif calcul == "air":
            print("Vous avez le \"diamètre\" ou le \"coté\"?")
        else:
            print("erreur")
            while True:
                break
    else:
        print("Veuillez écrire correctement\nMerci !!!\n\n")


def losange():
    print("que voulez-vous calculer?\nlargeur, longueur, air")
    calcul = input("")
    if calcul == "largeur" or calcul == "longueur" or calcul == "air":
        if calcul == "largueur":
            print("Quel est l'air?")
            air = input("")
        #elif calcul == "longueur"
        elif calcul == "air":
            print("Vous avez le \"diamètre\" ou le \"coté\"?")
        else:
            print("erreur")
            while True:
                break
    else:
        print("Veuillez écrire correctement\nMerci !!!\n\n")


def parallelogramme():
    print("que voulez-vous calculer?\nlargeur, longueur, air")
    calcul = input("")
    if calcul == "largeur" or calcul == "longueur" or calcul == "air":
        if calcul == "largueur":
            print("Quel est l'air?")
            air = input("")
        #elif calcul == "longueur"
        elif calcul == "air":
            print("Vous avez le \"diamètre\" ou le \"coté\"?")
        else:
            print("erreur")
            while True:
                break
    else:
        print("Veuillez écrire correctement\nMerci !!!\n\n")


def polygone_regulier():
    print("que voulez-vous calculer?\nlargeur, longueur, air")
    calcul = input("")
    if calcul == "largeur" or calcul == "longueur" or calcul == "air":
        if calcul == "largueur":
            print("Quel est l'air?")
            air = input("")
        #elif calcul == "longueur"
        elif calcul == "air":
            print("Vous avez le \"diamètre\" ou le \"coté\"?")
        else:
            print("erreur")
            while True:
                break
    else:
        print("Veuillez écrire correctement\nMerci !!!\n\n")