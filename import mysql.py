import pymssql

connesione=pymssql.connect(
            server='ce2.database.windows.net',
            user='ApiUser',
            password='ApiTeam123',
            database='CE')

cursore=connesione.cursor() #Gestione chiusura connesione e ecursore MANCANTE

def insert_Utente(username,nome,cognome,data,email,password,citta):
    query="INSERT INTO Utente(Username,Nome,Cognome,data_nascita,email,password,citta) VALUES(?,?,?,?,?,?,?)"
    res=cursore.execute(query,(username,nome,cognome,data,email,password,citta))
    connesione.commit()
    if res== True:
        print("OPERAZIONE AVVENUTA CON SUCCESSO")
    else:
        print("ERRORE")
    
def insert_Simulazione(Id_Simulazione, data_creazione, nome_città, UsernameUtente, MeteoDT):
    query="INSERT INTO Simulazione(Id_Simulazione, data_creazione, nome_città, Utente, Meteo) VALUES(?,?,?,?,?,?,?)"
    res=cursore.execute(query,(Id_Simulazione, data_creazione, nome_città, UsernameUtente, MeteoDT))
    connesione.commit()
    if res== True:
        print("OPERAZIONE AVVENUTA CON SUCCESSO")
    else:
        print("ERRORE")


def insert_Meteo(Datatime, pressione, temperatura, velocità_vento, direzione_vento, umidità, morfologia, precipitazioni, irraggiamento):
    query="INSERT INTO Meteo(Datatime, pressione, temperatura, velocità_vento, direzione_vento, umidità, morfologia, precipitazioni, irraggiamento) VALUES(?,?,?,?,?,?,?)"
    res=cursore.execute(query,(Datatime, pressione, temperatura, velocità_vento, direzione_vento, umidità, morfologia, precipitazioni, irraggiamento))
    connesione.commit()
    if res== True:
        print("OPERAZIONE AVVENUTA CON SUCCESSO")
    else:
        print("ERRORE")

def insert_Batteria(Id_Serie, energia_stoccata, entrata, uscita, datatime, capacità_max, Id_sim):
    query="INSERT INTO Batteria(Id_Serie, energia_stoccata, entrata, uscita, datatime, capacità_max, Id_sim) VALUES(?,?,?,?,?,?,?)"
    res=cursore.execute(query,(Id_Serie, energia_stoccata, entrata, uscita, datatime, capacità_max, Id_sim))
    connesione.commit()
    if res== True:
        print("OPERAZIONE AVVENUTA CON SUCCESSO")
    else:
        print("ERRORE")

def insert_Compravendita(Id_Transazione, datatime, guadagno, quantità_venduta, spesa, quantità_comprata, IdBatteria):
    query="INSERT INTO Compravendita(Id_Transazione, datatime, guadagno, quantità_venduta, spesa, quantità_comprata, IdBatteria) VALUES(?,?,?,?,?,?,?)"
    res=cursore.execute(query,(Id_Transazione, datatime, guadagno, quantità_venduta, spesa, quantità_comprata, IdBatteria))
    connesione.commit()
    if res== True:
        print("OPERAZIONE AVVENUTA CON SUCCESSO")
    else:
        print("ERRORE")


def insert_Struttura(Id_Edificio, consumo, posizione, direzione, costo, numero_pannelli, numero_abitanti, piani, superficie, tipo, IdSimulazione, IdPannello, IdProduzione):
    query="INSERT INTO Struttura(Id_Edificio, consumo, posizione, direzione, costo, numero_pannelli, numero_abitanti, piani, superficie, tipo, IdSimulazione, IdPannello, IdProduzione) VALUES(?,?,?,?,?,?,?)"
    res=cursore.execute(query,(Id_Edificio, consumo, posizione, direzione, costo, numero_pannelli, numero_abitanti, piani, superficie, tipo, IdSimulazione, IdPannello, IdProduzione))
    connesione.commit()
    if res== True:
        print("OPERAZIONE AVVENUTA CON SUCCESSO")
    else:
        print("ERRORE")

def insert_TipoPannello(Id_pannello, Dimensioni, Stato, Prezzo):
    query="INSERT INTO TipoPannello(Id_pannello, Dimensioni, Stato, Prezzo) VALUES(?,?,?,?,?,?,?)"
    res=cursore.execute(query,(Id_pannello, Dimensioni, Stato, Prezzo))
    connesione.commit()
    if res== True:
        print("OPERAZIONE AVVENUTA CON SUCCESSO")
    else:
        print("ERRORE")

def insert_ProduzioneStorico(Id_produzione,Potenza,Datatime):
    query="INSERT INTO ProduzioneStorico(Id_produzione,Potenza,Datatime) VALUES(?,?,?,?,?,?,?)"
    res=cursore.execute(query,(Id_produzione,Potenza,Datatime))
    connesione.commit()
    if res== True:
        print("OPERAZIONE AVVENUTA CON SUCCESSO")
    else:
        print("ERRORE")

def insert_CostoEnergiaStorico(Id_costo,Datatime,Costo_acquisto,Costo_vendita):
    query="INSERT INTO Costo_Energia_Storico(Id_costo,Datatime,Costo_acquisto,Costo_vendita) VALUES(?,?,?,?,?,?,?)"
    res=cursore.execute(query,(Id_costo,Datatime,Costo_acquisto,Costo_vendita))
    connesione.commit()
    if res== True:
        print("OPERAZIONE AVVENUTA CON SUCCESSO")
    else:
        print("ERRORE")



##PROVARE LE FUNZIONI 