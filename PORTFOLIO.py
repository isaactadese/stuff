
import pandas as pd
import pyodbc
import sqlalchemy
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-N1A8QKV\SQLEXPRESS;'
                      'Database=sa;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

sql_query1 = pd.read_sql_query('SELECT * FROM ABCTable as test1',conn)
sql_query2 = pd.read_sql_query('SELECT * FROM ABCTable',conn)
#print(sql_query1)
#print(type(sql_query1))

for index, row in sql_query1.iterrows():
    cursor.execute("INSERT INTO HumanResources.DepartmentTest (DepartmentID,Name,GroupName) values(?,?,?)", sql_query1.iloc[0], sql_query1.iloc[1], sql_query1.iloc[2])
conn.commit()
cursor.close()

sql_query2 = pd.read_sql_query('SELECT * FROM ABCTable',conn)
#print(sql_query2)
#print(type(sql_query2))

#df1=pd.read_excel('Population-country2.xlsx', index_col=0)
#f2=pd.read_excel('Population-country21.xlsx', index_col=0)
frames = [sql_query1,sql_query1]

result = pd.concat(frames)


def color(val):
    if val == 'A':
        color = 'green'
    elif val == "B":
        color ='bright green'
    elif val == "C":
        color = 'yellow'
    elif val == "D":
        color = 'orange'
    elif val == 'E':
        color = 'pink'
    elif val == "F":
        color = 'red'
    elif val == "G":
        color = 'white'
    elif val == "H":
        color = 'purple'
    elif val == "I":
        color = 'white'
    elif val == "K":
        color = 'brown'   
    elif val == "N":
        color = 'white'
    elif val == "P":
        color = 'purple'
    elif val == "X":
        color = 'Bordeaux'
    elif val == "Y":
        color = 'Bordeaux'
    elif val == "Z":
        color = 'Bordeaux'
    return 'background-color: %s' % color

result.style.applymap(color, subset=['dirog'])
result.to_excel("output.xlsx")