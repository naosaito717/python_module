import pandas as pd
import pyodbc



import os
from dotenv import load_dotenv
load_dotenv()

SERVER = os.getenv('SERVER')
DATABASE = os.getenv('DATABASE')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={DB_USER};PWD={DB_PASSWORD}'
conn = pyodbc.connect(connectionString)

cursor = conn.cursor()

# cursor.execute("CREATE TABLE movies(id int primary key, Release_Date date, Title varchar(50), Overview varchar(50),Popularity varchar(50),Vote_Count int ,Vote_Average int ,Original_Language  varchar(50) ,Genre varchar(50) ,Poster_Url varchar(100))")

df = pd.read_csv("./mymoviedb.csv")


