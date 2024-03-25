import pymssql


class TesterSql:
    def constructor(self):
        self.connesione=pymssql.connect(
                    server='ce2.database.windows.net',
                    user='ApiUser',
                    password='ApiTeam123',
                    database='CE')
        self.cursore=self.connesione.cursor() #Gestione chiusura connesione e ecursore MANCANTE

    def insert_Utente(self,username,nome,cognome,data,email,password,citta):
        query="INSERT INTO Utente(Username,Nome,Cognome,data_nascita,email,password,citta) VALUES(?,?,?,?,?,?,?)"
        res=self.cursore.execute(query,(username,nome,cognome,data,email,password,citta))
        self.connesione.commit()
        if res== True:
            print("OPERAZIONE AVVENUTA CON SUCCESSO")
        else:
            print("ERRORE")
        
    def insert_Simulazione(self,Id_Simulazione, data_creazione, nome_città, UsernameUtente, MeteoDT):
        query="INSERT INTO Simulazione(Id_Simulazione, data_creazione, nome_città, Utente, Meteo) VALUES(?,?,?,?,?,?,?)"
        res=self.cursore.execute(query,(Id_Simulazione, data_creazione, nome_città, UsernameUtente, MeteoDT))
        self.connesione.commit()
        if res== True:
            print("OPERAZIONE AVVENUTA CON SUCCESSO")
        else:
            print("ERRORE")


    def insert_Meteo(self,Datatime, pressione, temperatura, velocità_vento, direzione_vento, umidità, morfologia, precipitazioni, irraggiamento):
        query="INSERT INTO Meteo(Datatime, pressione, temperatura, velocità_vento, direzione_vento, umidità, morfologia, precipitazioni, irraggiamento) VALUES(?,?,?,?,?,?,?)"
        res=self.cursore.execute(query,(Datatime, pressione, temperatura, velocità_vento, direzione_vento, umidità, morfologia, precipitazioni, irraggiamento))
        self.connesione.commit()
        if res== True:
            print("OPERAZIONE AVVENUTA CON SUCCESSO")
        else:
            print("ERRORE")

    def insert_Batteria(self,Id_Serie, energia_stoccata, entrata, uscita, datatime, capacità_max, Id_sim):
        query="INSERT INTO Batteria(Id_Serie, energia_stoccata, entrata, uscita, datatime, capacità_max, Id_sim) VALUES(?,?,?,?,?,?,?)"
        res=self.cursore.execute(query,(Id_Serie, energia_stoccata, entrata, uscita, datatime, capacità_max, Id_sim))
        self.connesione.commit()
        if res== True:
            print("OPERAZIONE AVVENUTA CON SUCCESSO")
        else:
            print("ERRORE")

    def insert_Compravendita(self,Id_Transazione, datatime, guadagno, quantità_venduta, spesa, quantità_comprata, IdBatteria):
        query="INSERT INTO Compravendita(Id_Transazione, datatime, guadagno, quantità_venduta, spesa, quantità_comprata, IdBatteria) VALUES(?,?,?,?,?,?,?)"
        res=self.cursore.execute(query,(Id_Transazione, datatime, guadagno, quantità_venduta, spesa, quantità_comprata, IdBatteria))
        self.connesione.commit()
        if res== True:
            print("OPERAZIONE AVVENUTA CON SUCCESSO")
        else:
            print("ERRORE")


    def insert_Struttura(self,Id_Edificio, consumo, posizione, direzione, costo, numero_pannelli, numero_abitanti, piani, superficie, tipo, IdSimulazione, IdPannello, IdProduzione):
        query="INSERT INTO Struttura(Id_Edificio, consumo, posizione, direzione, costo, numero_pannelli, numero_abitanti, piani, superficie, tipo, IdSimulazione, IdPannello, IdProduzione) VALUES(?,?,?,?,?,?,?)"
        res=self.cursore.execute(query,(Id_Edificio, consumo, posizione, direzione, costo, numero_pannelli, numero_abitanti, piani, superficie, tipo, IdSimulazione, IdPannello, IdProduzione))
        self.connesione.commit()
        if res== True:
            print("OPERAZIONE AVVENUTA CON SUCCESSO")
        else:
            print("ERRORE")

    def insert_TipoPannello(self,Id_pannello, Dimensioni, Stato, Prezzo):
        query="INSERT INTO TipoPannello(Id_pannello, Dimensioni, Stato, Prezzo) VALUES(?,?,?,?,?,?,?)"
        res=self.cursore.execute(query,(Id_pannello, Dimensioni, Stato, Prezzo))
        self.connesione.commit()
        if res== True:
            print("OPERAZIONE AVVENUTA CON SUCCESSO")
        else:
            print("ERRORE")

    def insert_ProduzioneStorico(self,Id_produzione,Potenza,Datatime):
        query="INSERT INTO ProduzioneStorico(Id_produzione,Potenza,Datatime) VALUES(?,?,?,?,?,?,?)"
        res=self.cursore.execute(query,(Id_produzione,Potenza,Datatime))
        self.connesione.commit()
        if res== True:
            print("OPERAZIONE AVVENUTA CON SUCCESSO")
        else:
            print("ERRORE")

    def insert_CostoEnergiaStorico(self,Id_costo,Datatime,Costo_acquisto,Costo_vendita):
        query="INSERT INTO Costo_Energia_Storico(Id_costo,Datatime,Costo_acquisto,Costo_vendita) VALUES(?,?,?,?,?,?,?)"
        res=self.cursore.execute(query,(Id_costo,Datatime,Costo_acquisto,Costo_vendita))
        self.connesione.commit()
        if res== True:
            print("OPERAZIONE AVVENUTA CON SUCCESSO")
        else:
            print("ERRORE")



    ##PROVARE LE FUNZIONI 