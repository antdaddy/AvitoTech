|ID|1|
| :- | :- |
|Заголовок|Создание объявления - позитивный тест|
|Описание|Успешное создание объявления с корректными данными|
|Входные данные|<p>""name": "Samsung Galaxy 10",<br>"price": 84999,<br>"sellerId":194231,<br>"statistics": {<br> "contacts": 10,<br> "likes": 10,<br> "viewCount": 10</p><p></p><p></p>|
|Ожидаемый результат|Статус 200 OK|
|Реальный результат|Статус 200 OK|
|Серьезность|-|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/1.png)|

















|ID|2|
| :- | :- |
|Заголовок|Создание объявления -  негативный тест1|
|Описание|Создание объявления с пустыми полями|
|Входные данные|-|
|Ожидаемый результат|Статус 500 internal error|
|Реальный результат|Статус 500 internal error|
|Серьезность|-|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/2.png)|


















|ID|3|
| :- | :- |
|Заголовок|Создание объявления -  негативный тест2|
|Описание|Создание объявления с полем “price” типа string (текст вместо цены)|
|Входные данные|<p>"name": "Samsung Galaxy 10",<br>"price": "text",<br>"sellerId": 194231,<br>"statistics": {<br> "contacts": 10,<br> "likes": 10,<br> "viewCount": 10</p><p></p>|
|Ожидаемый результат|Статус 500 internal error|
|Реальный результат|Статус 500 internal error|
|Серьезность|-|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/3.png)|














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
















|ID|6|
| :- | :- |
|Заголовок|Создание объявления -  негативный тест5|
|Описание|Создание объявления со значением “price” >9223372036854775807|
|Входные данные|<p>"name": "Samsung Galaxy 10",<br>"price":  9223372036854775808,<br>"sellerId": 194231,<br>"statistics": {<br> "contacts": 10,<br> "likes": 10,<br> "viewCount": 10</p><p></p>|
|Ожидаемый результат|Статус 500 internal error|
|Реальный результат|Статус 500 internal error|
|Серьезность| -|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/6.png)|
















|ID|7|
| :- | :- |
|Заголовок|Создание объявления -  негативный тест6|
|Описание|Создание объявления полем «name» = None|
|Входные данные|<p>"name": None,<br>"price": 84999,<br>"sellerId": 194231,<br>"statistics": {<br> "contacts": 10,<br> "likes": 10,<br> "viewCount": 10</p><p></p>|
|Ожидаемый результат|Статус 500 internal error|
|Реальный результат|Статус 200|
|Серьезность| Major|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/7.png)|















|ID|8|
| :- | :- |
|Заголовок|Создание объявления -  негативный тест7|
|Описание|Создание объявления полем «name» типа int|
|Входные данные|<p>"name": 123,<br>"price": 84999,<br>"sellerId": 194231,<br>"statistics": {<br> "contacts": 10,<br> "likes": 10,<br> "viewCount": 10</p><p></p>|
|Ожидаемый результат|Статус 500 internal error|
|Реальный результат|Статус 500 internal error|
|Серьезность| -|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/8.png)|
















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
















|ID|11|
| :- | :- |
|Заголовок|Получение объявления по его идентификатору - позитивный тест|
|Описание|Успешное получение объявления по существующему идентификатору|
|Входные данные|<p>item\_id = '69a0e4dc-56b7-41f7-9f25-8153eb943fb3'</p><p></p>|
|Ожидаемый результат|Статус 200|
|Реальный результат|Статус 200|
|Серьезность| -|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/11.png)|



















|ID|12|
| :- | :- |
|Заголовок|Получение объявления по его идентификатору - негативный тест|
|Описание|Создание запроса с несуществующим идентификатором|
|Входные данные|<p>item\_id = '0010010100010010010'</p><p></p>|
|Ожидаемый результат|Статус 404|
|Реальный результат|Статус 404|
|Серьезность| -|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/12.png)|



















|ID|13|
| :- | :- |
|Заголовок|Получение объявления по его идентификатору - негативный тест2|
|Описание|Создание запроса с идентификатором типа string|
|Входные данные|<p>item\_id = "NotRealId"</p><p></p>|
|Ожидаемый результат|Статус 404|
|Реальный результат|Статус 404|
|Серьезность| -|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/13.png)|














|ID|14|
| :- | :- |
|Заголовок|Получение всех объявлений по идентификатору продавца - позитивный тест|
|Описание|Успешное получение всех объявлений для существующего sellerID|
|Входные данные|<p>UNIQUE\_SELLER\_ID = 194231</p><p></p>|
|Ожидаемый результат|Статус 200|
|Реальный результат|Статус 200|
|Серьезность| -|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/14.png)|



















|ID|15|
| :- | :- |
|Заголовок|Получение всех объявлений по идентификатору продавца – негативный тест|
|Описание|Получение объявлений для несуществующего sellerID|
|Входные данные|nonexistent\_seller\_id = "FakeData"|
|Ожидаемый результат|Статус 404|
|Реальный результат|Статус 200|
|Серьезность| Major|
|Скрин |![Image alt](https://github.com/antdaddy/AvitoTech/blob/main/2task/15.png)|

