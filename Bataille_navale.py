#Création d'une grille de jeu 10x10
def cgrille():
    return [["    " for _ in range(11)] for _ in range(11)]

#Remplissage de la grille avec les lettres et les chiffres
def remplir(grille):
    for i in range(1, 11):
        grille[i][0] = f"{i:<4}" #Remplir les lignes (1-10)
    for o in range(1, 11):
        grille[0][o] = f"{chr(64 + o):<4}" #Remplir les colonnes (A-J)

#Affichage de la grille
def afficher(grille):
    print("+" + "----+" * 11)
    for ligne in grille:
        print("|" + "|".join(ligne) + "|")
        print("+" + "----+" * 11)

grille = cgrille()  
remplir(grille)          

#Vérifier le placement des bateaux sur la grille
def verification(grille, taille, ligne, colonne, orientation):
    if orientation == "horizontal":
        if colonne + taille > 10:
            print("Placement hors des limites de la grille? ")
            return False
        for i in range(taille):
            if grille[ligne][colonne + i] != "    ":
                print("Placement sur un autre bateau")
                return False
    elif orientation == "vertical":
        if ligne + taille > 10:
            ("Placement hors des limites de la grille")
            return False
        for i in range(taille):
            if grille[ligne + i][colonne] != "    ":
                print("Placement sur un autre bateau")
                return False
    return True

#Placer les bateaux sur la grille
def placement(grille, taille):
    while True:
        orientation = input("Entrez l'orientation (horizontal ou vertical): ")
        colonne = input("Entrez (A-J): ")
        ligne = int(input("Entrez (1-10): "))

        colonne = ord(colonne) - ord("A") + 1

        if verification(grille, taille, ligne, colonne, orientation):
            for i in range(taille):
                if orientation == "horizontal":
                    grille[ligne][colonne + i] = " o  "
                elif orientation == "vertical":
                    grille[ligne + i][colonne] = " o  "
            break

def jouer(grille, bateaux):
    for bateau in bateaux:
        taille = int(bateau["taille"])
        print(f"Placez votre bateau: {bateau['nom']} ({bateau['taille']})")
        placement(grille, taille)
        afficher(grille) 

#Création des grilles pour deux joueurs
grilles = [cgrille() for _ in range(2)]

#Remplissage de la grille pour les deux joueurs
for grille in grilles:
    remplir(grille)

#Afficher les grilles
for joueur in range(2):
    print(f"\nGrille du Joueur {joueur + 1}:")
    afficher(grilles[joueur])

bateaux = [
    {"nom": "Porte-avions", "taille": "5"},
    {"nom": "Croiseur", "taille": "4"},
    {"nom": "Contre-torpilleur", "taille": "3"},
    {"nom": "Sous-marin", "taille": "3"},
    {"nom": "Torpilleur", "taille": "2"}
]

#Attaquer la grille de l'ennemi
def attaquer(grilleennemi):
    while True:
        colonne=int(input("Entrez la ligne à attaquer (1-10):"))
        ligne=input("Entrez la colonne à attaquer (A-J):")

        ligne= ord(ligne) - ord("A") + 1

        colonne2=colonne
        ligne2=ligne
        colonne=ligne2
        ligne=colonne2

        if 1<=ligne<=10 and 1<= colonne<=10:
            if grilleennemi[ligne][colonne]== " o  ":
                 print("Touché")
                 grilleennemi[ligne][colonne]= " X  "
            elif grilleennemi[ligne][colonne]==" X  ":
                 print("Cette case a déjà été attaqué, veuilez viser une autre case")
            elif grilleennemi[ligne][colonne]==" T  ":
                 print("Cette case a déjà été attaqué, veuilez viser une autre case")
            else:
                 print("Coulé")
                 grilleennemi[ligne][colonne]=" T  "
            break

#Interraction 
for joueur in range(2):
    print(f"\nJoueur {joueur + 1}, placez votre bateau")
    jouer(grilles[joueur], bateaux)
    afficher(grilles[joueur])

#Attaque du joueur
while True:
    for joueur in range(2):
     print(f"\nJoueur{joueur+1}, Attaquez l'ennemi") 
     attaquer(grilles[(joueur + 1) % 2])
     afficher(grilles[(joueur + 1) % 2])
           
