from datetime import datetime as dt


def filter_by_state(list_of_dict: list[dict], state='EXECUTED') -> list[dict]:
    """Функция возращения списка словарей по опциональному значению ключа """
    result_list = []
    for word in list_of_dict:
        if word.get('state') == state:
            result_list.append(word)
    return result_list


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))


def sort_by_date(list_of_dict: list[dict], ascending=True) -> list[dict]:
    return sorted(list_of_dict, key=lambda x: dt.strptime(x['date'][0:10], '%Y-%m-%d'), reverse=ascending)



