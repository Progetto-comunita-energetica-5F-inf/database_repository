# README

## Descrizione del Codice
Il codice fornito consiste in una serie di funzioni Python che consentono l'esecuzione di query su un database SQL Server. Le query vengono eseguite utilizzando la libreria `pyodbc`.

## Struttura del Codice
Il codice è organizzato in tre funzioni principali:

1. `visualizzaTutto`: Questa funzione esegue una query per visualizzare tutte le tabelle nel database.

2. `query1`: Questa funzione esegue una query complessa per ottenere informazioni specifiche su ogni simulazione, inclusa la somma della superficie dei pannelli solari di ogni edificio.

3. `query2`: Questa funzione esegue una query per ottenere informazioni sull'ultimo inserimento di produzione, consumo e stato della batteria per ogni simulazione.

## Tutorial

Per utilizzare le funzioni:

1. Assicurati di avere la libreria `pyodbc` installata nel tuo ambiente Python.
2. Modifica le stringhe di connessione nel codice per riflettere le tue credenziali e le informazioni sul server del database.
3. Esegui il codice Python in un ambiente Python appropriato.

Ecco un esempio di utilizzo delle funzioni nel codice:

```python
# Visualizza tutte le tabelle nel database
visualizzaTutto()

# Esegue la query 1 e ottiene informazioni su ogni simulazione
risultato_query1 = query1()
print(risultato_query1)

# Esegue la query 2 e ottiene informazioni sull'ultimo inserimento di produzione, consumo e stato della batteria per ogni simulazione
risultato_query2 = query2()
print(risultato_query2)
