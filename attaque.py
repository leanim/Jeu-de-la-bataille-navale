#Attaquer la grille de l'ennemi
def attaquer(grilleennemi):
    colonne=input("Entrez la colonne à attaquer (A-J)")
    ligne=int(input("Entrez la ligne à attaquer (1-10)"))
    colonne= ord(colonne) - ord("A") 

    if 0<=ligne<10 and 0 <= colonne<10:
        if grilleennemi[ligne][colonne]=="O":
            print("Touché")
            grilleennemi[ligne][colonne]="X"
        else:
            print("Raté")
            grilleennemi[colonne][ligne]="T"
            
#Attaque du joueur
for joueur in range(2):
    ennemi=(joueur+1)%2
    print(f"\nJoueur{joueur+1}, Attaquez l'ennemi")         
