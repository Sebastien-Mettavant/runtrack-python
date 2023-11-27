def draw_tapis_diagonale_reverse(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == n - j:
                print('', end=' ')
            else:
                print('#', end=' ')
        print()

# Exemple d'utilisation avec n=10
draw_tapis_diagonale_reverse(10)
print("+--------+")
print("######### ")
print("########  ")
print("#######   ")
print("######    ")
print("#####     ")
print("####      ")
print("###       ")
print("##        ")
print("#         ")
print("+---------")

