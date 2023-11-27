def decaler_caractere(caractere, decalage):
    if caractere.isalpha():
        # Appliquer le décalage en prenant en compte le dépassement
        offset = ord('A') if caractere.isupper() else ord('a')
        return chr((ord(caractere) - offset + decalage) % 26 + offset)
    else:
        # Si le caractère n'est pas une lettre, le laisser inchangé
        return caractere

def decaler_message_recursif(message, decalage):
    return "" if not message else decaler_caractere(message[0], decalage) + decaler_message_recursif(message[1:], decalage)

# Exemple d'utilisation
message_original = "xyz"
decalage = 3
message_decale = decaler_message_recursif(message_original, decalage)
print(message_decale)
