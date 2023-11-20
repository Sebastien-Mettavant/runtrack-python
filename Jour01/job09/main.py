produit = "jus de mangue"
prix_unitaire = 1000
quantite_en_stock = 2000

print("Information du produit :")
print("Nom du produit :", produit)
print("Le prix du produit :", prix_unitaire)
print("Quantité du produit en stock :", quantite_en_stock)

achat_produit = int(input("Combien en voulez-vous ? "))

quantite_en_stock -= achat_produit

print("Quantité du produit en stock :", quantite_en_stock)

prix_unitaire *= 1.10

print("\nInformation du produit :")
print("Nom du produit :", produit)
print("Le prix du produit :", prix_unitaire)
print("Quantité du produit en stock :", quantite_en_stock)