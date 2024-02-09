from fastapi import FastAPI

import psycopg2

import configparser
from datetime import datetime

app = FastAPI()

config = configparser.ConfigParser()
config.read('config.ini')
host = config['PostgreSQL']['host']
user = config['PostgreSQL']['user']
password = config['PostgreSQL']['pswd']
dbname = config['PostgreSQL']['db_name']

@app.get('/greet/history')
async def greetHistory():
    print(host)
    return postgreHistory()

@app.get('/greet/{name}')
async def greetAdd(name: str):
    postgreAdd(name)
    return "Привет, " + name + " от Python!"

@app.get('/status')
async def getStatus():
    return {"status": "Ok"}

def postgreAdd(name):

    nowDate = datetime.now()
    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            dbname = dbname
        )

        with connection.cursor() as cursor:
            sql_query = "INSERT INTO py_greet (time, name) VALUES (%s, %s);"
            sql_data = (nowDate, name)
            cursor.execute(sql_query, sql_data)
            connection.commit()
            
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        if connection:
            connection.close()
            print("PostgreSQL connection is closed")

def postgreHistory():
    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            dbname = dbname
        )

        with connection.cursor() as cursor:
            sql_query = "SELECT * FROM py_greet LIMIT 10000;"
            cursor.execute(sql_query)
            return cursor.fetchall()
            
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        if connection:
            connection.close()
            print("PostgreSQL connection is closed")
