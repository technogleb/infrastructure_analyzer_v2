from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base2 = declarative_base()


class Realty(Base2):
    __tablename__ = 'realty'

    id = Column(Integer, primary_key=True)
    cian_id = Column(Integer, nullable=False)
    cian_price = Column(Integer, nullable=False)
    cian_lon = Column(String, nullable=False)
    cian_lat = Column(String, nullable=False)
    cian_added = Column(DateTime, nullable=False)
    date_of_record_in_the_database = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Realty(cian_id={self.cian_id},\
                        cian_price={self.cian_price},\
                        cian_lon={self.cian_lon},\
                        cian_lat={self.cian_lat})>"



