from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ianapp.config import SQLALCHEMY_DATABASE_URI
from ianapp.infrastructure.models import Subway

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
Session = sessionmaker(bind=engine)


def save_infrastructure_to_db(response_text_in_json):
    """ Сохраняет json-данные в базу данных"""
    for data in response_text_in_json:
        write_to_db(
            global_id=data['Cells']['global_id'],
            station_name=data['Cells']['NameOfStation'],
            station_entry_name=data['Cells']['Name'],
            lon=data['Cells']['Longitude_WGS84'],
            lat=data['Cells']['Latitude_WGS84'],
            line=data['Cells']['Line'],
            date_of_record_in_the_database=datetime.today()
        )


def write_to_db(global_id, station_name, station_entry_name, lon, lat, line, date_of_record_in_the_database):
    """ Записывает построчно данные в таблицу realty"""
    new = Subway(
        global_id=global_id,
        station_name=station_name,
        station_entry_name=station_entry_name,
        lon=lon,
        lat=lat,
        line=line,
        date_of_record_in_the_database=date_of_record_in_the_database
    )

    session = Session()
    session.add(new)
    session.commit()
