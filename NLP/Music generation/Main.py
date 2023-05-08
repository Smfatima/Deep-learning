# Concept: Building a 



import psycopg2


con = psycopg2.connect(
database="stg_florence_db",
user="postgres",
password="139572",
host="localhost",
port= '5432'
)

if con == True:
    print("Connected!")
else:
    print("Not connected")
    print(TypeError)




