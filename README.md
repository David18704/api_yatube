# api_yatube
api_yatube
### Задание:
 Создан REST API для Yatube. Через этот интерфейс смогут работать мобильное приложение или чат-бот; 
через него же можно будет передавать данные в любое приложение или на фронтенд.
### Установка:

*Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/David18704/api_yatube.git
```

```
cd api_yatube
```

*Cоздать и активировать виртуальное окружение:

```
python -m venv env (для Windows) или python3 -m venv venv (для Windows на Mac или Linux)
```

```
source venv/Scripts/activate (для Windows) или source venv/bin/activate (для macOS или Linux)
```

Установить зависимости из файла requirements.txt:


```
pip install -r requirements.txt
```

Запустить сервер :

```
python manage.py runserver (http://127.0.0.1:8000/admin) 
```
```
Отправляем запросы через приложение Postman:
api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.
api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
api/v1/groups/ (GET): получаем список всех групп.
api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.
api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.
```
