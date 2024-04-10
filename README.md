# Descrizione del Codice e Tutorial

Il codice fornito è diviso in due parti principali: l'interfaccia per MongoDB e l'interfaccia per SQL. L'obiettivo dell'applicazione è fornire un'interfaccia utente per l'inserimento di dati in un database, utilizzando due diverse tecnologie di database: MongoDB e SQL Server.

## Struttura del Codice

1. Modulo `insert_mongo.py`:
   - Contiene la classe `TesterMongo` che gestisce l'interazione con il database MongoDB.
   - La classe contiene metodi per inserire dati nelle varie collezioni del database MongoDB.

2. Modulo `insert_sql.py`:
   - Contiene la classe `TesterSQL` che gestisce l'interazione con il database SQL Server.
   - La classe contiene metodi per inserire dati nelle varie tabelle del database SQL Server.

3. `TestAppCLI`:
   - Questa classe rappresenta l'interfaccia utente della nostra applicazione.
   - L'utente può scegliere se accedere al database MongoDB o al database SQL Server.
   - All'interno di ciascuna scelta, l'utente può inserire diversi tipi di dati corrispondenti alle varie entità del database.

## Tutorial

Per utilizzare l'applicazione, segui i passaggi seguenti:

1. Esegui il file `readme.txt` nel tuo ambiente di sviluppo Python.
2. Avvia il programma inserendo `python nome_file.py`.
3. Seleziona se accedere al database MongoDB o al database SQL Server.
4. Segui le istruzioni sul terminale per inserire i dati desiderati.

## Esempio di Utilizzo

1. Seleziona l'opzione per accedere al database MongoDB.
2. Scegli l'operazione di inserimento desiderata, ad esempio "Inserire una Mappa".
3. Segui le istruzioni per inserire i dettagli della mappa, come lunghezza, larghezza e prezzo.
4. Ripeti il processo per altre operazioni di inserimento o uscire dall'applicazione.

Nota: Assicurati di avere le credenziali corrette per accedere ai database MongoDB e SQL Server, e che i server siano in esecuzione prima di utilizzare l'applicazione.
