
|ID|4|
| :- | :- |
|Заголовок|Создание объявления -  негативный тест3|
|Описание|Создание объявления со значением “price” <0|
|Входные данные|<p>"name": "Samsung Galaxy 10",<br>"price": -1,<br>"sellerId": 194231,<br>"statistics": {<br> "contacts": 10,<br> "likes": 10,<br> "viewCount": 10</p><p></p>|
|Ожидаемый результат|Статус 500 internal error|
|Реальный результат|Статус 200|
|Серьезность| Major|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/4.png)|


|ID|5|
| :- | :- |
|Заголовок|Создание объявления -  негативный тест4|
|Описание|Создание объявления со значением “price” None|
|Входные данные|<p>"name": "Samsung Galaxy 10",<br>"price":  None,<br>"sellerId": 194231,<br>"statistics": {<br> "contacts": 10,<br> "likes": 10,<br> "viewCount": 10</p><p></p>|
|Ожидаемый результат|Статус 500 internal error|
|Реальный результат|Статус 200|
|Серьезность| Major|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/5.png)|

|ID|7|
| :- | :- |
|Заголовок|Создание объявления -  негативный тест6|
|Описание|Создание объявления полем «name» = None|
|Входные данные|<p>"name": None,<br>"price": 84999,<br>"sellerId": 194231,<br>"statistics": {<br> "contacts": 10,<br> "likes": 10,<br> "viewCount": 10</p><p></p>|
|Ожидаемый результат|Статус 500 internal error|
|Реальный результат|Статус 200|
|Серьезность| Major|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/7.png)|

|ID|9|
| :- | :- |
|Заголовок|Создание объявления -  негативный тест8|
|Описание|Создание с отрицательными значениями в  «statistics»|
|Входные данные|<p>"name": "Samsung Galaxy 10",<br>"price": 84999,<br>"sellerId": 194231,<br>"statistics": {<br> "contacts": -10,<br> "likes": -10,<br> "viewCount": -10</p><p></p>|
|Ожидаемый результат|Статус 500 internal error|
|Реальный результат|Статус 200|
|Серьезность| Minor|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/9.png)|


|ID|10|
| :- | :- |
|Заголовок|Создание объявления -  негативный тест9|
|Описание|Создание с пустыми значениями в  «statistics»|
|Входные данные|<p>"name": "Samsung Galaxy 10",<br>"price": 84999,<br>"sellerId": 194231,<br>"statistics": {<br> "contacts": None,<br> "likes": None,<br> "viewCount": None</p><p></p>|
|Ожидаемый результат|Статус 500 internal error|
|Реальный результат|Статус 200|
|Серьезность| Minor|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/10.png)|


|ID|15|
| :- | :- |
|Заголовок|Получение всех объявлений по идентификатору продавца – негативный тест|
|Описание|Получение объявлений для несуществующего sellerID|
|Входные данные|nonexistent\_seller\_id = "FakeData"|
|Ожидаемый результат|Статус 404|
|Реальный результат|Статус 200|
|Серьезность| Major|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/15.png)|

