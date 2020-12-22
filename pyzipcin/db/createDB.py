from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from .constants import DB_URI

Base = declarative_base()
engine = create_engine(DB_URI, echo=True)


class ZipDetail(Base):
    __tablename__ = "zips"

    id = Column(Integer, primary_key=True)
    circlename = Column(String(250))
    regionname = Column(String(250))
    divisionname = Column(String(250))
    officename = Column(String(250))
    pincode = Column(Integer())
    officetype = Column(String(250))
    delivery = Column(String(250))
    district = Column(String(250))
    statename = Column(String(250))

    def as_dict(self):
        return {
            c.name: getattr(self, c.name)
            for c in self.__table__.columns
            if c.name != "id"
        }

    def __str__(self):
        return self.pincode


def createDB(DB_URI):
    engine = create_engine(DB_URI)
    Base.metadata.create_all(engine)
