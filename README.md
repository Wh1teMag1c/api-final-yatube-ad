# API для социальной сети Yatube

## Описание
Проект **Yatube API** предоставляет программный интерфейс для социальной сети. С его помощью пользователи могут публиковать записи, подписываться на авторов, оставлять комментарии и объединяться в сообщества. Проект поддерживает аутентификацию через JWT-токены и разграничение прав доступа.

**Ключевые возможности:**
* **Публикации:** Создание, просмотр, редактирование и удаление постов.
* **Комментарии:** Возможность комментировать записи и управлять своими комментариями.
* **Сообщества:** Просмотр информации о группах.
* **Подписки:** Система подписок на авторов с возможностью поиска.
* **Документация:** Интерактивная документация в формате Redoc.

## Технологии
* Python 3.9+
* Django 3.2.16
* Django REST Framework
* JWT (SimpleJWT)
* SQLite3

## Установка

1.  Клонируйте репозиторий:
    ```bash
    git clone [https://github.com/wh1temag1c/api-final-yatube-ad.git](https://github.com/wh1temag1c/api-final-yatube-ad.git)
    cd api-final-yatube-ad
    ```

2.  Cоздайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/scripts/activate  # Для Windows
    # source venv/bin/activate    # Для Linux/macOS
    ```

3.  Установите зависимости из файла requirements.txt:
    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4.  Выполните миграции:
    ```bash
    python manage.py migrate
    ```

5.  Запустите проект:
    ```bash
    python manage.py runserver
    ```

После запуска проект будет доступен по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
Документация Redoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)