from pydo import Client
from pydo.operations import AccountOperations
import time
from resources.project import Project
from resources.database import PGDB
from resources.application import App

with open("key.txt", "r") as file:
    token = file.read()
project=Project(token,'sendbox')
print(project.create())
#time.sleep(5)
#print(project.delete())
#create database
db=PGDB(token,'sandbox-db','sendbox')
print(db.project.project_id)
if not db.exists:
    print("doesnt exist")
    print(db.create_db_cluster())
else:
    if db.dbproperties['status']=='creating':
        print("CREATING")
    #print(db.dbproperties)
    #print(db.delete_db_cluster())
app=App(token,'geoserver3','sendbox')  
print(app.create_app())
#print(app._getallApps())    
#create geoserver app

    #print(db.create_db_cluster())
#show databases
#db_list=client.databases.list_clusters()
#for d in db_list['databases']:
#    print(d)