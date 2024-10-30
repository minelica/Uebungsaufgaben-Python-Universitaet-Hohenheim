# Übungsaufgabe 1

def calculate_grade(n1, n2, n3):
    # Berechnung des Durchschnitts
    average = (n1 + n2 + n3) / 3

    # Umrechnung des Durchschnitts in eine Schulnote
    if average <= 1.15:
        return 1.0
    elif average <= 1.5:
        return 1.3
    elif average <= 1.85:
        return 1.7
    elif average <= 2.15:
        return 2.0
    elif average <= 2.5:
        return 2.3
    elif average <= 2.85:
        return 2.7
    elif average <= 3.15:
        return 3.0
    elif average <= 3.5:
        return 3.3
    elif average <= 3.85:
        return 3.7
    elif average <= 4.15:
        return 4.0
    else:
        return 5.0  # Noten schlechter als 4 werden zu 5.0


def main():
    # Eingabe der drei Noten
    try:
        note1 = int(input("Bitte die erste Note eingeben: "))
        note2 = int(input("Bitte die zweite Note eingeben: "))
        note3 = int(input("Bitte die dritte Note eingeben: "))

        # Überprüfung der Gültigkeit der Noten
        if note1 not in [1, 2, 3, 4, 5, 6] or note2 not in [1, 2, 3, 4, 5, 6] or note3 not in [1, 2, 3, 4, 5, 6]:
            print("Ungültige Eingabe. Die Noten müssen zwischen 1 und 6 liegen.")
            return

        # Aufruf der Funktion und Ausgabe des Ergebnisses
        result = calculate_grade(note1, note2, note3)
        print(f"Die berechnete Schulnote ist: {result:.1f}")

    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie nur ganze Zahlen ein.")


# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
