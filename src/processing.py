from datetime import datetime as dt


def filter_by_state(list_of_dict: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """ Функция возращения списка словарей по опциональному значению ключа """
    result_list = []
    for word in list_of_dict:
        if word.get('state') == state:
            result_list.append(word)
    return result_list


def sort_by_date(list_of_dict: list[dict], ascending: bool = True) -> list[dict]:
    """ Функция сортировки списка словарей по дате """
    return sorted(list_of_dict, key=lambda x: dt.strptime(x['date'][0:10], '%Y-%m-%d'), reverse=ascending)
