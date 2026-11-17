from forme2d import *
from stop import stop
from vérif_dimension import *


def deux():
    while True:
        print("\nBienvenue dans le menu des calculs en 2 dimensions\nChoisissez votre forme\n"
              "cercle, triangle, rectangle, carré, losange, parallélogramme, polygone régulier"
              "\nTaper dimension pour corriger vos dimension"
              "\n\nstop pour arrêter le programme ou pour revenir au menu central")
        forme = input("")
        if forme == "cercle" or forme == "triangle" or forme == "rectangle" or \
                forme == "carré" or forme == "losange" or forme == "parallélogramme" or \
                forme == "polygone régulier" or forme == "dimension":
            if forme == "cercle":
                cercle()
            elif forme == "triangle":
                triangle()
            elif forme == "rectangle":
                rectangle()
            elif forme == "carré":
                carre()
            elif forme == "losange":
                losange()
            elif forme == "parallélogramme":
                parallelogramme()
            elif forme == "polygone régulier":
                polygone_regulier()
            elif forme == "dimension":
                dimension(0)
            else:
                print("erreur")
        elif forme == "stop":
            print("Voulez-vous arréter le programme ou revenir au menu central?"
                  "\narret ou menu")
            choix = input("")
            if choix == "arret":
                stop(1)
        else:
            print("Veuillez écrire correctement\nMerci !!!\n\n")