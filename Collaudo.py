from Insert_mongo import *
from insert_mysql import *

class TestAppCLI:
    def constructor(self):
        menu=True

        while menu:
            choice=input("Premi: \n 1: Per accedere al dbMongo \n 2: Per accedere al dbSQL")
            if choice==1:
                menuMongo=True
                tm=TesterMongo()
                while menuMongo:
                    c1=input("Premi: \n 1:Per inserire una Mappa \n 2:Per inserire una Casa \n 3:Per inserire un Negozio \n 4:Per inserire un EdificioPubblico \n 5:Per inserire uno SpazioPubblico")
                    if c1==1:
                        #id, lunghezza,larghezza, prezzo
                        id_mappa = input("inserisci un id ")
                        lunghezza = input("inserisci la lunghezza ")
                        larghezza = input("inserisci la larghezza ")
                        prezzo = input("inserisci il prezzo ")
                        tm.insert_mappa(id_mappa, lunghezza, larghezza, prezzo)
                        #gestisci creazione della mappa
                    elif c1==2:
                        #id, lunghezza, larghezza, piani, appartamenti, tipologia, prezzo
                        id_casa = input("inserisci un id ")
                        lunghezza = input("inserisci la lunghezza ")
                        larghezza = input("inserisci la larghezza ")
                        appartamenti = input("inserisci l'appartamenti ")
                        tipologia = input("inserisci la tipologia ")
                        prezzo = input("inserisci il prezzo ")
                        tm.insert_casa(id_casa, lunghezza, larghezza, appartamenti, tipologia, prezzo)
                        # gestisci creazione della casa
                    elif c1==3:
                        #id, lunghezza, larghezza, nome_attivita, servizi, prezzo
                        id_negozio = input("inserisci un id ")
                        lunghezza = input("inserisci la lunghezza ")
                        larghezza = input("inserisci la larghezza ")
                        nome_attivita = input("inserisci il nome_attivita ")
                        servizi = input("inserisci il servizi ")
                        prezzo = input("inserisci il prezzo ")
                        tm.insert_negozio(id_negozio, lunghezza, larghezza, nome_attivita, servizi, prezzo)
                        #gestisci creazione del negozio
                    elif c1==4:
                        #id, lunghezza, larghezza, funzione, tipologia, prezzo, id_negozio
                        id_edificio = input("inserisci un id ")
                        lunghezza = input("inserisci la lunghezza ")
                        larghezza = input("inserisci la larghezza ")
                        funzione = input("inserisci la funzionalità ")
                        prezzo = input("inserisci il prezzo ")
                        id_negozio = input("inserisci l'id del negozio ")
                        tm.insert_EdificioP(id_edificio, lunghezza, larghezza, funzione, prezzo, id_negozio)
                        # gestisci creazione dell EDP
                    elif c1==5:
                        #id, lunghezza, larghezza, funzione, prezzo
                        id_spazioPub = input("inserisci un id ")
                        lunghezza = input("inserisci la lunghezza ")
                        larghezza = input("inserisci la larghezza ")
                        funzione = input("inserisci la funzionalità ")
                        prezzo = input("inserisci il prezzo ")
                        tm.insert_SpazioPubblico(id_spazioPub, lunghezza, larghezza, funzione, prezzo)
                        # gestisci creazione dell SP
                    else:
                        print("Errore nell'esecuzione della richiesta")
                        r1 = input("Premi: \n 0: per uscire \n 1:Per continuare con una nuova richiesta")
                        if r1 == 0:
                            menuMongo = False
                        else:
                            menuMongo = True
            elif choice==2:
                ts=TesterSql()
                menuSql=True
                while menuSql:
                    cc=input("Premi:\n 1: Per inserire un Utente \n 2:Per inserire una Simulazione \n 3:Per inserire Meteo, \n 4:Per inserire Batteria \n 5: Per inserire Compravendita \n 6: Per inserire TipoPannello \n 7: Per inserire ProduzioneStorico \n 8:Per inserire CostoEnergiaStorico")
                    if cc==1:
                        #username,nome,cognome,data,email,password,citta
                        username = input("inserisci un username ")
                        nome = input("inserisci il nome ")
                        cognome = input("inserisci il cognome ")
                        data = input("inserisci la data ")
                        email = input("inserisci l' email ")
                        citta = input("inserisci la città ")
                        ts.insert_Utente(username, nome, cognome, data, email, citta)
                    elif cc==2:
                        #Id_Simulazione, data_creazione, nome_città, UsernameUtente, MeteoDT
                        id_sim = input("inserisci un id_simulazione ")
                        data_creazione = input("inserisci la data creazione ")
                        nome_città = input("inserisci il nome della città ")
                        usernameUtente = input("inserisci Username ")
                        meteoDT = input("inserisci il datatime ")
                        ts.insert_Simulazione(id_sim, data_creazione, nome_città, usernameUtente, meteoDT)
                    elif cc==3:
                        #Datatime, pressione, temperatura, velocità_vento, direzione_vento, umidità, morfologia, precipitazioni, irraggiamento
                        datatime = input("inserisci il datatime ")
                        pressione = input("inserisci la pressione ")
                        temperatura = input("inserisci la temperatura")
                        velocità_vento = input("inserisci velocità del vento ")
                        direzione_vento = input("inserisci la direzione del vento ")
                        umidita = input("inserisci l'umidità ")
                        morfologia = input("inserisci la morfologia ")
                        precipitazioni = input("inserisci la precipitazioni")
                        irraggiamento = input("inserisci l'irraggiamento ")
                        ts.insert_Meteo(datatime, pressione, temperatura, velocità_vento, direzione_vento, umidita, morfologia, precipitazioni, irraggiamento)
                    elif cc==4:
                        #Id_Serie, energia_stoccata, entrata, uscita, datatime, capacità_max, Id_sim
                        id_Serie = input("inserisci un id ")
                        energia_stoccata = input("inserisci l'energia stoccata ")
                        entrata = input("inserisci l'entrata")
                        uscita = input("inserisci l'uscita")
                        datatime = input("inserisci il data e ora ")
                        capacita_max = input("inserisci la capacità massima ")
                        Id_sim = input("inserisci l'id della simulazione ")
                        ts.insert_Batteria(id_Serie, energia_stoccata, entrata, uscita, datatime, capacita_max, id_sim)
                    elif cc==5:
                        #Id_Transazione, datatime, guadagno, quantità_venduta, spesa, quantità_comprata, IdBatteria
                        id_Transazione = input("inserisci un id di transazione ")
                        datatime = input("inserisci la data e ora ")
                        guadagno = input("inserisci il guadagno ")
                        quantita_venduta = input("inserisci la quantità venduta")
                        spesa = input("inserisci le spese ")
                        quantita_comprata = input("inserisci la quantità comprata")
                        id_Batteria = input("inserisci l'id della batteria ")
                        ts.insert_Compravendita(id_Transazione, datatime, guadagno, quantita_venduta, spesa, quantita_comprata, id_Batteria)
                    elif cc==6:
                        #Id_pannello, Dimensioni, Stato, Prezzo
                        id_pannello = input("inserisci l'id del pannello ")
                        dimensioni = input("inserisci la dimensione ")
                        stato = input("inserisci lo stato ")
                        prezzo = input("inserisci il prezzo")
                        ts.insert_TipoPannello(id_pannello, dimensioni, stato, prezzo)
                    elif cc==7:
                        #Id_produzione,Potenza,Datatime
                        id_produzione = input("inserisci l'id di produzione ")
                        potenza = input("inserisci la potenza ")
                        datatime = input("inserisci la data e ora ")
                        ts.insert_ProduzioneStorico(id_produzione, potenza, datatime)
                    elif cc==8:
                        #Id_costo,Datatime,Costo_acquisto,Costo_vendita
                        id_costo = input("inserisci l'id del costo ")
                        datatime = input("inserisci la data e ora ")
                        costo_acquisto = input("inserisci il costo dell'aqcuisto ")
                        costo_vendita = input("inserisci il costo di vendita ")
                        ts.insert_CostoEnergiaStorico(id_costo, datatime, costo_acquisto, costo_vendita)
                    elif cc==9:
                        # Id_Edificio, consumo, posizione, direzione, costo, numero_pannelli, numero_abitanti, piani, superficie, tipo, IdSimulazione, IdPannello, IdProduzione
                        id_edificio = input("inserisci l'id dell'Edificio ")
                        consumo = input("inserisci il consumo ")
                        posizione = input("inserisci la posizione ")
                        direzione = input("inserisci la direzione ")
                        costo = input("inserisci il costo ")
                        numero_pannelli = input("inserisci il numero dei pannelli ")
                        numero_abitanti = input("inserisci il numero degli abitanti ")
                        piani = input("inserisci gli piani ")
                        superficie = input("inserisci la superficie ")
                        tipo = input("inserisci il tipo ")
                        id_simulazione = input("inserisci l'id della simulazione ")
                        id_pannello = input("inserisci l'id del pannello ")
                        id_produzione = input("inserisci l'id della produzione")
                        ts.insert_Struttura(id_edificio, consumo, posizione, direzione, costo, numero_pannelli, numero_abitanti, piani, superficie, tipo, id_simulazione, id_pannello, id_produzione)
                    else:
                        menuSql=False
                        print("Errore nell'esecuzione della richiesta")
                        r2 = input("Premi: \n 0: per uscire \n 1:Per continuare con una nuova richiesta")
                        if r2 == 0:
                            menuSql = False
                        else:
                            menuSql = True
            else:
                print("Errore nell'esecuzione della richiesta")
                rr=input("Premi: \n 0: per uscire \n 1:Per continuare con una nuova richiesta")
                if rr==0:
                    menu=False
                else:
                    menu=True

TestAppCLI()

