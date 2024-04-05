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

    def insert_mappa(self, id, lunghezza, larghezza, prezzo):
        db = self.get_db()
        collection = db["Mappa"]
        doc = {"id": id, "lunghezza": lunghezza, "larghezza": larghezza, "prezzo": prezzo}
        result = collection.insert_one(doc)
        if result.acknowledged:
            print("Documento Mappa inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento Mappa")

    def insert_casa(self, id, lunghezza, larghezza, piani, appartamenti, tipologia, prezzo):
        db = self.get_db()
        collection = db["Casa"]
        doc = {"id": id, "lunghezza": lunghezza, "larghezza": larghezza, "piani": piani,
                "appartamenti": appartamenti, "tipologia": tipologia, "prezzo": prezzo}
        result = collection.insert_one(doc)
        if result.acknowledged:
            print("Documento Casa inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento Casa")

    def insert_negozio(self, id, lunghezza, larghezza, nome_attivita, servizi, prezzo):
        db = self.get_db()
        collection = db["Negozio"]
        doc = {"id": id, "lunghezza": lunghezza, "larghezza": larghezza,
                "nome_attività": nome_attivita, "servizi": servizi, "prezzo": prezzo}
        result = collection.insert_one(doc)
        if result.acknowledged:
            print("Documento Negozio inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento Negozio")

    def insert_EdificioP(self, id, lunghezza, larghezza, funzione, tipologia, prezzo, id_negozio):
        db = self.get_db()
        collection = db["EdificioPubblico"]
        doc = {"id": id, "lunghezza": lunghezza, "larghezza": larghezza, "funzione": funzione,
                "tipologia": tipologia, "prezzo": prezzo, "id_negozio": id_negozio}
        result = collection.insert_one(doc)
        if result.acknowledged:
            print("Documento Edificio Pubblico inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento Edificio Pubblico")

    def insert_SpazioPubblico(self, id, lunghezza, larghezza, funzione, prezzo):
        db = self.get_db()
        collection = db["SpazioPubblico"]
        doc = {"id": id, "lunghezza": lunghezza, "larghezza": larghezza, "funzione": funzione, "prezzo": prezzo}
        result = collection.insert_one(doc)
        if result.acknowledged:
            print("Documento Spazio Pubblico inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento Spazio Pubblico")

# Example usage
tm = TesterMongo()
tm.insert_negozio("0002", "204", "205", "negozio1", "vendita", "15")
