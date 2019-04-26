from flask import Flask
from flaskext.mysql import MySQL
from dbconfig import DBConfig

mysql = MySQL()

def createApp():
    app = Flask(__name__)
    
    #Mysql Configuration
    app.config['MYSQL_DATABASE_HOST'] = DBConfig.host
    app.config['MYSQL_DATABASE_DB'] = DBConfig.db
    app.config['MYSQL_DATABASE_USER'] = DBConfig.user
    app.config['MYSQL_DATABASE_PASSWORD'] = DBConfig.passwd
    app.config['JSON_AS_ASCII'] = False
    # related db to app
    mysql.init_app(app)
    return app
