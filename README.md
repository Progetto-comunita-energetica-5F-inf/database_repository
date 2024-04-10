# README

Il presente codice fornisce una serie di classi e funzioni per l'inserimento di dati in due diversi tipi di database: MongoDB e SQL Server. 

## Struttura del codice

Il codice è organizzato in tre parti principali:

1. **Classe `TestAppCLI`**: questa classe gestisce l'interfaccia a riga di comando (CLI) per l'utente. Attraverso questa CLI, l'utente può scegliere se accedere al database MongoDB o al database SQL Server e inserire i dati corrispondenti.

2. **Classe `TesterMongo`**: questa classe gestisce le operazioni di inserimento dei dati nel database MongoDB. Include metodi per l'inserimento di mappe, case, negozi, edifici pubblici e spazi pubblici.

3. **Classe `TesterSQL`**: questa classe gestisce le operazioni di inserimento dei dati nel database SQL Server. Include metodi per l'inserimento di utenti, dati meteo, tipi di pannelli solari, produzione storica, costi energetici storici, batterie, transazioni di compravendita, simulazioni e strutture.

## Come funziona

L'utente può interagire con il codice tramite la classe `TestAppCLI`. All'avvio, viene visualizzato un menu che consente di scegliere tra l'accesso al database MongoDB (opzione 1) e l'accesso al database SQL Server (opzione 2).

### Accesso al database MongoDB

Se l'utente sceglie di accedere al database MongoDB, può inserire i dati relativi a diverse entità come mappe, case, negozi, edifici pubblici e spazi pubblici. Per ciascuna entità, verranno richiesti i dati pertinenti, come lunghezza, larghezza, prezzo, ecc.

### Accesso al database SQL Server

Se l'utente sceglie di accedere al database SQL Server, può inserire i dati relativi a utenti, dati meteo, tipi di pannelli solari, produzione storica, costi energetici storici, batterie, transazioni di compravendita, simulazioni e strutture. Per ciascuna entità, verranno richiesti i dati pertinenti, come username, temperatura, guadagno, ecc.

## Tutorial

Ecco un breve tutorial su come utilizzare il codice:

1. Avvia il programma eseguendo il codice Python.
2. Scegli se accedere al database MongoDB (opzione 1) o al database SQL Server (opzione 2).
3. Segui le istruzioni a schermo per inserire i dati richiesti per l'entità scelta.
4. Ripeti il processo per inserire altre entità o esci dal programma quando hai finito.

È importante notare che per l'utilizzo del codice è necessario disporre di un'adeguata configurazione e accesso ai database MongoDB e SQL Server. Assicurati di avere le credenziali e i dettagli di connessione corretti per poter eseguire con successo le operazioni di inserimento dei dati.
