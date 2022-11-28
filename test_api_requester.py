import main
import pytest
import requests

@pytest.fixture
def api_req() -> main.API_Requester:
    return main.API_Requester(input_url="https://api.binance.com/api/v3/klines",
                                input_traidingpair="BTCUSDT")


def test_1(api_req):
    timestamp = api_req.get_timestamp(input_datetime="01.01.2022 01:00:00")
    assert 1640995200000 == timestamp


def test_2(api_req):
    result = api_req.get_raw_data()
    assert type(result) == list


def test_3(api_req):
    api_req.url = "https://api.bsdgasdfasdgasef"
    with pytest.raises(requests.exceptions.ConnectionError):
        api_req.get_raw_data()


def test_4(api_req):
    df = api_req.get_dataframe()
    assert df.shape[1] == 3 and df.shape[0] >= 1


def test_5():
    df = main.get_data_from_DB()
    assert df.shape[1] == 3 and df.shape[0] >= 1