from app import db
from sqlalchemy import Column, String, Integer, Float

class Country(db.Model):
    __tablename__ = "countries"
    country_id = Column(Integer, primary_key=True)
    country_name = Column(String)
    capital = Column(String)
    area = Column(Float)