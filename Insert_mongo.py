from pymongo import MongoClient
from pymongo.server_api import ServerApi


class TesterMongo:
    def constructor(self):
        uri = "mongodb+srv://SuperAdmin:SuperAdmin123@interfaccia.zekgqcl.mongodb.net/?retryWrites=true&w=majority&appName=Interfaccia"
        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db=self.client["Interfaccia"]
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def insert_mappa(self,id, lunghezza,larghezza, prezzo):
        collection=self.db["Mappa"]
        doc={"id":id,"lunghezza":lunghezza,"larghezza":larghezza,"prezzo":prezzo}
        result=collection.insert_one(doc)
        if result.acknowledged:
            print("Documento inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento")


    def insert_casa(self,id, lunghezza, larghezza, piani, appartamenti, tipologia, prezzo ):
        collection=self.db["Casa"]
        doc={"id":id,"lunghezza":lunghezza,"larghezza":larghezza,"piani":piani,"appartamenti":appartamenti,"tipologia":tipologia,"prezzo":prezzo}
        result=collection.insert_one(doc)
        if result.acknowledged:
            print("Documento inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento")


    def insert_negozio(self,id, lunghezza, larghezza, nome_attivita, servizi, prezzo):
        collection=self.db["Casa"]
        doc={"id":id,"lunghezza":lunghezza,"larghezza":larghezza,"nome_attività":nome_attivita,"servizi":servizi,"prezzo":prezzo}
        result=collection.insert_one(doc)
        if result.acknowledged:
            print("Documento inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento")


    def insert_EdificioP(self,id, lunghezza, larghezza, funzione, tipologia, prezzo, id_negozio ):
        collection=self.db["EdificioPubblico"]
        doc={"id":id,"lunghezza":lunghezza,"larghezza":larghezza,"funzione":funzione,"tipologia":tipologia,"prezzo":prezzo,"id_negozio":id_negozio}
        result=collection.insert_one(doc)
        if result.acknowledged:
            print("Documento inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento")

    def insert_SpazioPubblico(self,id, lunghezza, larghezza, funzione, prezzo):
        collection=self.db["EdificioPubblico"]
        doc={"id":id,"lunghezza":lunghezza,"larghezza":larghezza,"funzione":funzione,"prezzo":prezzo}
        result=collection.insert_one(doc)
        if result.acknowledged:
            print("Documento inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento")

tm=TesterMongo()
tm.insert_negozio("0001","204","205","negozio1","vendita","15")
