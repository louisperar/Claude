from math import *


def sphere():
    print("que voulez vous calculer?\nlargeur, longueur, volume, hauteur")
    calcul = input("")
    largeur = None
    longueur = None
    volume = None
    hauteur = None
    if calcul == "volume" or calcul == "largeur" or calcul == "longueur" or calcul == "hauteur":
        print("rentré les valeurs que vous avez.\n Merci de mettre \"0\" si vous n'avez pas cette mesure")
        print("largeur : ")
        largeur = int(input())
        print("longueur : ")
        longueur = int(input())
        print("volume : ")
        volume = int(input())
        print("hauteur : ")
        hauteur = int(input())
        if calcul == "volume":
            if str(longueur) != "0":
                if str(hauteur) != "0":
                    if str(largeur) != "0":
                        volume = largeur * longueur * hauteur
                        print("le volume de votre cercle est égale à largeur * longueur * hauteur donc"
                              + str(largeur) + " * " + str(longueur) + " * " + str(hauteur) + " = " + str(volume))
                    else:
                        print("Vous n'avez pas donné de valeur ou"
                              " alors vous n'avez pas écris correctement "
                              "bien évidemment mettre 0 dans rayon puisque "
                              "vous calculez le rayon")
                        sphere()
                else:
                    rayon = hauteur/(2*pi)
                    print("le rayon de votre est le hauteur/(2*π) donc" +
                          str(hauteur) + "/(2*π) = " + str(volume))
            else:
                rayon = sqrt(longueur/pi)
                print("le rayon de votre est le √(longueur/π) donc √(" +
                      str(longueur) + "/π) = " + str(volume))
        elif calcul == "largeur":
            if str(longueur) == "0":
                if str(hauteur) == "0":
                    if str(volume) != "0":
                        largeur = volume*2
                        print("le largeur de votre cercle est le diamètre/2 donc"
                           + str(volume) + "/2 = " + str(largeur))
                    else:
                        print("Vous n'avez pas donné de valeur ou"
                              " alors vous n'avez pas écris correctement \n"
                                "bien évidemment mettre 0 dans diamètre puisque "
                              "vous calculez le rayon\n\nVous êtes prié de me "
                              "donner des chiffres ou nombres et non du texte")
                        sphere()
                else:
                    largeur = hauteur/(2*pi)
                    print("le largeur de votre est le hauteur/(2*π) donc" +
                          str(hauteur) + "/(2*π) = " + str(largeur))
            else:
                largeur = sqrt(longueur/pi)
                print("le largeur de votre est le √(longueur/π) donc √(" + str(longueur) + "/π) = " + str(largeur))
        elif calcul == "longueur":
            print("Vous avez le \"largeur\" ou le \"volume\"?\n")
        elif calcul == "périmètre":
            print("Vous avez le \"largeur\" ou le \"volume\"?\n")
        else:
            print("erreur")
            while True:
                break
    else:
        print("Veuillez écrire correctement\nMerci !!!\n\n")


def cube():
    print("que voulez vous calculer?\nlargeur, longueur, volume, hauteur")
    calcul = input("")
    largeur = None
    longueur = None
    volume = None
    hauteur = None
    if calcul == "volume" or calcul == "largeur" or calcul == "longueur" or calcul == "hauteur":
        print("rentré les valeurs que vous avez.\n Merci de mettre \"0\" si vous n'avez pas cette mesure")
        print("largeur : ")
        largeur = int(input())
        print("longueur : ")
        longueur = int(input())
        print("volume : ")
        volume = int(input())
        print("hauteur : ")
        hauteur = int(input())
        if calcul == "volume":
            if str(longueur) != "0":
                if str(hauteur) != "0":
                    if str(largeur) != "0":
                        volume = largeur * longueur * hauteur
                        print("le volume de votre cercle est égale à largeur * longueur * hauteur donc"
                              + str(largeur) + " * " + str(longueur) + " * " + str(hauteur) + " = " + str(volume))
                    else:
                        print("Vous n'avez pas donné de valeur ou"
                              " alors vous n'avez pas écris correctement "
                              "bien évidemment mettre 0 dans rayon puisque "
                              "vous calculez le rayon")
                        cube()
                else:
                    rayon = hauteur/(2*pi)
                    print("le rayon de votre est le hauteur/(2*π) donc" +
                          str(hauteur) + "/(2*π) = " + str(volume))
            else:
                rayon = sqrt(longueur/pi)
                print("le rayon de votre est le √(longueur/π) donc √(" +
                      str(longueur) + "/π) = " + str(volume))
        elif calcul == "largeur":
            if str(longueur) == "0":
                if str(hauteur) == "0":
                    if str(volume) != "0":
                        largeur = volume*2
                        print("le largeur de votre cercle est le diamètre/2 donc"
                           + str(volume) + "/2 = " + str(largeur))
                    else:
                        print("Vous n'avez pas donné de valeur ou"
                              " alors vous n'avez pas écris correctement \n"
                                "bien évidemment mettre 0 dans diamètre puisque "
                              "vous calculez le rayon\n\nVous êtes prié de me "
                              "donner des chiffres ou nombres et non du texte")
                        cube()
                else:
                    largeur = hauteur/(2*pi)
                    print("le largeur de votre est le hauteur/(2*π) donc" +
                          str(hauteur) + "/(2*π) = " + str(largeur))
            else:
                largeur = sqrt(longueur/pi)
                print("le largeur de votre est le √(longueur/π) donc √(" + str(longueur) + "/π) = " + str(largeur))
        elif calcul == "longueur":
            print("Vous avez le \"largeur\" ou le \"volume\"?\n")
        elif calcul == "périmètre":
            print("Vous avez le \"largeur\" ou le \"volume\"?\n")
        else:
            print("erreur")
            while True:
                break
    else:
        print("Veuillez écrire correctement\nMerci !!!\n\n")


def rectangle3d():
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