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

Подготавливаемся и запускаем проект
----------

1. Клонируем проект,создаём вирутальное окружение и активируем:
```bash
cd api_final_yatube
python -m venv venv
source venv/Scripts/activate
```
2. Апгрейдим pip и устанавливаем зависимости:
```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```
3. Про миграций не забываем и запускаем:
```bash
cd yatube_api
python manage.py migrate
python manage.py runserver
```
Примеры иcпользования
----------
Для большинства запросов надо токен,поэтому создаём пользователя
```bash
/api/v1/users/
```
Получаем список постов
```bash
/api/v1/posts/
```
Или список сообществ
```bash
/api/v1/groups/
```
Нужен конкретный пост или сообщество? не проблема
```bash
/api/v1/posts/{id поста}/

/api/v1/groups/{id сообщества}/
```
Документация
----------
Доступна по адресу ```/redoc/```.
