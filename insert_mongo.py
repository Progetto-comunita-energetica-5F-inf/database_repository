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

    def insert_simulation(self,owner,creation,ground,lights,fog,antialiasing,quality,x,y,id_buildings,xp,zp,xs,zs,ys,panels):
        db=self.get_db()
        collection=db["Simulation"]
        doc={"owner":owner,creation:creation,"graphics":{"ground":ground,"lights":lights,"fog":fog,"antialiasing":antialiasing,"quality":quality},"map":{"grid":{"x":x,"y":y},"buildings":{"_id":id_buildings,"position":{"x":xp,"z":zp},"size":{"x":xs,"z":zs,"y":ys}},"panels":panels}}
        result=collection.insert_one(doc)
        if result.acknowledged:
            print("Documento Simulazione inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento Simulazione")

# Example usage
tm = TesterMongo()
tm.insert_simulation("Glober","2024/04/18","false","true","fog","false","lowPower",20,20,1,5,5,2,3,3,0)
