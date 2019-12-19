import requests

from ianapp.config import DATASETS, DATA_MOS_API_KEY, USERAGENT_COOKIE


def define_order_in_download_queue():
    """ Определяет в какой последовательности скачивать наборы данных.

    В каждый вложенный словарь в словаре DATASETS создает ключ 'items_count' в который записывает
    значение полученное по ключу 'ItemsCount' из результата api запроса.
    (api https://apidata.mos.ru/Docs#datasetInfo).

    В корне словаря DATASETS создает ключ 'order_in_download_queue',
    куда записывает список 'id' порядок которых опрееделяет значение доступное по ключу 'items_count'.
    Порядок в списке от меньшего к большему.
    """

    # Копирует ключи справочника DATASETS в виде списка
    datasets = list(DATASETS.keys())

    headers = {
        'User-Agent': USERAGENT_COOKIE,
    }
    params = {
        "api_key": DATA_MOS_API_KEY,
    }
    for set_id in datasets:
        url = f'https://apidata.mos.ru/v1/datasets/{set_id}'
        tmp = requests.get(url, params=params, headers=headers).json()
        DATASETS[set_id]['items_count'] = tmp['ItemsCount']

    # Сортировка (от меньшего к большему) вложенных словарей по количеству записей 'items_count' в каждом наборе
    tmp = sorted(DATASETS.items(), key=lambda x: x[1]['items_count'])
    # Добавление в справочник ключа 'order_in_download_queue', где
    # хранится последовательность для скачивания данных
    DATASETS['order_in_download_queue'] = list(map(lambda x: x[1]['id'], tmp))


if __name__ == '__main__':
    define_order_in_download_queue()
    print(DATASETS)
