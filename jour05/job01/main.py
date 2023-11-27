def info_user():
    try:
        name = input("Quel est ton nom? ")
        if not name:
            raise ValueError()
        else:
            print(f"hello {name}")
    
    except:
        print("Erreur: veuillez rentrer votre prenom")

info_user()