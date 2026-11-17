import re

def dimension(a):
    if a == 0:
        while True:
            print("quel est la dimension?\n"
                  "femtomètre soit 10^-15 mètre \"f\", picomètre soit 10^-12 mètre \"p\", nanomètre soit 10^-9 mètre \"n\" micromètre soit 10^-6 mètre \"µ\""
                  ", millimètre soit 10^-3 mètre \"m\", centimètre soit 10^-2 mètre \"c\", décimètre soit 10^-1 mètre \"d\", mètre \"m\""
                  ", décamètre soit 10^1 mètre \"da\", hectomètre soit 10^2 mètre \"h\", kilomètre soit 10^3 mètre \"k\", "
                  "mégamètre soit 10^6 mètre \"M\", gigamètre soit 10^9 mètre \"G\" ou téramètre soit 10^12 mètre \"T\""
                  "\n\nVos mesures seront automatiquement convertis en mètre")
            dimensions = input("")
            if re.search(r"^(f|p|n|µ|m|c|d|da|h|k|M|G|T)m|m$", dimensions):
                if dimensions == "fm":
                    verif(0, dimensions)
                    break
                elif dimensions == "pm":
                    verif(0, dimensions)
                    break
                elif dimensions == "nm":
                    verif(0, dimensions)
                    break
                elif dimensions == "µm":
                    verif(0, dimensions)
                    break
                elif dimensions == "mm":
                    verif(0, dimensions)
                    break
                elif dimensions == "cm":
                    verif(0, dimensions)
                    break
                elif dimensions == "dm":
                    verif(0, dimensions)
                    break
                elif dimensions == "m":
                    verif(0, dimensions)
                    break
                elif dimensions == "dam":
                    verif(0, dimensions)
                    break
                elif dimensions == "hm":
                    verif(0, dimensions)
                    break
                elif dimensions == "km":
                    verif(0, dimensions)
                    break
                elif dimensions == "Mm":
                    verif(0, dimensions)
                    break
                elif dimensions == "Gm":
                    verif(0, dimensions)
                    break
                elif dimensions == "Tm":
                    verif(0, dimensions)
                    break
                else:
                    print("erreur")
                    break
            else:
                print("Veuillez écrire correctement\nMerci !!!\n\n")


def verif(chiffre, dimensions):
    if chiffre == 0:
        while True:
            print("êtes-vous sûr que c'est en " + dimensions + "?\n\"oui\" ou \"non\"")
            choix = input()
            if choix == "oui" or choix == "non":
                if choix == "oui":
                    if dimensions == "fm":
                        print("Femtomètre soit 10^-15 mètre")
                        break
                    elif dimensions == "pm":
                        print("Picomètre soit 10^-12 mètre")
                        break
                    elif dimensions == "nm":
                        print("Nanomètre soit 10^-9 mètre")
                        break
                    elif dimensions == "µm":
                        print("Micromètre soit 10^-6 mètre")
                        break
                    elif dimensions == "mm":
                        print("Millimètre soit 10^-3 mètre")
                        break
                    elif dimensions == "cm":
                        print("Centimètre soit 10^-2 mètre")
                        break
                    elif dimensions == "dm":
                        print("Décimètre soit 10^-1 mètre")
                        break
                    elif dimensions == "m":
                        print("Mètre")
                        break
                    elif dimensions == "dam":
                        print("Décamètre soit 10^1 mètre")
                        break
                    elif dimensions == "hm":
                        print("Hectomètre soit 10^2 mètre")
                        break
                    elif dimensions == "km":
                        print("Kilomètre soit 10^3 mètre")
                        break
                    elif dimensions == "Mm":
                        print("Mégamètre soit 10^6 mètre")
                        break
                    elif dimensions == "Gm":
                        print("Gigamètre soit 10^9 mètre")
                        break
                    elif dimensions == "Tm":
                        print("Téramètre soit 10^12 mètre")
                        break
                    else:
                        print("erreur")
                        break
                elif choix == "non":
                    print("veuillez resélectionné")
                    dimension(0)
                else:
                    print("erreur")
                    break
            else:
                print("Veuillez écrire correctement\nMerci !!!\n\n")