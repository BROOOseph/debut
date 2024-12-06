nombre1 = input("Entrez un nombre entier")
nombre2 = input("Entrez un nombre entier")

if not nombre1.isnumeric() or not nombre2.isnumeric():
    print("Ce ne sont pas des nombre entiers")
    raise SystemExit("Fin du programme")

nombre1 = int(nombre1)
nombre2 = int(nombre2)


operation = input("Entrez l'opération souhaité['+','-','*' ou '/']:")

if operation not in ["+", "-", "*", "/"]:
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    raise SystemExit("Fin du programme")



if operation == "+":
    resultat = nombre1 + nombre2

elif operation == "-":
    resultat = nombre1 - nombre2

elif operation == "*":
    resultat = nombre1 * nombre2

elif operation == "/":
    resultat = nombre1 / nombre2
    if nombre2 == 0:
        print("Erreur : impossible de diviser par zéro.")
        raise SystemExit("Fin du programme")



print(f"Le résultat est {resultat}")

