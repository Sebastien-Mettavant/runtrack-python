number_extractions = (26, 37, 88)
number_total = 100

def generate_numbers():
    result = []  # On initialise une liste vide appelée "result" qui va stocker les nombres générés ||exemple    ( = [] <--- )||
    while sum(result) < number_total:  # On continue à ajouter des éléments à la liste tant que la somme est inférieure à "number_total" La fonction sum() en Python est utilisée pour calculer la somme des éléments dans une séquence, telle qu'une liste, un (tuple)=En Python, un tuple est une structure de données similaire à une liste, mais avec une différence clé : les tuples sont immuables, ce qui signifie qu'une fois qu'ils sont créés, leurs éléments ne peuvent pas être modifiés, ajoutés ni supprimés. Les tuples sont définis en utilisant des parenthèses ().    ou un autre itérable. Voici un exemple simple d'utilisation de la fonction sum() :
        result.extend(number_extractions)  # On ajoute tous les éléments de "number_extractions" à la liste "result"   En résumé, la méthode extend() est une façon pratique d'ajouter les éléments d'un iterable à la fin d'une liste existante en modifiant la liste d'origine.
    result = result[:number_total]  # On tronque la liste pour s'assurer qu'elle a exactement "number_total" d'éléments
    return result  # On renvoie la liste résultante

result = generate_numbers()  # On appelle la fonction et on assigne le résultat à la variable "result" L'appel à la fonction generate_numbers() avec les valeurs spécifiées de number_extractions et number_total générera une liste qui répond aux critères définis.
print(result , number_total)  # On imprime la liste résultante

