from sqlalchemy import Column, Integer, Float
from db import Base, engine


class AddressBook(Base):

    __tablename__ = "address_book"

    id = Column(Integer, primary_key=True, autoincrement=True)
    long = Column(Float)
    lat = Column(Float)