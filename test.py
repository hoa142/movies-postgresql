import psycopg2

url = "postgres://postgres:postgres@localhost:5432/postgres"

connection = psycopg2.connect(url)

cursor = connection.cursor()
cursor.execute("SELECT * FROM test;")

first_user = cursor.fetchall()

print(first_user)

connection.close()