def draw_rectangle(width=0, height=0):
    if width == 0 or height == 0:
        print(" ⚠️   ERREUR : Veuillez entrer une largeur et une hauteur non nulles.")
    else:
        print(f"largeur : {width}")
        print(f"hauteur : {height}")

        print('|' + '-' * (width - 2) + '|')
        for _ in range(height - 2):
            print('|' + ' ' * (width - 2) + '|')
        print('|' + '-' * (width - 2) + '|')

# Exemple d'utilisation avec une largeur de 5 et une hauteur de 3
draw_rectangle(5, 3)


draw_rectangle(10, 3)