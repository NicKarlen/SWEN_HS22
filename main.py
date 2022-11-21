import requests
from datetime import datetime
import json
import pandas as pd
import sqlite3

"""
    API doku: https://binance-docs.github.io/apidocs/spot/en/#compressed-aggregate-trades-list 
"""
class API_Requester():

    
    def __init__(self, input_url: str, input_traidingpair: str) -> None:
        """
            # Konstruktor - Wird benötigt um die Klasse zu instanzieren
        """
        self.url = input_url
        self.traidingpair = input_traidingpair

    def get_timestamp(self, input_datetime) -> int:
        """
            Methode um aus einem lesbaren Timestamp einen UNIX-Timestamp zu machen (wird für die API Abfrage verwendet)
        """


    def get_raw_data(self) -> list[list]:
        """
            Methode um die Daten via Request von der API von Binance abzurufen.
        """

    def get_dataframe(self) -> pd.DataFrame:
        """
            Methode um einen Pandas Dataframe zu erstellen
        """
        pass


if __name__ == "__main__":
 
    API_req = API_Requester(input_url="https://api.binance.com/api/v3/klines",
                            input_traidingpair="BTCUSDT")




