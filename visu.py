import streamlit as st
import sqlite3
import pandas as pd

"""
    Modul um unsere Daten in einem Streamlit server anzuzeigen.
"""

def get_data_from_DB():
    connection = sqlite3.connect(database="database.db")
    df = pd.read_sql(sql="SELECT * FROM price_data", con=connection)

    df = df.loc[:,["Kline Close time","Close price", "Volume"]]

    return df
