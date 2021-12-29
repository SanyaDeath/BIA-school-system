![BIA-school-system workflow](https://github.com/SanyaDeath/BIA-school-system/actions/workflows/main.yml/badge.svg)

# BIA-school-system

Необходимо разработать систему для помощи школьникам в процессе изучения математики
Ученикам должна быть предоставлена возможность ввести в форму произвольное арифметическое выражение и предполагаемый результат,
система должна провалидировать выражение и проверить правильность вычисления.

### Технологии
- Python 3.9
- Django 4.0
- Docker-compose 3.7
- nginx 1.19.3
- postgres 12.4

### Перейти в папку с проектом:
```
cd BIA-school-system
```

### В папке **infra** создать файл .env с содержимым переменных окружения:

```
DEBUG=True                                  # Or False
ALLOWED_HOSTS=Any,host                      # Any,host,that,you,want,to,use
SECRET_KEY=some_string                      # Any string like beleberda
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Установка докер
https://docs.docker.com/engine/install/

### В папке **infra** запустите команду докер
``` docker-compose up -d --build  ``` Shell

### Соберите статику
``` docker-compose exec python manage.py collectstatic --noinput ``` Shell

### Миграции
``` docker-compose exec python manage.py migrate --noinput ``` Shell

### Введите команду для создания суперпользователя
``` docker-compose exec web python manage.py createsuperuser ``` Shell

### Введите команду для создания групп пользователей с правами
``` docker-compose exec web python manage.py create_group ``` Shell

### Заполнения базы начальными данными
``` docker-compose exec web python manage.py loaddata fixtures/data.json ``` Shell


### При переходе на http://127.0.0.1/ появится окно для логина
### данные для входа  
``` 
имя пользователя: teacher / student
пароль: adminadmin 
```
## подсказка:
``` при создании нового учителя или студента определите его в одну из соотвествующих групп (techers для учителей, students для учеников соответсвенно) ```

### что не успел реализовать: Поддержку скобок в выражении. 