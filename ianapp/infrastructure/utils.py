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
        # у тебя здесь в цикле происходит создание сессии, добавление обьекта и коммит, это не оптимально.
        # создание сессии и коммит тяжелые операции
        # вместо этого тебе стоит сделать так - создаем сессию, далее в цикле проходимся по обьектам и добавляем их
        # в конце делаем коммит
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

    # функция write_to_db в твоем виде не переиспользуема. что, если я захочу записать в базу данных другую модель,
    # в которой поля отличны от модели Subway? Мне придется писать функцию write_to_db_2?
    # Пример того, как правильно -- ниже ps Загугли что такое **kwargs
    # учись писать более абстрактный код там где это надо
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


def write_to_db_the_right_way(model_class, **kwargs):
    new = model_class(**kwargs)
    session = Session()
    session.add(new)
    session.commit()
