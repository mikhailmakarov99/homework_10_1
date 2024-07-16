from typing import Any


def filter_by_state(input_list: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция, сортирующая список по указанному ключу"""
    new_list = []

    for key in input_list:
        if key.get('state') == state_id:
            new_list.append(key)
    return new_list


def sort_by_date(input_list: list[dict[str, Any]], reverse=True) -> list[dict[str, Any]]:
    """Функция сортировки исходных данных по дате"""
    sorted_input_list = sorted(input_list, key=lambda input_list: input_list["date"], reverse=True)
    return sorted_input_list
