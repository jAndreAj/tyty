import os

def main():
    print("Benvenuto in Replit!")

    # Funzionalità 1: Esecuzione di codice
    print("1. Esecuzione di codice")
    print("Eseguiamo una semplice operazione matematica: 5 + 3 =", 5 + 3)

    # Funzionalità 2: Interazione con l'utente
    print("\n2. Interazione con l'utente")
    nome = input("Come ti chiami? ")
    print(f"Ciao, {nome}!")

    # Funzionalità 3: Creazione e gestione di file
    print("\n3. Creazione e gestione di file")
    with open("esempio.txt", "w") as file:
        file.write(f"Ciao, {nome}! Questo è un file creato su Replit.\n")

    print("Il file 'esempio.txt' è stato creato.")

    # Funzionalità 4: Lettura del file appena creato
    print("\n4. Lettura del file")
    with open("esempio.txt", "r") as file:
        contenuto = file.read()
        print("Contenuto del file:")
        print(contenuto)

if __name__ == "__main__":
    main()
