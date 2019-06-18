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
    # import pdb;+ pdb.set_trace()
    # from celery.contrib import rdb
    # rdb.set_trace()
    try:
        # getting ip address of the flask web server docker
        # hostname = socket.gethostname()
        # IPAddr = socket.gethostbyname(hostname)
        # print("IP address: " + IPAddr)
        # logging.info("IP Address of docker of flask web server is: " + IPAddr)

        # # getting ip address of the psql docker
        # ip_args = ['docker', 'inspect', '-f', "'{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'", 'pg-docker']
        # ip_addr = subprocess.check_output(ip_args)
        # clean_ip = ip_addr.decode().split("'")[1]
        # logging.info("Flask Web Server is connected to PostgreSQL server in docker at IP address: " + clean_ip)

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
