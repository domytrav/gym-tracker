from database import caricaDati, salvaDati
from workout import (
    creaScheda,
    aggiungiEsercizio,
    aggiungiMuscolo,
    aggiungiGiorno,
    eliminaUtente,
    eliminaEsercizio,
    eliminaMuscolo,
    eliminaGiorno,
    eliminaScheda,
    visualizzaScheda
)

dati = caricaDati()


def menu(dati, username):
    while True:
        scelta = input("Bentornato, cosa vuoi fare?\n1.creare una nuova scheda\n2.modificare scheda\n3.visualizza scheda\n4.esci\n5.elimina utente")

        if scelta == "1":
            creaScheda(dati,username)
        
        elif scelta == "2":
            sceltaModifica = input("cosa vuoi fare?\n1.aggiungere\n2.eliminare\n3.modificare la scheda")
            
            if sceltaModifica == "1":
                aggiunta = input("cosa vuoi aggiungere?\n1.esercizio\n2.muscolo\n3.giorno")

                if aggiunta == "1":
                    aggiungiEsercizio(dati,username)

                elif aggiunta == "2":
                    aggiungiMuscolo(dati,username)

                elif aggiunta == "3":
                    aggiungiGiorno(dati,username)

            elif sceltaModifica == "2":
                eliminazione = input("cosa vuoi eliminare?\n1.scheda\n2.esercizio\n3.muscolo\n4.giorno")

                if eliminazione == "1":
                    eliminaScheda(dati,username)

                elif eliminazione == "2":
                    eliminaEsercizio(dati,username)

                elif eliminazione == "3":
                    eliminaMuscolo(dati,username)

                elif eliminazione == "4":
                    eliminaGiorno(dati,username)

        
        elif scelta == "3":
            visualizzaScheda(dati,username)

        elif scelta == "4":
            break

        elif scelta == "5":
            eliminaUtente(dati,username)
            break


username = input("Benvenuto in GymTracker, inserisci il tuo username: ").lower()

if username not in dati:
    dati[username]= {}
    creaScheda(dati, username)
    menu(dati, username)
    
else:
    menu(dati, username)