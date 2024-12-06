# Récupérer la saisie de l'utilisateur
nombres_input = input("Saisissez une liste de nombres séparés par des virgules: ")

# Séparer l'ensemble des nombres et les insérer dans une liste
liste_strings = nombres_input.split(",")
# Afficher la liste des nombres
print("Liste des nombres:", liste_strings)

# A ce stade liste est une liste de chaînes de caractères
# Convertir chaque élément de la liste en entier
liste_entiers = []
range(5)
for string in liste_strings:
    nombre_entier = int(string)
    liste_entiers.append(nombre_entier)


# Calculer la somme des nombres
somme = 0
for nombre in liste_entiers:
    somme += nombre

# Equivalent à:
# somme = sum(liste_entiers)

print("Somme des nombres:", somme)

# Effectuer la moyenne à l'aide de la somme des nombre
moyenne = somme / len(liste_entiers)

print("Moyenne des nombres:", moyenne)

# Trouver combien de nombres de la liste sont supérieurs à la moyenne
nombre_au_dessus_moyenne = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        nombre_au_dessus_moyenne += 1
print("Nombre de nombres supérieurs à la moyenne:", nombre_au_dessus_moyenne)

# Equivalent à:
# nombre_au_dessus_moyenne = 0
# idx = 0
# while idx < len(liste_entiers):
#     if liste_entiers[idx] > moyenne:
#         nombre_au_dessus_moyenne += 1
#     idx += 1
# Attention! Il est déconseillé d'utiliser la boucle while pour parcourir une liste.

print("Nombre de nombres pairs:", nombre_au_dessus_moyenne)