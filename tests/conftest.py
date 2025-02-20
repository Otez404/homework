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
