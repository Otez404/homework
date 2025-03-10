from datetime import datetime as dt
from typing import Any


def filter_by_state(list_of_dicts: list[dict[str, Any]], state: str = 'EXECUTED') -> list[dict[str, Any]]:
    """ Функция возращения списка словарей по опциональному значению ключа """
    result_list = []
    for word in list_of_dicts:
        if word.get('state') == state:
            result_list.append(word)
    return result_list


def sort_by_date(list_of_dicts: list[dict[str, Any]], descending: bool = True) -> Any:
    """ Функция сортировки списка словарей по дате """
    try:
        sorted(list_of_dicts, key=lambda x: dt.strptime(x['date'][0:10], '%Y-%m-%d'), reverse=descending)
    except ValueError:
        return 'Введите дату в формате: год - месяц - день'
    else:
        return sorted(list_of_dicts, key=lambda x: dt.strptime(x['date'][0:10], '%Y-%m-%d'), reverse=descending)
