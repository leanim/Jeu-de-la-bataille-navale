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
afficher(grille)  
