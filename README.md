from pymongo import MongoClient
from pymongo.server_api import ServerApi


class TesterMongo:
    client = None

    def __init__(self):
        uri = "mongodb+srv://ettoreedoardo:AmmMongo5F@interfaccia.zekgqcl.mongodb.net/?retryWrites=true&w=majority&appName=Interfaccia"
        TesterMongo.client = MongoClient(uri, server_api=ServerApi('1'))

    def get_db(self):
        if TesterMongo.client is None:
            self.__init__()
        return TesterMongo.client["Interfaccia"]

    def insert_mappa(self, lunghezza, larghezza, prezzo):
        db = self.get_db()
        collection = db["Mappa"]
        doc = {"lunghezza": lunghezza, "larghezza": larghezza, "prezzo": prezzo}
        result = collection.insert_one(doc)
        if result.acknowledged:
            print("Documento Mappa inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento Mappa")

    def insert_casa(self, lunghezza, larghezza, piani, appartamenti, tipologia, prezzo):
        db = self.get_db()
        collection = db["Casa"]
        doc = {"lunghezza": lunghezza, "larghezza": larghezza, "piani": piani,
                "appartamenti": appartamenti, "tipologia": tipologia, "prezzo": prezzo}
        result = collection.insert_one(doc)
        if result.acknowledged:
            print("Documento Casa inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento Casa")

    def insert_negozio(self, lunghezza, larghezza, nome_attivita, servizi, prezzo):
            collection = self.db["Negozio"]
            doc = {"lunghezza": lunghezza, "larghezza": larghezza,
                    "nome_attività": nome_attivita, "servizi": servizi, "prezzo": prezzo}
            result = collection.insert_one(doc)
            if result.acknowledged:
                print("Documento Negozio inserito correttamente")
                return result.inserted_id  # Restituisci l'ID del negozio appena inserito
            else:
                print("Errore durante l'inserimento del documento Negozio")
                return None

    def insert_EdificioP(self, lunghezza, larghezza, funzione, tipologia, prezzo):
        id_negozio = self.insert_negozio(lunghezza, larghezza, funzione, tipologia, prezzo)
        if id_negozio:
            collection = self.db["EdificioPubblico"]
            doc = {"lunghezza": lunghezza, "larghezza": larghezza, "funzione": funzione,
                    "tipologia": tipologia, "prezzo": prezzo, "id_negozio": id_negozio}
            result = collection.insert_one(doc)
            if result.acknowledged:
                print("Documento Edificio Pubblico inserito correttamente")
            else:
                print("Errore durante l'inserimento del documento Edificio Pubblico")
        else:
            print("Impossibile inserire l'Edificio Pubblico senza un ID negozio")

    def insert_SpazioPubblico(self, lunghezza, larghezza, funzione, prezzo):
        db = self.get_db()
        collection = db["SpazioPubblico"]
        doc = {"lunghezza": lunghezza, "larghezza": larghezza, "funzione": funzione, "prezzo": prezzo}
        result = collection.insert_one(doc)
        if result.acknowledged:
            print("Documento Spazio Pubblico inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento Spazio Pubblico")

# Example usage
tm = TesterMongo()
tm.insert_negozio("0002", "204", "205", "negozio1", "vendita", "15")
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
