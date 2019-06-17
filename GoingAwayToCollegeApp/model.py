#app dependencies
from GoingAwayToCollegeApp import app
#SQLAlcuemy Configuring/Connecting dependencies
from flask_sqlalchemy import SQLAlchemy
from helper import sqlalchemyConfig
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#SQLAlchemy DML dependencies
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref

#Configuring/Connecting SQLAlchemy
config = sqlalchemyConfig.SqlAlchemyConfig()
engine = create_engine(config.config())
Base = declarative_base()

class Profile(Base):
    print('It\' getting into Profile Class' )
    __tablename__ = 'PROFILE'
    id = Column(Integer, primary_key = True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key = True)
    profileid = Column(Integer, ForeignKey('profile.id'))
    first_name = (String)
    last_name = (String)
    dni = (String)

Session = sessionmaker(bind=engine)
#session = Session()

#con = engine.connect()
#result = con.execute("SELECT * FROM `USUARIO`")
#print('Resultado' + str(result))

