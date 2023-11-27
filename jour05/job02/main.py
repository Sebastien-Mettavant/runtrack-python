def rect(width=10, height=3):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('-' * width)
        else:
            print(f'|{" " * (width - 2)}|')

# Exemple d'utilisation avec les paramètres par défaut
rect()

