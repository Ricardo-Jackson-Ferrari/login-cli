from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import *
from .models.base import Base

url_coonection = 'sqlite:///projeto_login.db'

engine = create_engine(url_coonection)

Base.metadata.create_all(engine)


def get_session():
    Session = sessionmaker(bind=engine)
    return Session()
