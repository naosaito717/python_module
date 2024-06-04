import pandas as pd
import pyodbc

# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=10.10.3.57;'
#                       'uid=sa;'
#                       'pwd=NewGrads2024;'
#                       'Database=GB新人研修_齋藤直;')

# #cursor = conn.cursor()
# df = pd.read_sql('SELECT * FROM mic拠点',conn)

# print(df)


# cursor.execute('DELETE * FROM 拠点 WHERE id = 7')
# cursor.execute('SELECT * FROM 拠点')
              
# for row in cursor:
#     print(row)

# conn.commit()
import os
from dotenv import load_dotenv
load_dotenv()

SERVER = os.getenv('SERVER')
DATABASE = os.getenv('DATABASE')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# id--自動連番
# 名前　vercher
# 年齢 int


# data = "{SQL Server}" + SERVER
# data2 = ";uid"+DB_USER
# data3 = ";pwd"

print(SERVER)

# connection_info ="Driver={SQL Server};SERVER=" + SERVER + ";uid=" + DB_USER + ";pwd=" + DB_PASSWORD +";Database=" + DATABASE


connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={DB_USER};PWD={DB_PASSWORD}'
conn = pyodbc.connect(connectionString)

cursor = conn.cursor()

# insert_query = '''
# INSERT INTO Users
# ("名前","年齢")
# VALUES
# (?,?);
# '''

# user_data = [('saito',22)]

# cursor.execute("INSERT INTO Users (名前,年齢) VALUES ('saito',22)")
# conn.commit()

# cursor.execute("UPDATE Users SET 年齢=32 WHERE id=3")
# conn.commit()


#pandasを利用してUsersテーブルをdfに入れる
df = pd.read_sql('SELECT * FROM Users',conn)
print(df)