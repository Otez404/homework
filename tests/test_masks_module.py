from src.masks import get_mask_card_number
from src.masks import get_mask_account

# тесты функции get_mask_card_number:
def test_mask_card_number_str(number_card_str):
    assert get_mask_card_number(number_card_str) == '7000 79** **** 6361'


def test_mask_card_number_int(number_card_int):
    assert get_mask_card_number(number_card_int) == '7000 79** **** 6361'


def test_correct_card_number(correct_number_card):
    assert get_mask_card_number(correct_number_card) == "Введен неверный номер карты"

def test_input_correct_card_number(input_correct_number_card):
    assert get_mask_card_number(input_correct_number_card) == "Введите только номер карты"

# тесты функции get_mask_account:
def test_mask_account_number_str(account_number_str):
    assert get_mask_account(account_number_str) == '**4305'


def test_mask_account_number_int(account_number_int):
    assert get_mask_account(account_number_int) == '**4305'

def test_correct_mask_account_number(correct_account_number_str):
    assert get_mask_account(correct_account_number_str) == "Введен неверный номер счета"
