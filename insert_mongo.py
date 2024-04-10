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