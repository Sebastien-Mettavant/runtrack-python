def liste_fruits():
    fruits = ["pomme", "cerise", "orange", "melon"]
    if fruits[0] == "pomme":
        fruits[0] = "framboise"
    elif fruits[1] == "cerise":
        pass  # une instruction qui ne fait rien
    if fruits[2] == "orange":
        fruits[2] = "mangue"
    if   fruits[3] == "melon":
        pass  
    return fruits

ensemble_fruits = liste_fruits()
print(ensemble_fruits)






