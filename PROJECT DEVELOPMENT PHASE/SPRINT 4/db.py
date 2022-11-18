 

import ibm_db
 
def dbconnect():
        
    hostname="9938aec0-8105-433e-8bf9-0fbb7e483086.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
    uid="xld30906"
    pwd="TnhtJjQ3hnB3YxA8"
    driver="{IBM DB2 ODBC DRIVER}"
    db="bludb"
    port="32459"
    cert="certificate.crt"
    dsn=(
            "DATABASE={0};"
            "HOSTNAME={1};"
            "PORT={2};"
            "UID={3};"
            "SECURITY=SSL;"
        "SSLServerCertificate={4};"
        "PWD={5};"
         
    ).format(db,hostname,port,uid,cert,pwd)
    
    try:
        db2=ibm_db.connect(dsn,"","")
        print("connected")
        return dsn
    except:
        print("unable to connect",ibm_db.conn_errormsg())

 