from typing import Any


def filter_by_currency(transactions: list[dict[str, Any]], currency: str):
    """ Фильтрует транзакции по валюте  """
    if not transactions:
        yield 'Транзакции отсутствуют'
    else:
        for transaction in transactions:
            if transaction["operationAmount"]["currency"].get('name') == currency:
                yield transaction
            else:
                yield 'Транзакции по заданной валюте не найдены'


def transaction_descriptions(transactions: list[dict[str, Any]]):
    """ Возвращает описание транзакции """
    if not transactions:
        yield 'Транзакции отсутствуют'
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int):
    """ Генератор, выдает номера банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ """
    if start > stop:
        raise ValueError("значение start должно быть меньше или равно значению stop")
    for number in range(start, stop + 1):
        number_card = str(number).zfill(16)
        formatted_card_number = (number_card[0:4]
                                 + " "
                                 + number_card[4:8]
                                 + " "
                                 + number_card[8:12]
                                 + " "
                                 + number_card[12:16])
        yield formatted_card_number
