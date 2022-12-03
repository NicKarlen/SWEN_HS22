"""
Wir importieren die Packages, welche wir gebrauchen.
Neu kommt streamlit hinzu, da wir uns dazu entschieden haben, die Visualisierung über Streamlit zu machen.
Ggf. Streamlit Modul noch innerhalb Python installieren
Modul um unsere Daten in einem Streamlit server anzuzeigen.

URL zu gehosteter Website (streamlit):

https://nickarlen-swen-hs22-visu-91na1b.streamlit.app/


Um streamlit lokal zu hosten - in Terminal: streamlit run visu.py

"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import main



# Titel der Website (Tab-name) und icon von einer url genommen.
st.set_page_config(page_title="SWEN_2022", page_icon="https://cdn-icons-png.flaticon.com/512/5968/5968260.png")

#Hier wird der angezeigte Titel auf dem Streamlit definiert
st.title("Visualisierung BTCUSDT 01.-12.2022")

#Hier wird die Funktion "get_...." aufgerufen und wir erhalten einen Dataframe zurück, der in der Variable df_btcusdt gespeichert wird
df_btcusdt = main.get_data_from_DB()


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

# Wir mussten wie eine wrapper Funktion verwenden damit ein Fehler abgefangen werden kann. Try / Except funktionierte nicht direkt über dem "st.button" element.
def gather_data_wrapper():
    try:
        main.gather_data()
    except:
        st.text("Daten konnten nicht geladen werden:")
        st.text(main.API_req.last_req_response)

# Ein Button um die Funktion gather_data vom modul main zu triggern um neue Daten herunterzuladen
st.button(label="Collect new data",on_click=gather_data_wrapper)
