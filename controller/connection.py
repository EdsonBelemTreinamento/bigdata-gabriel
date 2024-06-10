from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

load_dotenv()

user_pg = os.environ['usuario']
pswd_pg = os.environ['senha']

engine = create_engine(f'postgresql+psycopg2://{user_pg}:{pswd_pg}@localhost:5432/covid_vac')

Session = sessionmaker(bind=engine)
session = Session()
