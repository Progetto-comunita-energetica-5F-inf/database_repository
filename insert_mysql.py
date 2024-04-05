import time

import pymssql


class TesterSql:

    def __init__(self, server="ce2.database.windows.net", user="SuperAdmin", password="CiaoCai123", database="CE"):
        try:
            self.server = server
            self.user = user
            self.password = password
            self.database = database
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
        c = self.connessione()
        query = f"INSERT INTO Utente(Username,Nome,Cognome,Data_nascita,Email,Psw,Citta) VALUES('{username}','{nome}','{cognome}','{data}','{email}','{password}','{citta}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()

    def insert_Simulazione(self,data_creazione,nome_città,id_u,id_m):
        c = self.connessione()
        query = f"INSERT INTO Simulazione(Data_creazione,Nome_città,IdU,IdM) VALUES('{data_creazione}','{nome_città}','{id_u}','{id_m}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()

    def insert_Meteo(self,datatime,pressione,temperatura,velocità_vento,direzione_vento,umidità,
                     morfologia,precipitazioni,irraggiamento):
        c = self.connessione()
        query = f"INSERT INTO Meteo(Datatime,Pressione,Temperatura,Velocità_vento,Direzione_vento,Umidità,Morfologia,Precipitazioni,Irraggiamento) VALUES('{datatime}','{pressione}','{temperatura}','{velocità_vento}','{direzione_vento}','{umidità}','{morfologia}','{precipitazioni}','{irraggiamento}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()

    def insert_Batteria(self,energia_stoccata,entrata,uscita,datatime,capacità_max,id_sim):
        c = self.connessione()
        query = f"INSERT INTO Batteria(Energia_stoccata,Entrata,Uscita,Capacità_max,Datatime,IdS) VALUES('{energia_stoccata}','{entrata}','{uscita}','{capacità_max}','{datatime}','{id_sim}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()

    def insert_Compravendita(self,guadagno,quantità_venduta,spesa,quantità_comprata,datatime,id_batt):
        c = self.connessione()
        query = f"INSERT INTO Compravendita(Guadagno,Quantità_venduta,Spesa,Quantità_comprata,Datatime,IdBa) VALUES('{guadagno}','{quantità_venduta}','{spesa}','{quantità_comprata}','{datatime}','{id_batt}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()

    def insert_Struttura(self,consumo,posizione,direzione,costo,numero_abitanti,numero_pannelli,
                         piani,superficie,tipo,id_sim,id_pann,id_prod):
        c = self.connessione()
        query = f"INSERT INTO Struttura(Consumo,Posizione,Direzione,Costo,Numero_abitanti,Numero_pannelli,Piani,Superficie,Tipo,IdS,IdPan,IdProd) VALUES('{consumo}','{posizione}','{direzione}','{costo}','{numero_abitanti}','{numero_pannelli}','{piani}','{superficie},'{tipo}','{id_sim}','{id_pann}','{id_prod}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()

    def insert_TipoPannello(self,id_pannello,dimensione,stato,prezzo):
        c = self.connessione()
        time.sleep(10)
        query = f"INSERT INTO TipoPannello(Dimensione,Stato,Prezzo) VALUES(
        {dimensione},
        {stato},
        {prezzo}
        )"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()

    def insert_ProduzioneStorico(self,potenza,datatime):
        c = self.connessione()
        query = f"INSERT INTO ProduzioneStorico(Id_Produzione,Potenza,Datatime) VALUES(
        '{potenza}',
        '{datatime}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()

    def insert_CostoEnergiaStorico(self,datatime,costo_acquisto,costo_vendita):
        c = self.connessione()
        query = f"INSERT INTO Costo_Energia_Storico(Datatime,Costo_acquisto,Costo_vendita) VALUES (
        '{datatime}',
        '{costo_acquisto}',
        '{costo_vendita}')"
        cursore = c.cursor()
        cursore.execute(query)
        c.commit()
        self.connesione.commit()
        self.disconnesione()

        ##COLLAUDO CLASSE
        ts = TesterSql()
        ts.insert_Utente("kriskehayov", "kris", "kehayov", "2003/05/03 12:50:50", "buonasera@gmail.com", "pass-loca",
                         "Milano")

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



