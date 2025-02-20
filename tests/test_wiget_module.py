import pytest

from src.wiget import get_date
from src.wiget import mask_account_card


# проверка модуля wiget функции mask_account_card:
@pytest.mark.parametrize('card_or_account_number,expected_result', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('Счет 64435686473678894779589', 'Счет Введен неверный номер счета'),
    ('Maestro 15968378685705199', 'Maestro Введен неверный номер карты')])
def test_mask_account_card(card_or_account_number, expected_result):
    assert mask_account_card(card_or_account_number) == expected_result


# проверка модуля get_date функции mask_account_card:
@pytest.mark.parametrize('input_date,result', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2025-09-13T02:26:18.671407', '13.09.2025'),
    ('25.10.2023', 'Введите дату в формате: год - месяц - день')])
def test_get_date(input_date, result):
    assert get_date(input_date) == result
