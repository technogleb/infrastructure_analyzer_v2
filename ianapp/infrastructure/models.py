from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base1 = declarative_base()


class Subway(Base1):
    __tablename__ = 'subway'

    id = Column(Integer, primary_key=True)
    global_id = Column(Integer, nullable=False)
    station_name = Column(String, nullable=False)
    station_entry_name = Column(String, nullable=False)
    lon = Column(String, nullable=False)
    lat = Column(String, nullable=False)
    line = Column(String, nullable=False)
    date_of_record_in_the_database = Column(DateTime, nullable=True)

    def __repr__(self):
        return f'<Subway(station_name={self.station_name},\
                        station_entry_name={self.station_entry_name},\
                        lon={self.lon},\
                        lat={self.lat})>'
