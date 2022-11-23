"""
Wir importieren die Packages, welche wir gebrauchen.
Neu kommt streamlit hinzu, da wir uns dazu entschieden haben, die Visualisierung über Streamlit zu machen.
Ggf. Streamlit Modul noch innerhalb Python installieren
Modul um unsere Daten in einem Streamlit server anzuzeigen.
"""

import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime



def get_data_from_DB() -> pd.DataFrame:
    """
    Wir holen die Daten aus der DB aus und speichern es in einem Dataframe
    """
    #Wie im ersten File verwenden wir das Modul sqlite3 mit deren Funktion wir eine Verbindung zur Datenbank database.db aufbauen.
    connection = sqlite3.connect(database="database.db")
    
    #Wir lesen die Tabelle aus der Datenbank aus. Wir nehmen sämtliche Spalten aus der Tabelle "price_data".
    df = pd.read_sql(sql="SELECT * FROM price_data", con=connection)
    #Wir wählen alle Reihen aus und spezifisch die drei Kolonnen "Kline Close time","Close price", "Volume" aus und speichern es in einem Datenframe
    df = df.loc[:,["Kline Close time","Close price", "Volume"]]
    #Wir geben den Wert df (Variable Dataframe) zurück
    return df

#Hier wird der angezeigte Titel auf dem Streamlit definiert
st.title("Visualisierung BTCUSDT 01.-12.2022")

#Hier wird die Funktion "get_...." aufgerufen und wir erhalten einen Dataframe zurück, der in der Variable df_btcusdt gespeichert wird
df_btcusdt = get_data_from_DB()


def modify_data(row):
    # Es wird eine Funktion erstellt, um die Datentypen und -formate an die Streamlit-Bedürfnisse anzupassen
    # Zuerst ändern wir den Datentypen für die Column "Close Price" in einen float (war ursprünglich ein str)
    row["Close price"] = float(row["Close price"])
    # Hier ändern wir den Unix-Timestamp in ein Datum in ein dateime-Format (gefunden auf stackoverflow, wobei die String-Umwandlung auskommentiert wurde)
    row["date"] = datetime.utcfromtimestamp(row["Kline Close time"]/1000)#.strftime('%Y-%m-%d')
    # Wir geben die row zurück
    return row
# Wir verwenden die apply-Funktion um modify_data auf alle rows anzuwenden und überschreiben die Variable mit dem angepassten Dataframe
df_btcusdt = df_btcusdt.apply(modify_data, axis=1)

## Wir testen den Datatyp der row 0 und column 3 (date)
#print(type(df_btcusdt.iloc[0,3]))

# Wir plotten ein Line-Charte über Streamlit und definieren die x-Achse sowie die y-Achse aus unserem df_btcusdt
st.line_chart(data=df_btcusdt, x="date", y="Close price")
