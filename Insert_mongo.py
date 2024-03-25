
from pymongo.server_api import ServerApi

uri = "mongodb+srv://SuperAdmin:SuperAdmin123@interfaccia.zekgqcl.mongodb.net/?retryWrites=true&w=majority&appName=Interfaccia"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db=client["Interfaccia"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def insert_mappa(id, lunghezza,larghezza, prezzo):
    collection=db["Mappa"]
    doc={"id":id,"lunghezza":lunghezza,"larghezza":larghezza,"prezzo":prezzo}
    result=collection.insert_one(doc)
    if result.acknowledged:
        print("Documento inserito correttamente")
    else:
        print("Errore durante l'inserimento del documento")


def insert_casa(id, lunghezza, larghezza, piani, appartamenti, tipologia, prezzo ):
    collection=db["Casa"]
    doc={"id":id,"lunghezza":lunghezza,"larghezza":larghezza,"piani":piani,"appartamenti":appartamenti,"tipologia":tipologia,"prezzo":prezzo}
    result=collection.insert_one(doc)
    if result.acknowledged:
        print("Documento inserito correttamente")
    else:
        print("Errore durante l'inserimento del documento")


def insert_negozio(id, lunghezza, larghezza, nome_attività, servizi, prezzo):
    collection=db["Casa"]
    doc={"id":id,"lunghezza":lunghezza,"larghezza":larghezza,"nome_attivita":nome_attività,"servizi":servizi,"prezzo":prezzo}
    result=collection.insert_one(doc)
    if result.acknowledged:
        print("Documento inserito correttamente")
    else:
        print("Errore durante l'inserimento del documento")


def insert_EdificioP(id, lunghezza, larghezza, funzione, tipologia, prezzo, id_negozio ):
    collection=db["EdificioPubblico"]
    doc={"id":id,"lunghezza":lunghezza,"larghezza":larghezza,"funzione":funzione,"tipologia":tipologia,"prezzo":prezzo,"id_negozio":id_negozio}
    result=collection.insert_one(doc)
    if result.acknowledged:
        print("Documento inserito correttamente")
    else:
        print("Errore durante l'inserimento del documento")

def SpazioPubblico(id, lunghezza, larghezza, funzione, prezzo):
    collection=db["EdificioPubblico"]
    doc={"id":id,"lunghezza":lunghezza,"larghezza":larghezza,"funzione":funzione,"prezzo":prezzo}
    result=collection.insert_one(doc)
    if result.acknowledged:
        print("Documento inserito correttamente")
    else:
        print("Errore durante l'inserimento del documento")