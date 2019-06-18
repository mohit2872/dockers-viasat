from flask import Flask
import psycopg2
import subprocess
import logging
import socket 

app = Flask(__name__)

@app.route('/')
def new_func():
    return "hello world "

@app.route('/hello')
def hello_world():
    logging.basicConfig(filename="logfilename.log", level=logging.INFO)         
    conn = None
    # from celery.contrib import rdb
    # rdb.set_trace()
    try:
        # hard coded SQL server IP address
        clean_ip = "172.18.0.3"
        conn = psycopg2.connect(host=clean_ip, database="counter", user="postgres", password="docker")

        cur = conn.cursor();

        cur.execute("SELECT * FROM  counter_table;")

        counter_arr = cur.fetchall()
        last_number = counter_arr[-1][0]
        last_number = last_number + 1
        
        cur.execute("INSERT INTO counter_table VALUES(" + str(last_number) + ");")
        conn.commit()

        cur.close()

        return str(last_number)
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        return error
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
