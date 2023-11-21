while True: #pour que la boucle soit en condition d
    try:
        N = int(input("Entrez un nombre entier positif (N) supérieur à zéro : ")) #(input) empeche la boucle de tourner a l infinie 
        if N > 0:
            break
        else:
            print("Veuillez entrer un nombre entier positif supérieur à zéro.")
    except ValueError:
        print("Veuillez entrer un nombre entier.")

# Affiche les tables de multiplication de 1 à N
for multiple in range(1, N + 1):
    print("------------------- MULTIPLES --------------------")
    print("La table de multiplication de  :", multiple, " est :")
    for i in range(1, 11):
        print(i, " x ", multiple, " = ", i * multiple)
