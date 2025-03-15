import pytest

from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator


# тестирование функции filter_by_currency
def test_filter_by_currency(transactions_list):
    currency_gen = filter_by_currency(transactions_list, 'USD')
    assert next(currency_gen) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }
    assert next(currency_gen) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }


def test_filter_by_currency_empty():
    currency_gen = filter_by_currency([], 'USD')
    assert next(currency_gen) == 'Транзакции отсутствуют'


def test_filter_by_currency_only_rub(transactions_list_only_rub):
    currency_gen = filter_by_currency(transactions_list_only_rub, 'USD')
    assert next(currency_gen) == 'Транзакции по заданной валюте не найдены'


# тестирование функции transaction_descriptions
def test_transaction_descriptions(transactions_list):
    transaction_gen = transaction_descriptions(transactions_list)
    assert 'Перевод организации' == next(transaction_gen)
    assert 'Перевод со счета на счет' == next(transaction_gen)
    assert 'Перевод со счета на счет' == next(transaction_gen)
    assert 'Перевод с карты на карту' == next(transaction_gen)
    assert 'Перевод организации' == next(transaction_gen)


def test_transaction_descriptions_empty():
    transaction_gen = transaction_descriptions([])
    assert 'Транзакции отсутствуют' == next(transaction_gen)


def test_card_number_generator_invalid_range():
    with pytest.raises(ValueError, match="значение start должно быть меньше или равно значению stop"):
        next(card_number_generator(10, 5))


@pytest.mark.parametrize(
    "start, stop, results",
    [
        (1, 5, [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005"
        ]),
        (9999999999999990, 9999999999999995, [
            "9999 9999 9999 9990",
            "9999 9999 9999 9991",
            "9999 9999 9999 9992",
            "9999 9999 9999 9993",
            "9999 9999 9999 9994",
            "9999 9999 9999 9995"
        ]),
        (1234567890123456, 1234567890123456, [
            "1234 5678 9012 3456"
        ]),
        (0, 2, [
            "0000 0000 0000 0000",
            "0000 0000 0000 0001",
            "0000 0000 0000 0002"
        ]),
    ]
)
def test_card_number_generator(start, stop, results):
    generator = card_number_generator(start, stop)
    for expected, actual in zip(results, generator):
        assert actual == expected
