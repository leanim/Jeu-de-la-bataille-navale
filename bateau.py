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
                    grille[ligne][colonne + i] = "O"
                elif orientation == "vertical":
                    grille[ligne + i][colonne] = "O"
            break

def jouer(grille, bateaux):
    for bateau in bateaux:
        taille = int(bateau["taille"])
        print(f"Placez votre bateau: {bateau['nom']} ({bateau['taille']})")
        placement(grille, taille)
        afficher(grille)  # Afficher la grille après chaque placement

#Création des grilles pour deux joueurs
grilles = [grille() for _ in range(2)]

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

#Interraction 
for joueur in range(2):
    print(f"\nJoueur {joueur + 1}, placez votre bateau")
    jouer(grilles[joueur], bateaux)
    afficher(grilles[joueur])
