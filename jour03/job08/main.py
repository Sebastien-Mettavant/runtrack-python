def chr(langage):
    if langage == "javascript":
        return "tu es un développeur web"
    elif langage == "python":
        return "tu es un développeur IA"
    elif langage == "java":
        return "tu es un développeur logiciel"
    else:
        return "Langage non reconnu"

# Exemple d'appel de la fonction
langage_utilisateur = "javascript"#etc......etc......
resultat = chr(langage_utilisateur)
print(resultat)
