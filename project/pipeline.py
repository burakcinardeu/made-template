
import os
import pandas as pd
import sqlite3
import sqlalchemy as sql
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

d_files = ['alistairking/u-s-co2-emissions',
           'berkeleyearth/climate-change-earth-surface-temperature-data']



def download_kaggle(datasets):
    
    api.dataset_download_files(dataset=datasets, path = '../data', unzip = True)



    

def pre_pro_tem():
    df = pd.read_csv(filepath_or_buffer='../data/GlobalLandTemperaturesByState.csv')
    df = df[df.Country == 'United States'] #drop countries which are not USA
    del df['AverageTemperatureUncertainty'] #deleting unnecessary column
    df['Year'] = df['dt'].str[:4]
    df['Year'] = df['Year'].astype(int)
    df = df[df['Year'] >= 1970 ] 
    df = df[df['Year'] <= 2012]

    return df

    


def pre_pro_emi():
    df = pd.read_csv(filepath_or_buffer='../data/emissions.csv')
    df = df[df['year'] <= 2012]

    return df


def create_sqlite_table(df, table_name, engine):
    df.to_sql(name=table_name, con=engine, index=False, if_exists='append')


def main():
    data_directory = '../data'
    engine = sql.create_engine('sqlite:///../data/data.sqlite')
    for file in d_files:
        download_kaggle(file)
    df_tem = pre_pro_tem()
    df_emi = pre_pro_emi()
    create_sqlite_table(df=df_tem, table_name='temperature', engine=engine)
    create_sqlite_table(df=df_emi, table_name='emission', engine=engine)



if __name__ == '__main__':
    main()