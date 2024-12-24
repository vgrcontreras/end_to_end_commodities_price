import pandas as pd
from sqlalchemy import create_engine
import yfinance as yf
from settings import Settings

settings = Settings()

DB_USER = settings.DB_USER
DB_PASSWORD = settings.DB_PASSWORD
DB_HOST = settings.DB_HOST
DB_PORT = settings.DB_PORT
DB_NAME = settings.DB_NAME

DATABASE_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DATABASE_URL)

ticker_list = ['CL=F', 'GC=F', 'SI=F']

def fetch_commodities_data(
    ticker_symbol: str,
    period: str = '5d', 
    interval: str = '1d',
) -> pd.DataFrame:
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(period=period, interval=interval)[['Close']]
    data['ticker'] = ticker_symbol
    
    return data


def fetch_all_commodities_data(
    ticker_list: list
) -> pd.DataFrame:
    commodities_dataframes_list = []
    for ticker in ticker_list:
        data = fetch_commodities_data(ticker_symbol=ticker)
        commodities_dataframes_list.append(data)
    
    return pd.concat(commodities_dataframes_list)


def load_data(df: pd.DataFrame) -> None:
    df.to_sql('commodities', con=engine, schema='public', if_exists='replace')


if __name__ == '__main__':
    result = fetch_all_commodities_data(ticker_list)
    load_data(result)
