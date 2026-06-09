from database import salvaDati

def creaScheda(dati, username):
    print(f"ok {username}, iniziamo a preparare la tua scheda!")

    inputUtente = input("Quali giorni vorresti allenarti? ").lower()
    giorni = inputUtente.replace(",", " ").split()

    dati[username]["giorni"] = {}

    for giorno in giorni:
        dati[username]["giorni"][giorno] = {}
        muscoli = input(f"quali muscoli alleni {giorno}? ").lower().split()
        dati[username]["giorni"][giorno]["muscoli"] = {}

        for muscolo in muscoli:
            dati[username]["giorni"][giorno]["muscoli"][muscolo] = {}
            esercizi = input(f"Esercizi per {muscolo}: ").lower().replace(",", " ").split()

            dati[username]["giorni"][giorno]["muscoli"][muscolo]["esercizi"] = esercizi

    salvaDati(dati)

def modificaScheda(dati, username):
    for giorno in dati[username]["giorni"]:
        print("-", giorno)

    giorno = input("Quale giorno vuoi modificare? ").lower()

    if giorno not in dati[username]["giorni"]:
        print("Giorno non trovato")
        return

    muscolo = input("Quale muscolo vuoi modificare? ").lower()
    
    if muscolo not in dati[username]["giorni"][giorno]["muscoli"]:
        print("Muscolo non trovato")
        return

    nuoviEsercizi = input(
        f"Nuovi esercizi per {muscolo}: "
    ).lower().replace(",", " ").split()

    dati[username]["giorni"][giorno]["muscoli"][muscolo]["esercizi"] = nuoviEsercizi

    salvaDati(dati)

    print("Scheda aggiornata!")


def aggiungiEsercizio(dati, username):

    giorno = input("In quale giorno? ").lower()

    if giorno not in dati[username]["giorni"]:
        print("Giorno non trovato")
        return

    muscolo = input("Per quale muscolo? ").lower()

    if muscolo not in dati[username]["giorni"][giorno]["muscoli"]:
        print("Muscolo non trovato")
        return

    nuoviEsercizi = input(
        "Quali esercizi vuoi aggiungere? "
    ).lower().replace(",", " ").split()

    dati[username]["giorni"][giorno]["muscoli"][muscolo]["esercizi"].extend(nuoviEsercizi)

    salvaDati(dati)

    print("Esercizi aggiunti!")

def aggiungiMuscolo(dati, username):


    giorno = input("In quale giorno? ").lower()

    if giorno not in dati[username]["giorni"]:
        print("Giorno non trovato")
        return

    nuoviMuscoli = input(
        "Quali muscoli vuoi aggiungere? "
    ).lower().replace(",", " ").split()

    for muscolo in nuoviMuscoli:

        if muscolo in dati[username]["giorni"][giorno]["muscoli"]:
            print(f"{muscolo} già esiste")
        else:
            dati[username]["giorni"][giorno]["muscoli"][muscolo] = {
                "esercizi": []
            }

    salvaDati(dati)

    print("Muscoli aggiunti!")

def aggiungiGiorno(dati, username):

    nuoviGiorni = input(
        "Quali giorni vuoi aggiungere? "
    ).lower().replace(",", " ").split()

    for giorno in nuoviGiorni:

        if giorno in dati[username]["giorni"]:
            print(f"{giorno} già esiste")
        else:
            dati[username]["giorni"][giorno] = {
                "muscoli": {}
            }

    salvaDati(dati)

    print("Giorni aggiunti!")


def visualizzaScheda(dati, username):
    for giorno in dati[username]["giorni"]:
        print(f"\n{giorno.upper()}")

        for muscolo in dati[username]["giorni"][giorno]["muscoli"]:
            print(f"\n  {muscolo.upper()}")

            for esercizio in dati[username]["giorni"][giorno]["muscoli"][muscolo]["esercizi"]:
                print(f"  -{esercizio}")

    print("\n")


def eliminaUtente(dati, username):
    del dati[username]
    salvaDati(dati)
    print("Utente eliminato")

def eliminaEsercizio(dati, username):

    giorno = input("Giorno: ").lower()
    muscolo = input("Muscolo: ").lower()

    eserciziDaEliminare = input(
        "Quali esercizi vuoi eliminare? "
    ).lower().replace(",", " ").split()

    for esercizio in eserciziDaEliminare:

        if esercizio in dati[username]["giorni"][giorno]["muscoli"][muscolo]["esercizi"]:

            dati[username]["giorni"][giorno]["muscoli"][muscolo]["esercizi"].remove(esercizio)

    salvaDati(dati)

    print("Esercizi eliminati!")

def eliminaMuscolo(dati, username):

    giorno = input("Giorno: ").lower()

    muscoliDaEliminare = input(
        "Quali muscoli vuoi eliminare? "
    ).lower().replace(",", " ").split()

    for muscolo in muscoliDaEliminare:

        if muscolo in dati[username]["giorni"][giorno]["muscoli"]:

            del dati[username]["giorni"][giorno]["muscoli"][muscolo]

    salvaDati(dati)

    print("Muscoli eliminati!")

def eliminaGiorno(dati, username):



    giorniDaEliminare = input(
        "Quali giorni vuoi eliminare? "
    ).lower().replace(",", " ").split()

    for giorno in giorniDaEliminare:

        if giorno in dati[username]["giorni"]:

            del dati[username]["giorni"][giorno]

    salvaDati(dati)

    print("Giorni eliminati!")

def eliminaScheda(dati, username):

    dati[username]["giorni"] = {}

    salvaDati(dati)

    print("Scheda eliminata!")


