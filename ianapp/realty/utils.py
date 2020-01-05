from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ianapp.config import SQLALCHEMY_DATABASE_URI
from ianapp.realty.models import Realty


def pack_to_json(response_results_dict: dict):
    """ Конвертирует reauests.text в json и возвращает словарь, где
    key это квадранты, а value полученные данные в виде json
    На вход получает словарь с результатами запросов
    """
    # можно было проще
    # return {square: response_obj.json() for square, response_obj in response_results_dict.items()}
    response_text_in_json = {}
    for square, response_obj in response_results_dict.items():
        response_text_in_json[square] = response_obj.json()
    return response_text_in_json


def save_realty_to_db(response_text_in_json: dict):
    """ Сохраняет json-данные в базу данных"""
    for square, json_data in response_text_in_json.items():
        for data in json_data['data']['offers']:
            write_to_db(
                cian_id=data['cian_id'],
                cian_price=data['price'],
                cian_lon=data['lon'],
                cian_lat=data['lat'],
                cian_added=datetime.fromtimestamp(data['added']),
                date_of_record_in_the_database=datetime.today(),
            )


def write_to_db(cian_id, cian_price, cian_lon, cian_lat, cian_added, date_of_record_in_the_database):
    """ Записывает построчно данные в таблицу realty"""
    #  те же замечание про добавление в цикле и переиспользуемость кода, что и в модуле infrastructure
    new = Realty(
        cian_id=cian_id,
        cian_price=cian_price,
        cian_lon=cian_lon,
        cian_lat=cian_lat,
        cian_added=cian_added,
        date_of_record_in_the_database=date_of_record_in_the_database
    )

    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(new)
    session.commit()


if __name__ == '__main__':
    write_to_db(
        cian_id=195533839,
        cian_price=21000.0,
        cian_lon=37.468102,
        cian_lat=55.627316,
        cian_added=datetime.fromtimestamp(1576062805),
        date_of_record_in_the_database=datetime.today(),
    )
