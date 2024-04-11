import pyodbc

"""
UTENTE-METEO-TIPO PANNELLO-PRODUZIONE STORICO-COSTO ENERGIA STORICO-BATTERIA-COMPRAVENDITA
"""

def insert_utente(username, nome, cognome, password):

    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        cursor = connection.cursor()
        query = f"""
            INSERT INTO Utente (Username, Nome, Cognome, Psw)
            VALUES ('{username}', '{nome}', '{cognome}', '{password}')
        """
        cursor.execute(query)
        connection.commit()
#insert_utente("iiiiii", "Mario", "Rossi", "Ciao123") # FUNZIONA


def insert_meteo(data_ora, pressione, temperatura, velocita_vento, direzione_vento, umidita, morfologia, precipitazioni, irraggiamento):

    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        cursor = connection.cursor()
        query = f"""
            INSERT INTO Meteo ( Datatime,Pressione, Temperatura, Velocità_vento, Direzione_vento, Umidità, Morfologia, Precipitazioni, Irraggiamento)
            VALUES ('{data_ora}', {pressione}, {temperatura}, {velocita_vento}, '{direzione_vento}', {umidita}, '{morfologia}', {precipitazioni}, {irraggiamento})
        """
        cursor.execute(query)
        connection.commit()

#insert_meteo("2024/03/22 12:30:12", 1013.25, 22.5, 3.5, "N", 60, "Sereno", 0.0, 500.0) # FUNZIONA



def insert_tipo_pannello(dimensione, stato, prezzo):
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        cursor = connection.cursor()
        query = f"""
            INSERT INTO Tipo_Pannello (Dimensione, Stato, Prezzo)
            VALUES ('{dimensione}', '{stato}', {prezzo})
        """
        cursor.execute(query)
        connection.commit()

# insert_tipo_pannello("50","non disponibile","600000") # FUNZIONA

def insert_produzione_storico(data_ora, potenza):
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"  # Your connection string
    with pyodbc.connect(connection_string) as connection:
        cursor = connection.cursor()
        query = f"""
            INSERT INTO Produzione_Storico (Datatime, Potenza)
            VALUES ('{data_ora}', {potenza})
        """
        cursor.execute(query)
        connection.commit()

# insert_produzione_storico("2024/03/22 12:30:12","700") # FUNZIONA


def insert_costo_energia_storico(data_ora, costo_acquisto, costo_vendita):
    connection_string =  "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        cursor = connection.cursor()
        query = f"""
            INSERT INTO Costo_Energia_Storico (Datatime, Costo_acquisto, Costo_vendita)
            VALUES ('{data_ora}', {costo_acquisto}, {costo_vendita})
        """
        cursor.execute(query)
        connection.commit()
#insert_costo_energia_storico("2024/03/22 12:30:12","500","1000") # FUNZIONA ME VERIFICA OUTPUT


def insert_batteria(energia_stoccata, entrata, uscita, capacita_max, data_ora):
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"  # Your connection string
    with pyodbc.connect(connection_string) as connection:
        cursor = connection.cursor()
        query = f"""
            INSERT INTO Batteria (Energia_stoccata, Entrata, Uscita, Capacità_max, Datatime)
            VALUES ({energia_stoccata}, {entrata}, {uscita}, {capacita_max}, '{data_ora}')
        """
        cursor.execute(query)
        connection.commit()
#insert_batteria("25","50","25","700","2024/03/22 12:30:12") # FUNZIONA

def insert_compravendita(guadagno, quantita_venduta, spesa, quantita_comprata, data_ora):
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"  # Your connection string
    with pyodbc.connect(connection_string) as connection:
        cursor = connection.cursor()
        query = f"""
            INSERT INTO Compravendita (Guadagno, Quantità_venduta, Spesa, Quantità_comprata, Datatime)
            VALUES ({guadagno}, {quantita_venduta}, {spesa}, {quantita_comprata}, '{data_ora}')
        """
        cursor.execute(query)
        connection.commit()


#insert_compravendita("500","4","400","40","2024/03/22 12:30:12") # FUNZIONA

def insert_simulazione(data_creazione, nome_citta, risparmio_co2,
                    id_utente, id_meteo):

    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"  #
    with pyodbc.connect(connection_string) as connection:
        cursor = connection.cursor()
        query = f"""
            INSERT INTO Simulazione (Data_creazione, Nome_città, Risparmio_co2, IdU, IdM)
            VALUES ('{data_creazione}', '{nome_citta}', {risparmio_co2}, {id_utente}, {id_meteo})
        """
        cursor.execute(query)
        connection.commit()


#insert_simulazione("2024/03/22", "Simulazionopoli", 500, 6, 2) # FUNZIONA

def insert_struttura(consumo, posizione, direzione, costo, numero_abitanti,
                    numero_pannelli, piani, superficie, tipo, id_simulazione, id_tipo_pannello, id_produzione):

    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        cursor = connection.cursor()
        query = f"""
            INSERT INTO Struttura (Consumo, Posizione, Direzione, Costo, Num_abitanti, 
            Numero_pannelli, Piani, Superficie, Tipo, IdS, IdPan, IdProd)
            VALUES ({consumo}, '{posizione}', '{direzione}', {costo}, {numero_abitanti}, 
            {numero_pannelli}, {piani}, {superficie}, '{tipo}', {id_simulazione}, {id_tipo_pannello}, {id_produzione})
        """
        cursor.execute(query)
        connection.commit()

#insert_struttura(500,"Centro Nord","Sud",500,40,3,7,3000,"vila",1,1,1) # FUNZIONA




