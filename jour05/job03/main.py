def draw_rectangle(height=0):
    if height == 0:
        print(" ⚠️   ERREUR : Veuillez entrer une hauteur non nulle.")
    else:
        print(f"hauteur : {height} \n")

        for i in range(height):

            if i == height - 1:
                print('/' + '_' * (2 * i) + '\\')
            else:
                print(' ' * (height - i - 1) + '/' + ' ' * (2 * i) + '\\')

# Exemple d'utilisation avec une hauteur de 5
draw_rectangle(5)

