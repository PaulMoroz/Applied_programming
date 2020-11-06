Лабораторна робота, виконана на ОС Linux Mint 19.3 TRICIA

Результати роботи будуть тут
Установка pipenv
```bash
pip install pipenv
```
Установка python 3.8 на віртуальне середовище
```bash
pipenv install --python 3.8
```
Установка Flask
```bash
pipenv install flask
```
Установка WSGI сервера(gunicorn)
```bash
pipenv install gunicorn
```
Запуск WSGI сервера 
```bash
gunicorn --bind 127.0.0.1:5000 wsgi:app
```

