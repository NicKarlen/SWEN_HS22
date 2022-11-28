#wir müssen pytest importieren, damit das Testing funktioniert, main braucht es, weil wir auch Teile des main testen
#request importieren wir, weil wir die Funktion request auch testen
import main
import pytest
import requests

#@pytest.fixture ist ein Python Decorator des pytest Moduls, ein Hinweis, damit der Code richig läuft
#der Returnwert kann in jeder Funktion als Parameter übergeben werden
#diese Funktion wird definiert, damit wir main.API_Requester() nicht in jedem Test instanzieren müssen, sondern nur darauf referenzieren müssen
@pytest.fixture
def api_req() -> main.API_Requester:
    return main.API_Requester(input_url="https://api.binance.com/api/v3/klines",
                                input_traidingpair="BTCUSDT")

#Test1 hier testen wir, ob wir von der Funktion api.req.get_timestamp den korrekten UNIX-Timestamp zurückerhalten
def test_1(api_req):
    timestamp = api_req.get_timestamp(input_datetime="01.01.2022 01:00:00")
    assert 1640995200000 == timestamp

#Test2 wir testen, ob wir von der Funktion api_req.get_raw_data eine Liste zurückerhalten
def test_2(api_req):
    result = api_req.get_raw_data()
    assert type(result) == list

#Test3 wir testen, ob wir von der Funktion api_req.get_raw_data() mit einer falschen Variable api_req.url eine Fehlermeldung des Typs requests.exceptions.ConnectionError erhalten
def test_3(api_req):
    api_req.url = "https://api.bsdgasdfasdgasef"
    with pytest.raises(requests.exceptions.ConnectionError):
        api_req.get_raw_data()

#Test4 wir überprüfen, ob wir von der Funktion api_req.get_dataframe ob wir genau 3 Kolonnen erhalten und es mindestens eine Row zurückgibt
def test_4(api_req):
    df = api_req.get_dataframe()
    assert df.shape[1] == 3 and df.shape[0] >= 1

#Test5 wir überprüfen, ob wir von der Funktion main.get_data_from_DB ob wir genau 3 Kolonnen erhalten und es mindestens eine Row zurückgibt 
def test_5():
    df = main.get_data_from_DB()
    assert df.shape[1] == 3 and df.shape[0] >= 1