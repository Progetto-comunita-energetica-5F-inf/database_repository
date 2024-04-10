README
Descrizione
Il codice fornito include due file Python: insert_mongo.py e insert_sql.py, oltre a una classe denominata TestAppCLI. Il programma consente l'inserimento di dati in un database MongoDB attraverso l'interfaccia fornita dalla classe TesterMongo.

Struttura del codice
Il codice è suddiviso in due parti principali:

Definizione della classe TestAppCLI, che gestisce l'interfaccia a riga di comando per l'utente.
Definizione della classe TesterMongo, che fornisce i metodi per l'inserimento di dati nel database MongoDB.
Funzionamento
Il programma fornisce un'interfaccia a riga di comando per l'utente. L'utente può scegliere di accedere al database MongoDB o SQL e inserire vari tipi di dati, come Mappa, Casa, Negozio, Edificio Pubblico e Spazio Pubblico.

Tutorial
Esegui il file TestAppCLI per avviare l'applicazione.
Seleziona il database a cui desideri accedere (MongoDB o SQL) inserendo 1 o 2, rispettivamente.
Segui le istruzioni a schermo per inserire i dati nel database selezionato.
Esempio di utilizzo
python
Copy code
tm = TesterMongo()
tm.insert_negozio("0002", "204", "205", "negozio1", "vendita", "15")
Questo esempio illustra come inserire un negozio nel database MongoDB utilizzando la classe TesterMongo.
