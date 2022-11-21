import requests
from datetime import datetime
import json
import pandas as pd
import sqlite3

"""
    API doku: https://binance-docs.github.io/apidocs/spot/en/#compressed-aggregate-trades-list 
"""
class API_Requester():

    # Konstruktor - Wird benötigt um die Klasse zu instanzieren
    def __init__(self, input_url: str, input_traidingpair: str) -> None:
        """
        Hier werden die Variablen für die Klassen definiert/übergeben
        URL:            ist URL/Endpunkt der Binance-API
        Tradingpair:    ist das zu untersuchende Tradingpair
        """
        self.url = input_url
        self.traidingpair = input_traidingpair

    def get_timestamp(self, input_datetime: str) -> int:
        """
            Methode um aus einem lesbaren Timestamp einen UNIX-Timestamp zu machen (wird für die API Abfrage verwendet)
        """
        #print(int(datetime.strptime(input_datetime, '%d.%m.%Y %H:%M:%S').timestamp() * 1000))
         
        #Hier wird aus dem Datum im Format Tag Monat Jahr Stunde Minute Sekunde mittels der Methode strptime ein Objekt der Klasse datetime erstellt und anschliessed daraus ein UNIX timestamp als int zurückgegeben
        return int(datetime.strptime(input_datetime, '%d.%m.%Y %H:%M:%S').timestamp() * 1000)
    
    def get_raw_data(self) -> list[list]:
        """
            In der API-Dokumentation werden die benötigten Parameter angegeben. Diese werden nachfolgend als Dictionnary definiert
            Die bei der Instanzierung übergebenen Variablen (URL + Tradingpair) und die nachfolgend definierten Parameter werden der "get"-Methode des "requests"-Moduls übergeben.
            
        """
        params = {            
            'symbol' : self.traidingpair,
            'interval': "1d",
            'startTime': self.get_timestamp(input_datetime="01.01.2022 01:00:00"),
            'endTime': self.get_timestamp(input_datetime="13.11.2022 01:00:00"),
            'limit': 1000
        }

        # Die "get"-Methode des "requests"-Moduls wird mit unseren Parameter ausgeführt und deren Resultat in der Variablen "req" abgespeichert
        req = requests.get(url=self.url, params=params)
        
        # Wir konvertieren den erhaltenen String in Form einer Liste von Liste in den Datentyp Liste von Liste
        return json.loads(req.text)       

    def get_dataframe(self) -> pd.DataFrame:
        """
            Methode um einen Pandas Dataframe zu erstellen
        """
        #Pass -> Methode bereits definiert, aber noch nicht fertig, damit keine Fehler aufpoppen

        """
        Wir rufen die Funktion "get_raw_data" auf und speichern das Ergebnis in "input_data" ab
        Die Variable "input_data" ist vom Typ Liste von Liste (Meta-Liste)
        """
    
        input_data = self.get_raw_data()
        #Pandas Modul, wir wollen eine Klasse "DataFrame" instanzieren (bedeutet in etwa "ins Leben rufen")
        #Plan wäre pd.DataFrame und mit Klammer (data=input_data) ist der Aufruf -> Ausführung des Plan
        df = pd.DataFrame(data=input_data)

        #Ich übergebe dem Dataframe die Namen der Kolonnen, die Anzahl Namen der Kolonnen muss mit der Anzahl Kolonnen im Dataframe übereinstimmen
        df.columns = [
            "Kline open time",
            "Open price",
            "High price",
            "Low price",
            "Close price",
            "Volume",
            "Kline Close time",
            "Quote asset volume",
            "Number of trades",
            "Taker buy base asset volume",
            "Taker buy quote asset volume",
            "Unused"
        ]
        #Wir wählen alle Zeilen (rows) mittels : aus und zusätzlich nur die drei folgenden Spalten, die restlichen fallen weg
        df = df.loc[:,["Kline Close time", "Close price", "Volume"]]

        return df #print(df) Printet es aus

if __name__ == "__main__":
 
    API_req = API_Requester(input_url="https://api.binance.com/api/v3/klines",
                            input_traidingpair="BTCUSDT")
    """
    Erster Versuch die API-Antwort zu printen führt zu folgendem Resultat: 
    {'code': -1100, 'msg': "Illegal characters found in parameter 'startTime'; legal range is '^[0-9]{1,20}$'."}
    jetzt funktioniert er, weil wir die 'startTime': self.get_timestamp(input_datetime="01.01.2022 01:00:00"), 
    und die 'endTime': self.get_timestamp(input_datetime="13.11.2022 01:00:00"), angepasst haben  
    """
    #print(API_req.get_raw_data())

    #API_req.get_timestamp(input_datetime="01.01.2022 01:00:00")
    
    #Der (Zwischen-)Schritt "Abspeichern in einer Variabel" wird somit übersprungen
    print(API_req.get_dataframe())

    #Abspeichern der obigen Variabel in einem x-beliebigen Wert
    #Zwischending = API_req.get_dataframe()

    #Print des zuvor definierten x-beliebigen Wert
    #print(Zwischending)