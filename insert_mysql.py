import time

import pymssql

class TesterSql:

    def __init__(self,server="ce2.database.windows.net",user="SuperAdmin",password="CiaoCai123",database="CE"):
        try:
            self.server=server
            self.user=user
            self.password=password
            self.database=database
        except Exception as e:
            print(e)

    def connessione(self):
        try:
            TesterSql.conn = pymssql.connect(server=self.server, user=self.user,
                                               password=self.password, database=self.database)
            return TesterSql.conn
            print("\nConnessione effettuata !\n")
        except:
            print("\nConnessione NON riuscita!\n")
            return 0

    def disconnesione(self):
        try:
            TesterSql.conn.close()
            print("OK CHIUSURA CONNESSIONE DB")
        except:
            print("Attenzione KO CHIUSURA CONNESSIONE DB")


    def insert_Utente(self,username,nome,cognome,data,email,password,citta):
        c=self.connessione()
        query=f"INSERT INTO Utente(Username,Nome,Cognome,Data_nascita,Email,Psw,Citta) VALUES('{username}','{nome}','{cognome}','{data}','{email}','{password}','{citta}')"
        cursore=c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()

        
    def insert_Simulazione(self,Id_Simulazione, data_creazione, nome_città, UsernameUtente, MeteoDT):
        c=self.connessione()
        query=f"INSERT INTO Simulazione(Id_Simulazione, data_creazione, nome_città, Utente, Meteo) VALUES('{Id_Simulazione}','{data_creazione}','{nome_città}','{UsernameUtente}','{MeteoDT}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()



    def insert_Meteo(self,Datatime, pressione, temperatura, velocità_vento, direzione_vento, umidità, morfologia, precipitazioni, irraggiamento):
        c=self.connessione()
        query=f"INSERT INTO Meteo(Datatime, pressione, temperatura, velocità_vento, direzione_vento, umidità, morfologia, precipitazioni, irraggiamento) VALUES('{Datatime}','{pressione}','{temperatura}','{velocità_vento}','{umidità}','{morfologia}','{precipitazioni}','{irraggiamento}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()


    def insert_Batteria(self,Id_Serie, energia_stoccata, entrata, uscita, datatime, capacità_max, Id_sim):
        c=self.connessione()
        query=f"INSERT INTO Batteria(Id_Serie, energia_stoccata, entrata, uscita, datatime, capacità_max, Id_sim) VALUES('{Id_Serie}','{energia_stoccata}','{entrata}','{uscita}','{datatime}','{capacità_max}','{Id_sim}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()


    def insert_Compravendita(self,Id_Transazione, datatime, guadagno, quantità_venduta, spesa, quantità_comprata, IdBatteria):
        c=self.connessione()
        query=f"INSERT INTO Compravendita(Id_Transazione, datatime, guadagno, quantità_venduta, spesa, quantità_comprata, IdBatteria) VALUES('{Id_Transazione}','{datatime}','{guadagno}','{quantità_venduta}','{spesa}','{quantità_comprata}','{IdBatteria}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()




    def insert_Struttura(self,Id_Edificio, consumo, posizione, direzione, costo, numero_pannelli, numero_abitanti, piani, superficie, tipo, IdSimulazione, IdPannello, IdProduzione):
        c=self.connessione()
        query=f"INSERT INTO Struttura(Id_Edificio, consumo, posizione, direzione, costo, numero_pannelli, numero_abitanti, piani, superficie, tipo, IdSimulazione, IdPannello, IdProduzione) VALUES('{Id_Edificio}','{consumo}','{posizione}','{direzione}','{costo}','{numero_pannelli}','{numero_abitanti}','{piani}','{superficie}','{tipo}','{IdSimulazione}','{IdPannello}','{IdProduzione}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()


    def insert_TipoPannello(self,Id_pannello, Dimensione, Stato, Prezzo):

        c=self.connessione()
        time.sleep(10)
        query=f"INSERT INTO TipoPannello(Id_pannello, Dimensione, Stato, Prezzo) VALUES({Id_pannello},{Dimensione},{Stato},{Prezzo})"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()


    def insert_ProduzioneStorico(self,Id_produzione,Potenza,Datatime):
        c=self.connessione()
        query=f"INSERT INTO ProduzioneStorico(Id_produzione,Potenza,Datatime) VALUES({Id_produzione},'{Potenza}','{Datatime}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()



    def insert_CostoEnergiaStorico(self,Id_costo,Datatime,Costo_acquisto,Costo_vendita):
        c=self.connessione()
        query=f"INSERT INTO Costo_Energia_Storico(Id_costo,Datatime,Costo_acquisto,Costo_vendita) VALUES('{Id_costo}','{Datatime}','{Costo_acquisto}','{Costo_vendita}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()

##COLLAUDO CLASSE
ts=TesterSql()
ts.insert_Utente("kriskehayov","kris","kehayov","2003/05/03 12:50:50","buonasera@gmail.com","pass-loca","Milano")

##BLOCCO DI CODICE FUNZIONANTE 100%
"""
    try:
        connesione = pymssql.connect(
            server='ce2.database.windows.net',
            user='SuperAdmin',
            password='CiaoCai123',
            database='CE')
        cursore = connesione.cursor()
        id_p = "0000003"
        dimensione = "500"
        stato = "disp"
        prezzo = 600
        query = f"INSERT INTO Tipo_Pannello(Id_pannello, Dimensione, Stato, Prezzo) VALUES('{id_p}','{dimensione}','{stato}',{prezzo})"

        cursore.execute(query)
        connesione.commit()
        cursore.close()
        connesione.close()
    except Exception as e:
        print(e)
"""



