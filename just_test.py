import socket, select, string, sys
import json,os,ast
import mysql.connector
import urllib.request
import time
import 
import json
ip=''
port='80'
url_name='/i-switch/m2m_interval.php?'
url='http://'+ip+":"+port+url_name
from http.server import BaseHTTPRequestHandler, HTTPServer #if python 3 uncomment this line
#from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer #in python 2 we use this line
import time

# only for heartbeat interval
hostName = ""
pat="/var/www/html/m2mserver/hp_interval.json"
hostPort = 55555 #new port to be open

def heartbeat_interval_fun():
    
    try:
        
        sSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket successfully created")
    except:
        print ("Socket creation failed with error %s") %(err) 


    try:
        
        sSock.connect(('', ))
        print ("connection successful")
    except:
        print ("'Unable to connect %s'") %(err)
    with open (pat,"r+")as f:
    
        c=json.load(f)
        #c=ast.literal_eval(x)    
    hp_interval = c["heartbeat_interval"]
    hp_interval=str(hp_interval)
    sSock.send(hp_interval.encode())

    data = ''
    data = sSock.recv(1024).decode()
    print (data)
    if data[0:2] == '^03':
        hp_interval = int(data[5:8]) * 60

    sys.exit
 
    sSock.close() 



while True:
    try:


        #if(os.path.exists(pat)):
        		

        with open(pat,"r+") as f:

            data=json.load(f)
            mydb=mysql.connector.connect(host="localhost",user="",passwd="",database="m_to_m")
			my=mydb.cursor()
			sql_check="SELECT panel_id, panel_interval FROM heartbeat_interval"
			my.execute(sql_check)
			db_data=my.fetchall()
			for row in db_data:
						
				panel_id=row[0]
				panel_interval=str(row[1])
			for i in data:
						
				panel_id_from_server=panel_id
				panel_interval_from_server=i['panel_interval']
				
			if panel_interval!=panel_interval_from_server:
				sql_check="UPDATE heartbeat_interval SET panel_interval=%s WHERE panel_id=%s"
				my.execute(sql_check,(panel_interval_from_server,panel_id_from_server))
#exceutingquerytosql
				mydb.commit()
				print("panel_interval_updated")
			else:
					print("same_interval")

	except:
		print("not_done")



heartbeat_interval_fun()







   

try:
    myServer.serve_forever()

except KeyboardInterrupt:
    pass

 