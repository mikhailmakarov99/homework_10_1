#**Проект: "Виджет банковских операций"** 
 
##**Описание:** 
 
Данный виджет отображает последние удачные операции по банковским картам. На данный момент разработки функционал включает в себя отображение номера карты\счета по зашифрованной маской, сортировкой операций по дате и отображению удачных или неудачных операций. 
 
##**Установка** 
 
1. Клонируйте репозиторий:
```
git clone https://github.com/mikhailmakarov99/homework_10_1.git
```
2. Установите зависимости:
``` 
pip install -r requirements.txt 
``` 
 
##**Использование** 
 
1. Импортируйте необходимые функции:
``` 
from your_module import filter_by_state, sort_by_date
```
2. Используйте функции в своем коде:
``` 
dict_list = [...]  # ваш список транзакций 
filtered_transactions = filter_by_state(dict_list, 'EXECUTED') 
sorted_transactions = sort_by_date(filtered_transactions) 
```         
     `