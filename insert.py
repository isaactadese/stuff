
import pandas as pd
import pyodbc
#import sqlalchemy
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-N1A8QKV\SQLEXPRESS;'
                      'Database=AdventureWorks2017;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()



sql_query1 = pd.read_sql_query("""
                                declare @date as date= (SELECT max([ModifiedDate]) 
                                FROM [AdventureWorks2017].[Sales].[Customer]) 
                                
                                SELECT *
                                 FROM [AdventureWorks2017].[Sales].[Customer] 
                                where cast(ModifiedDate as date ) =@date
                                """,conn)

print(sql_query1)
for index, row in sql_query1.iterrows():
    cursor.execute("""
    INSERT INTO [Sales].[Customer] (CustomerID, PersonID, StoreID, TerritoryID, AccountNumber, rowguid, ModifiedDate) values(?,?,?,?,?,?,?)"""
                   , sql_query1.iloc[0], sql_query1.iloc[1], sql_query1.iloc[2])
conn.commit()
cursor.close()