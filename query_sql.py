import pyodbc


def visualizzaUtente():
    lista = []
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        try:
            cursor = connection.cursor()
            query = f"""
                SELECT *
                FROM Utente
                """
            cursor.execute(query)
            # Fetch all restituisce una lista di tuple, dove ogni tupla rappresenta una riga della tabella
            lista = cursor.fetchall()
            # Visualizzazione delle tabelle
            print("Tabelle nel database:")
            for table in lista:
                print("\n")
                print(table)
                print("\n")
        except pyodbc.Error as e:
            print("Errore durante il recupero delle tabelle:", e)

#visualizzaUtente() 


def visualizzaMeteo():
    lista = []
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        try:
            cursor = connection.cursor()
            query = f"""
                SELECT *
                FROM Meteo
                """
            cursor.execute(query)
            # Fetch all restituisce una lista di tuple, dove ogni tupla rappresenta una riga della tabella
            lista = cursor.fetchall()
            # Visualizzazione delle tabelle
            print("Tabelle nel database:")
            for table in lista:
                print("\n")
                print(table)
                print("\n")
        except pyodbc.Error as e:
            print("Errore durante il recupero delle tabelle:", e)

#visualizzaMeteo()

def visualizzaBatteria():
    lista = []
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        try:
            cursor = connection.cursor()
            query = f"""
                SELECT *
                FROM Batteria
                """
            cursor.execute(query)
            # Fetch all restituisce una lista di tuple, dove ogni tupla rappresenta una riga della tabella
            lista = cursor.fetchall()
            # Visualizzazione delle tabelle
            print("Tabelle nel database:")
            for table in lista:
                print("\n")
                print(table)
                print("\n")
        except pyodbc.Error as e:
            print("Errore durante il recupero delle tabelle:", e)

#visualizzaBatteria()

def visualizzaTipoPann():
    lista = []
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        try:
            cursor = connection.cursor()
            query = f"""
                SELECT *
                FROM Tipo_Pannello
                """
            cursor.execute(query)
            # Fetch all restituisce una lista di tuple, dove ogni tupla rappresenta una riga della tabella
            lista = cursor.fetchall()
            # Visualizzazione delle tabelle
            print("Tabelle nel database:")
            for table in lista:
                print("\n")
                print(table)
                print("\n")
        except pyodbc.Error as e:
            print("Errore durante il recupero delle tabelle:", e)

#visualizzaTipoPann()


def visualizzaProduzioneStorico():
    lista = []
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        try:
            cursor = connection.cursor()
            query = f"""
                SELECT *
                FROM Produzione_Storico
                """
            cursor.execute(query)
            # Fetch all restituisce una lista di tuple, dove ogni tupla rappresenta una riga della tabella
            lista = cursor.fetchall()
            # Visualizzazione delle tabelle
            print("Tabelle nel database:")
            for table in lista:
                print("\n")
                print(table)
                print("\n")
        except pyodbc.Error as e:
            print("Errore durante il recupero delle tabelle:", e)

#visualizzaProduzioneStorico()


def visualizzaCostoEnergiaStorico():
    lista = []
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        try:
            cursor = connection.cursor()
            query = f"""
                SELECT *
                FROM Costo_Energia_Storico
                """
            cursor.execute(query)
            # Fetch all restituisce una lista di tuple, dove ogni tupla rappresenta una riga della tabella
            lista = cursor.fetchall()
            # Visualizzazione delle tabelle
            print("Tabelle nel database:")
            for table in lista:
                print("\n")
                print(table)
                print("\n")
        except pyodbc.Error as e:
            print("Errore durante il recupero delle tabelle:", e)

#visualizzaCostoEnergiaStorico()


def visualizzaCompravendita():
    lista = []
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        try:
            cursor = connection.cursor()
            query = f"""
                SELECT *
                FROM Compravendita
                """
            cursor.execute(query)
            # Fetch all restituisce una lista di tuple, dove ogni tupla rappresenta una riga della tabella
            lista = cursor.fetchall()
            # Visualizzazione delle tabelle
            print("Tabelle nel database:")
            for table in lista:
                print("\n")
                print(table)
                print("\n")
        except pyodbc.Error as e:
            print("Errore durante il recupero delle tabelle:", e)

#visualizzaCompravendita()


def visualizzaSim():
    lista = []
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        try:
            cursor = connection.cursor()
            query = f"""
                SELECT *
                FROM Simulazione
                """
            cursor.execute(query)
            # Fetch all restituisce una lista di tuple, dove ogni tupla rappresenta una riga della tabella
            lista = cursor.fetchall()
            # Visualizzazione delle tabelle
            print("Tabelle nel database:")
            for table in lista:
                print("\n")
                print(table)
                print("\n")
        except pyodbc.Error as e:
            print("Errore durante il recupero delle tabelle:", e)

#visualizzaSim()


def visualizzaStruttura():
    lista = []
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        try:
            cursor = connection.cursor()
            query = f"""
                SELECT *
                FROM Struttura
                """
            cursor.execute(query)
            # Fetch all restituisce una lista di tuple, dove ogni tupla rappresenta una riga della tabella
            lista = cursor.fetchall()
            # Visualizzazione delle tabelle
            print("Tabelle nel database:")
            for table in lista:
                print("\n")
                print(table)
                print("\n")
        except pyodbc.Error as e:
            print("Errore durante il recupero delle tabelle:", e)

#visualizzaStruttura()


#-- per ogni simulazione tutti gli edifici e la somma della superficie dei pannelli solari di ogni edificio --
def query1():
    lista = []
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        try:
            cursor = connection.cursor()
            query = """
                SELECT s.Id_Simulazione, COUNT(st.Id_Struttura) AS Numero_Edifici, SUM(st.Superficie) AS Superficie_Pannelli_Solari
                FROM Simulazione as s
                JOIN Struttura as st ON s.Id_Simulazione = st.IdS
                GROUP BY s.Id_Simulazione;
                """
            cursor.execute(query)
            lista = cursor.fetchall()
            print("CE" + " | " + "Select effettuata! Disconnessione... \n")
        except pyodbc.Error as Errore:
            print("CE" + " | " + "Errore {SELECT}! Disconnessione... \n")
            print(Errore)
    return lista


#-- per ogni simulazione datatime dell'ultimo inseiriti di produzione, consumo, stato della batteria --
def query2():
    connection_string = "Driver={SQL Server Native Client 11.0};Server=ce2.database.windows.net;Database=CE;Uid=SuperAdmin;Pwd=CiaoCai123;"
    with pyodbc.connect(connection_string) as connection:
        try:
            cursor = connection.cursor()
            query = """
                SELECT TOP 1 s.Id_simulazione, b.Datatime, b.Entrata, b.Uscita, b.Energia_stoccata
                FROM Batteria as b join Simulazione as s ON b.IdS = s.Id_simulazione
                ORDER BY b.Entrata, b.Uscita, b.Energia_stoccata DESC
                """
            cursor.execute(query)
            lista = cursor.fetchall()
            print("CE" + " | " + "Select effettuata! Disconnessione... \n")
        except pyodbc.Error as Errore:
            print("CE" + " | " + "Errore {SELECT}! Disconnessione... \n")
            print(Errore)
    return lista