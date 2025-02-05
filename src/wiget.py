import re
from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(card_number: str) -> str:
    """Функция маскировки как банковского счета, так и номера карты"""
    only_numbers = re.findall(r'\d+', card_number)
    str_only_numbers = ''.join(only_numbers)
    if 'Счет' in card_number:
        return get_mask_account(str_only_numbers)
    else:
        return get_mask_card_number(str_only_numbers)


def get_date(date_format: str) -> str:
    """Функция изменения формата даты"""
