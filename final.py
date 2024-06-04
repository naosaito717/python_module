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

# cursor.execute("ALTER TABLE movies ALTER COLUMN Overview varchar(1000)")

# conn.commit()

# cursor.execute("CREATE TABLE newmovies(id int IDENTITY(1,1), Release_Date date, Title varchar(1000), Overview varchar(2000),Popularity varchar(1000),Vote_Count int ,Vote_Average int ,Original_Language  varchar(1000) ,Genre varchar(1000) ,Poster_Url varchar(1000))")
# conn.commit()


df = pd.read_csv('./mymoviedb.csv',lineterminator='\n')
for row in df.itertuples():
    # print(1)
    cursor.execute("INSERT INTO newmovies(Release_Date, Title, Overview,Popularity,Vote_Count,Vote_Average,Original_Language,Genre,Poster_Url) values(?,?,?,?,?,?,?,?,?)",row.Release_Date,row.Title,row.Overview,row.Popularity,row.Vote_Count,row.Vote_Average,row.Original_Language,row.Genre,row.Poster_Url)


conn.commit()