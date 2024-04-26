def mot_a_sequence_numerique(mot):

    mot = mot.upper()

    sequence_numerique = []

    for lettre in mot:
        if 'A' <= lettre <= 'Z':
            sequence_numerique.append(str(ord(lettre) - ord('A') + 1))
    

    return ''.join(sequence_numerique)

mot = input("Entrez un mot: ")
sequence_numerique = mot_a_sequence_numerique(mot)
print(f"Le mot '{mot}' est représenté par la séquence: {sequence_numerique}")

def trouver_sequence_dans_pi(sequence, chemin_fichier):

    try:
        with open(chemin_fichier, 'r') as fichier:
            decimales_pi = fichier.read()
            position = decimales_pi.find(sequence)
            return position
    except FileNotFoundError:
        print("Fichier non trouvé.")
        return -1
    except Exception as e:
        print(f"Erreur: {e}")
        return -1

sequence = sequence_numerique
chemin_fichier = "milliardPi.txt"
position = trouver_sequence_dans_pi(sequence, chemin_fichier)

if position != -1:
    print(f"Le mot est trouvé à la décimale: {position}")
else:
    print("Séquence introuvable.")
