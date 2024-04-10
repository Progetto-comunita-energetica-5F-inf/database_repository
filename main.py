from insert_mongo import *

class TestAppCLI:
    def main(self):
        tm = TesterMongo()               

        while menuMongo:
            c1=input("Premi: \n 1:Per inserire una Mappa \n 2:Per inserire una Casa \n 3:Per inserire un Negozio \n 4:Per inserire un EdificioPubblico \n 5:Per inserire uno SpazioPubblico")
            if c1==1:
                #id, lunghezza,larghezza, prezzo
                lunghezza = input("inserisci la lunghezza ")
                larghezza = input("inserisci la larghezza ")
                prezzo = input("inserisci il prezzo ")
                tm.insert_mappa(lunghezza, larghezza, prezzo)
                #gestisci creazione della mappa
            elif c1==2:
                #id, lunghezza, larghezza, piani, appartamenti, tipologia, prezzo
                lunghezza = input("inserisci la lunghezza ")
                larghezza = input("inserisci la larghezza ")
                appartamenti = input("inserisci l'appartamenti ")
                tipologia = input("inserisci la tipologia ")
                prezzo = input("inserisci il prezzo ")
                tm.insert_casa(lunghezza, larghezza, appartamenti, tipologia, prezzo)
                # gestisci creazione della casa
            elif c1==3:
                #id, lunghezza, larghezza, nome_attivita, servizi, prezzo
                lunghezza = input("inserisci la lunghezza ")
                larghezza = input("inserisci la larghezza ")
                nome_attivita = input("inserisci il nome_attivita ")
                servizi = input("inserisci il servizi ")
                prezzo = input("inserisci il prezzo ")
                tm.insert_negozio(lunghezza, larghezza, nome_attivita, servizi, prezzo)
                #gestisci creazione del negozio
            elif c1==4:
                #id, lunghezza, larghezza, funzione, tipologia, prezzo, id_negozio
                lunghezza = input("inserisci la lunghezza ")
                larghezza = input("inserisci la larghezza ")
                funzione = input("inserisci la funzionalità ")
                prezzo = input("inserisci il prezzo ")
                id_negozio = input("inserisci l'id del negozio ")
                tm.insert_EdificioP(lunghezza, larghezza, funzione, prezzo, id_negozio)
                # gestisci creazione dell EDP
            elif c1==5:
                #id, lunghezza, larghezza, funzione, prezzo
                lunghezza = input("inserisci la lunghezza ")
                larghezza = input("inserisci la larghezza ")
                funzione = input("inserisci la funzionalità ")
                prezzo = input("inserisci il prezzo ")
                tm.insert_SpazioPubblico(lunghezza, larghezza, funzione, prezzo)
                # gestisci creazione dell SP
            else:
                print("Errore nell'esecuzione della richiesta")
                r1 = input("Premi: \n 0: per uscire \n 1:Per continuare con una nuova richiesta")
                if r1 == 0:
                    menuMongo = False
                else:
                    menuMongo = True

TestAppCLI()