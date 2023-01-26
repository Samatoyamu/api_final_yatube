Финальная версия REST API для YaTube  
=====

Описание
----------

API сервис для социальной сети Yatube 

Что было использовано в проекте
----------
* Python 3.9.10
* Django 3.2.16 
* Django Rest Framework
* Simple-JWT

Как этим всем пользоватся
----------

1. Клонируем проект, и переходим в него:
```bash
cd API_YaTube
```
2. Создаем и активируем виртуальное окружение:
```bash
python -m venv venv

source venv/Scripts/activate
```
3. Апгрейдим pip и устанавливаем зависимости:
```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```
4. Про миграций не забываем:
```bash
python manage.py migrate
```
5. И запускаем:
```bash
python3 manage.py runserver
```
Примеры иcпользования
----------
Документация доступна по адресу ```/redoc/```.
