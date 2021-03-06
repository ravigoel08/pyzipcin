from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from os import path
from ..db import Base

DB_URI = "sqlite:///" + path.join(path.dirname(path.abspath(__file__)), "database.db")

engine = create_engine(
    DB_URI, connect_args={"check_same_thread": False}, poolclass=StaticPool
)
Base.metadata.bind = engine
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
  