from flask_sqlalchemy import SQLAlchemy
from GoingAwayToCollegeApp import app
from helper import sqlalchemyConfig
from sqlalchemy import create_engine

config = sqlalchemyConfig.SqlAlchemyConfig()
engine = create_engine(config.config())
con = engine.connect()
result = con.execute("SELECT * FROM `USUARIO`")
print('Resultado' + str(result))