import pymysql
import sys

connection = pymysql.connect(
    host='semil-db-instance.cmxju4nvktwj.us-east-2.rds.amazonaws.com',
    user=sys.argv[1],
    password=sys.argv[2],
    db='semil-db',
)

#created table using mysql console

my_database = connection.cursor()
sql_statement = "INSERT INTO games (gid,gname,publisher,rating) values(%s,%s,%s,%s)"
values = ("4","CS:GO","steam","9")                                  #ran this for differnt values 
#my_database.execute(sql_statement,values)
connection.commit()

sql_statement = "SELECT * FROM games"
my_database.execute(sql_statement)
output = my_database.fetchall()
for x in output:
  print(x)
  
sql_statement = "UPDATE games SET gname='FIFA19' where gid='2'"
my_database.execute(sql_statement)
connection.commit()

sql_query = "DELETE FROM games where gname='cricket07'"
my_database.execute(sql_query)
connection.commit()
print("Row(s) deleted successfully!!!!")                                                            