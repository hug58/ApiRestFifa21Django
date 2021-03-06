import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


from dotenv import load_dotenv

import os
load_dotenv()

user:str = os.getenv('POSTGRES_USER')
password:str = os.getenv('POSTGRES_PASSWORD')
host:str = os.getenv('POSTGRES_HOST')
port:str = os.getenv('POSTGRES_PORT')
db_name:str = os.getenv('POSTGRES_DB')

engine = db.create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
    )
#

Session = scoped_session( sessionmaker(bind=engine) )
session = Session()

metadata = db.MetaData()

db_player = db.Table('player__fifa', metadata, autoload=True, autoload_with=engine)
db_team = db.Table('team__fifa', metadata, autoload=True, autoload_with=engine)


