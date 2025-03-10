from src.generators import filter_by_currency
from src.generators import transaction_descriptions


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
    assert next(currency_gen) == []


# тестирование функции transaction_descriptions
def test_transaction_descriptions(transactions_list):
    transaction_gen = transaction_descriptions(transactions_list)
    assert 'Перевод организации' == next(transaction_gen)
    assert 'Перевод со счета на счет' == next(transaction_gen)
    assert 'Перевод со счета на счет' == next(transaction_gen)
    assert 'Перевод с карты на карту' == next(transaction_gen)
    assert 'Перевод организации' == next(transaction_gen)
