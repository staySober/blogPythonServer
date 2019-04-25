from flask import Flask
from flaskext.mysql import MySQL
from dbconfig import config, DBConfig

db = MySQL()

def createApp(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #Mysql Configuration
    app.config['MYSQL_DATABASE_HOST'] = DBConfig.host
    app.config['MYSQL_DATABASE_DB'] = DBConfig.db
    app.config['MYSQL_DATABASE_USER'] = DBConfig.user
    app.config['MYSQL_DATABASE_PASSWORD'] = DBConfig.passwd

    # related db to app
    db.init_app(app)



    return app