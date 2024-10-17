#Attaquer la grille de l'ennemi
def attaquer(grilleennemi):
    while True:
        colonne=input("Entrez la colonne à attaquer (A-J)")
        ligne=int(input("Entrez la ligne à attaquer (1-10)"))
        colonne= ord(colonne) - ord("A") 

        if 0<=ligne<10 and 0 <= colonne<10:
            if grilleennemi[ligne][colonne]=="O":
             print("Touché")
            grilleennemi[ligne][colonne]="X"
        elif grilleennemi[ligne][colonne]=="X":
            print("Cette case a déjà été attaqué, veuilez viser une autre case")
        elif grilleennemi[ligne][colonne]=="T":
            print("Cette case a déjà été attaqué, veuilez viser une autre case")

        else:
            print("Coulé")
            grilleennemi[colonne][ligne]="T"
            break
            
            
#Attaque du joueur
for joueur in range(2):
    ennemi=(joueur+1)%2
    print(f"\nJoueur{joueur+1}, Attaquez l'ennemi")         
