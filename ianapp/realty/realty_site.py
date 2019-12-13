from requests import Request, session
from time import sleep
from urllib.parse import urlencode

from ianapp.config import URL, USERAGENT_COOKIE, prepare_params


def prepare_request_obj():
    """Создает словарь с объектами requests, готовыми для отправки.
    Ключи в словаре соответствуют наименованиям квадрантов, из которых забираем объявления.
    """
    prepared_requests = {}
    # Получили словарь с параметрами запроса по api
    prepared_params: dict = prepare_params(deal_type='rent')

    for key, params in prepared_params.items():
        # Подготовили uri, где заменяем обратно на запятые перекодированные запятые
        query = urlencode(params).replace('%2C', ',')
        request = Request(method='get', url=URL, params=query).prepare()
        request.headers['User-agent'] = USERAGENT_COOKIE
        prepared_requests[key] = request
    return prepared_requests


def get_realty_data_obj():
    """Делает запросы по api.
    Отдает полученные по api ответы в виде объектов.
    """
    responses = {}
    prepared_requests = prepare_request_obj()
    s = session()
    for square, request in prepared_requests.items():
        tmp = s.send(request)
        responses[square] = tmp
        sleep(7)
    return responses
