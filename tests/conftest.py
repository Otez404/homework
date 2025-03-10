import pytest


# проверка модуля masks функции get_mask_card_number:
@pytest.fixture()
def number_card_str():
    return '7000792289606361'


@pytest.fixture()
def number_card_int():
    return 7000792289606361


@pytest.fixture()
def correct_number_card():
    return '7023400792289606361'


@pytest.fixture()
def input_correct_number_card():
    return 'Visa 7023400792289606361'


# проверка модуля masks функции get_mask_account:
@pytest.fixture()
def account_number_str():
    return '73654108430135874305'


@pytest.fixture()
def account_number_int():
    return 73654108430135874305


@pytest.fixture()
def correct_account_number_str():
    return '732343654108430135874305'


# проверка модуля processing функции filter_by_state:
@pytest.fixture()
def list_of_dicts_for_filter():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture()
def empty_list_of_dicts_for_filter():
    return []


# проверка модуля processing функции sort_by_date:
@pytest.fixture()
def list_of_dicts_for_sort_by_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture()
def correct_list_of_dicts_for_sort_by_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019.07.03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018.06.30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018.09.12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018.10.14T08:21:33.419441'}]
