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

    def insert_simulation(self,owner,name,creation,ground,lights,fog,antialiasing,quality,x,y,id_buildings,xp,zp,xs,zs,ys,panels):
        db=self.get_db()
        collection=db["Simulation"]
        doc={"Owner":owner,"Name":name,"Creation":creation,"Graphics":{"Ground":ground,"Lights":lights,"Fog":fog,"Antialiasing":antialiasing,"Quality":quality},"Map":{"Grid":{"x":x,"y":y},"Buildings":{"_id":id_buildings,"Position":{"x":xp,"z":zp},"Size":{"x":xs,"z":zs,"y":ys}},"Panels":panels}}
        result=collection.insert_one(doc)
        if result.acknowledged:
            print("Documento Simulazione inserito correttamente")
        else:
            print("Errore durante l'inserimento del documento Simulazione")

# Example usage
tm = TesterMongo()
tm.insert_simulation("iooooooo","simulazione-loca","2024/04/18","false","true","fog","false","lowPower",20,20,2,6,8,9,9,5,3)
