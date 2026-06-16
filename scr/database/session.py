from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os import getenv
load_dotenv()

engine = create_engine(f'{getenv('sql_api')}')

Session_start = sessionmaker(bind=engine)