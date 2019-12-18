import requests

from ianapp.config import DATASETS, DATA_MOS_API_KEY, USERAGENT_COOKIE


def get_dataset_size():
    """ Дополняет справочник DATASETS дополнительной информацией о размере датасета.
    Информацию о размере датасета получает из api (источник https://apidata.mos.ru/Docs#datasetInfo).

    В каждый вложенный словарь в DATASETS создает ключ 'items_count' в который записывает
    значение полученное по ключу 'ItemsCount' из результата запроса.
    """

    # Копирует ключи справочника DATASETS в виде списка
    datasets = list(DATASETS.keys())

    params = {
        "api_key": DATA_MOS_API_KEY,
    }
    for set_id in datasets:
        url = f'https://apidata.mos.ru/v1/datasets/{set_id}'
        tmp = requests.get(url, params=params).json()
        tmp.headers['User-agent'] = USERAGENT_COOKIE
        DATASETS[set_id]['items_count'] = tmp['ItemsCount']

if __name__ == '__main__':
    get_dataset_size()
    print(DATASETS)
