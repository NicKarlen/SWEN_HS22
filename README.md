# SWEN_HS22
Preisdaten von Binance API heruntergeladen, in eine Datenbank gespeichert und mittels "streamlit" visualisiert.

## Komponenten

1. main.py (Enthält die Klasse API_Fetcher und eine verschiedene Hilfsfunktionen)
2. visu.py (Enthält die Visualisierung mittels "streamlit")
3. test_api_requester.py (Enthält die Unittests)

## How to run it:

1. Download des gesamten Repositories
2. Installieren der benötigten Module


`$ pip install -r /path/to/requirements.txt`

3. Ausführen des folgenden Kommandos um den streamlit server lokal zu starten

`$ streamlit run /path/to/visu.py`

4. Es sollte sich automatisch ein Webseite öffnen auf der die Visualisierung sichtbar ist.


## Grob Aufbau des Codes:

![alt text](https://github.com/NicKarlen/SWEN_HS22/blob/main/Ablauf_SWEN.PNG?raw=true)


