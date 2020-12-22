from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
from .constants import DB_URI, FILE_PATH
from .createDB import ZipDetail, Base
from typing import Generator


def ZIP(filename: str) -> Generator:

    reader = open(f"{FILE_PATH}\{filename}")
    read = csv.reader(reader, delimiter=",", quotechar="|")

    for row in read:
        yield row


def populatedb():
    engine = create_engine(DB_URI, echo=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    total = 155600
    _iter = 0
    for j in ZIP("Pincode_30052019.csv"):
        _iter += 1
        new_zip = ZipDetail(
            circlename=j[0],
            regionname=j[1],
            divisionname=j[2],
            officename=j[3],
            pincode=j[4],
            officetype=j[5],
            delivery=j[6],
            district=j[7],
            statename=j[8],
        )
        session.add(new_zip)
        print((_iter / total) * 100)
    session.commit()


