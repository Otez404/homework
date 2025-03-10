from src.processing import filter_by_state
from src.processing import sort_by_date


# проверка модуля wiget функции sort_by_date:
def test_sort_by_date(list_of_dicts_for_sort_by_date):
    assert sort_by_date(list_of_dicts_for_sort_by_date, True, ) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert sort_by_date(list_of_dicts_for_sort_by_date, False) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


def test_correct_date_for_sort(correct_list_of_dicts_for_sort_by_date):
    assert sort_by_date(correct_list_of_dicts_for_sort_by_date, True) == 'Введите дату в формате: год - месяц - день'


# проверка модуля wiget функции filter_by_state:
def test_filter_by_state(list_of_dicts_for_filter):
    assert filter_by_state(list_of_dicts_for_filter, 'EXECUTED') == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert filter_by_state(list_of_dicts_for_filter, 'CANCELED') == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_empty_filter_by_state(empty_list_of_dicts_for_filter):
    assert filter_by_state(empty_list_of_dicts_for_filter, ' ') == []