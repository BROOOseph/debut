print("Bienvenue sur le jeu des allumettes !")

nombre_actuel_allumettes = nombre_total_allumettes_ = int(input("Veuillez saisir le nombre d'allumettes que vous souhaitez voir dans le jeu :"))

retrait_allumettes = 0

joueur = 1

def tour_joueur(joueur):
    if joueur

def afficher_nombre_allumettes_restantes(nombre_actuel_allumettes):
    print("Il reste",nombre_actuel_allumettes,"allumettes")

def tour_joueur(nombre_actuel_allumettes,retrait_allumettes):
    if joueur == 1:
        print("Au tour du joueur 1")



    if nombre_actuel_allumettes == 2:
        retrait_allumettes = int(input("Voulez vous retirer 2 allumettes"))

    if nombre_actuel_allumettes > 3:
        retrait_allumettes = int(input("Combien voulez vous retirer d'allumettes ?"))

    while retrait_allumettes > 3 or retrait_allumettes < 1:
        retrait_allumettes = int(input("Veuillez saisir un chiffre entre 1 et 3. Combien voulez vous retirer d'allumettes ?"))

    nombre_actuel_allumettes = nombre_actuel_allumettes - retrait_allumettes


    afficher_nombre_allumettes_restantes(nombre_actuel_allumettes)

    return nombre_actuel_allumettes

while nombre_actuel_allumettes > 1:
    nombre_actuel_allumettes = tour_joueur(nombre_actuel_allumettes,retrait_allumettes)

if nombre_actuel_allumettes == 0 or 1:
        print("Vous avez perdu !")

