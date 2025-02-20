from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция маскировки номера банковской карты"""
    str_card_number = str(card_number)
    if str_card_number.isdigit():
        if len(str_card_number) != 16:
            return "Введен неверный номер карты"
        else:
            return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
    return "Введите только номер карты"


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция маскировки номера банковского счета"""
    str_account_number = str(account_number)
    if len(str_account_number) != 20:
        return "Введен неверный номер счета"
    else:
        return f"**{str_account_number[-4:]}"
