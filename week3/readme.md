## REST 
(REpresentational State Transfer) is an architectural style, and an approach to communications that is often used in the development of Web services.

Данный репозитория содержит скрипты по развертыванию своего простого REST API c помощью FLASK. 

Напоминаю, что перед запуском нужно добавить в систему переменную FLASK_APP=file.py. На юникс системах это будет команда export 
на win это команда set. Далее запуск приложения осуществляестя через команду flask run в командной строке. 
<br>
После этого, вы можете делать запросы из питона, обращаясь к ip сервера, где запущено приложение. Если вы запустили на локально
на свой машине, то ваш ip это 127.0.0.1 или localhost. Порт по умолчанию стоит 5000. Протокол по умолчанию стоит http.

Соответственно, после запуска f_app4.py, можете по-очереди позапускать в питоне следующие команды: 
```python 
import requests

res = requests.get('http://127.0.0.1:5000/todo/api/v1/tasks/1')

print(res.status_code)

res.json()

## несуществующий ключ
res = requests.get('http://127.0.0.1:5000/todo/api/v1/tasks/3')

print(res.status_code)

res.json()
## все задачи
requests.get('http://127.0.0.1:5000/todo/api/v1/all_tasks').json()

## добавить задачу 

js = {'key2': 'new_object2'}

res = requests.post('http://127.0.0.1:5000/todo/api/v1/tasks', json=js)

## Проверка

requests.get('http://127.0.0.1:5000/todo/api/v1/all_tasks').json()
```
По всем вопросам пишите: 
telegram: @sergechuvakin

PS: отличныя тетрадка для обучения командам по командной строки: 

https://github.com/alexeyev/HSE-SPb-BigData-Python-Fall2016/blob/master/lesson08/lesson8_updated.ipynb
