def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты в виде числa и возвращает маску номера"""
    card_number_str = str(card_number)
    slice_cn = card_number_str[6:12]
    mask_card_number = card_number_str.replace(slice_cn, "******")
    mask_card_number_list = list(mask_card_number)
    mask_card_number_list.insert(4, " ")
    mask_card_number_list.insert(9, " ")
    mask_card_number_list.insert(14, " ")
    return " ".join(mask_card_number_list)


def get_mask_account(number_account: int) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера"""
    number_account_str = str(number_account)
    return "*" * 2 + number_account_str[-4:]
