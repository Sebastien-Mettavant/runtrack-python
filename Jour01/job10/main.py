montant_initial = 42000
taux_de_rendement_annuel =20
gain_annuel = montant_initial*(taux_de_rendement_annuel/100)
print("le rendement annuel est de :", gain_annuel)

montant_initial += 5000
taux_de_rendement_annuel += 2
nouveau_gain_annuel = montant_initial*(taux_de_rendement_annuel/100)
print("le rendement annuel est de :", nouveau_gain_annuel)

retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_de_rendement_annuel -= 1

montant_final = montant_initial + nouveau_gain_annuel
print("Montant final est de :", montant_final)