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

    def insert_mappa(self, x, z, case, negozi, edifici_pubblici, spazi_pubblici,  prezzo):
        db = self.get_db()
        collection = db["Mappa"]
        doc = {"dimensioni": {"x": x, "z": z}, "edifici": {"case": case, "negozi": negozi, "edifici_pubblici": edifici_pubblici, "spazi_pubblici": spazi_pubblici}, "prezzo": prezzo}
        result = collection.insert_one(doc)
        if result.acknowledged:
            print("Documento Mappa inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento Mappa")

    def insert_casa(self, x, z, lunghezza, larghezza, altezza, piani, appartamenti, tipologia, pannello, prezzo):
        db = self.get_db()
        collection = db["Casa"]
        doc = {"posizione": {"x": x, "z": z}, "dimensioni": {"lunghezza": lunghezza, "larghezza": larghezza, "altezza": altezza}, "piani": piani,
                "appartamenti": appartamenti, "tipologia": tipologia, "pannello": pannello, "prezzo": prezzo}
        result = collection.insert_one(doc)
        if result.acknowledged:
            print("Documento Casa inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento Casa")

    def insert_negozio(self, x, z, lunghezza, larghezza, altezza, nome_attivita, servizi, pannello, prezzo):
            collection = self.db["Negozio"]
            doc = {"posizione": {"x": x, "z": z}, "dimensioni": {"lunghezza": lunghezza, "larghezza": larghezza, "altezza": altezza},
                    "nome_attività": nome_attivita, "servizi": servizi, "pannello": pannello, "prezzo": prezzo}
            result = collection.insert_one(doc)
            if result.acknowledged:
                print("Documento Negozio inserito correttamente")
                return result.inserted_id  # Restituisci l'ID del negozio appena inserito
            else:
                print("Errore durante l'inserimento del documento Negozio")
                return None

    def insert_EdificioP(self, x, z, lunghezza, larghezza, altezza, funzione, tipologia, pannello, prezzo):
        id_negozio = self.insert_negozio(lunghezza, larghezza, funzione, tipologia, prezzo)
        if id_negozio:
            collection = self.db["EdificioPubblico"]
            doc = {"posizione": {"x": x, "z": z}, "dimensioni": {"lunghezza": lunghezza, "larghezza": larghezza, "altezza": altezza}, "funzione": funzione,
                    "tipologia": tipologia, "pannello": pannello, "prezzo": prezzo, "id_negozio": id_negozio}
            result = collection.insert_one(doc)
            if result.acknowledged:
                print("Documento Edificio Pubblico inserito correttamente")
            else:
                print("Errore durante l'inserimento del documento Edificio Pubblico")
        else:
            print("Impossibile inserire l'Edificio Pubblico senza un ID negozio")

    def insert_SpazioPubblico(self, x, z, lunghezza, larghezza, altezza, funzione, pannello, prezzo):
        db = self.get_db()
        collection = db["SpazioPubblico"]
        doc = {"posizione": {"x": x, "z": z}, "dimensioni": {"lunghezza": lunghezza, "larghezza": larghezza, "altezza": altezza}, "funzione": funzione,  "pannello": pannello, "prezzo": prezzo}
        result = collection.insert_one(doc)
        if result.acknowledged:
            print("Documento Spazio Pubblico inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento Spazio Pubblico")

# Example usage
tm = TesterMongo()
tm.insert_casa(1, 2, 100, 200, 300, 10, 20, "villa", True, 1000)
