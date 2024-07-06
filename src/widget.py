from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_info: str) -> str:
    """Функция, которая принимает номер или счет карты и возвращает маску"""
    number_list = []
    letter_list = []
    card_info_list = card_info.split()
    for elem in card_info_list:
        if elem.isdigit():
            number_list.append(elem)
        elif elem.isalpha():
            letter_list.append(elem)
    # Проверка кол-ва символов, 16 == карта, 20 == счет
    symbol_number_list = "".join(number_list)
    len_symbol = len(symbol_number_list)
    # передаю подходящую по условию функцию
    if len_symbol == 16:
        mask_info_card = get_mask_card_number(int(symbol_number_list))
    elif len_symbol == 20:
        mask_info_card = get_mask_account(int(symbol_number_list))
    return f'{" ".join(letter_list)} {mask_info_card}'


def get_date(input_data: str) -> str:
    """Функция, которая меняет формат получаемой даты на "ДД.ММ.ГГГГ" """
    data_list = input_data.split("T")[0]
    formatted_data = f'{data_list[-2:]}.{data_list[5:7]}.{data_list[:4]}'
    return formatted_data












