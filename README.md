![BIA-school-system workflow](https://github.com/SanyaDeath/BIA-school-system/actions/workflows/main.yml/badge.svg)

# BIA-school-system

Необходимо разработать систему для помощи школьникам в процессе изучения математики
Ученикам должна быть предоставлена возможность ввести в форму произвольное арифметическое выражение и предполагаемый результат,
система должна провалидировать выражение и проверить правильность вычисления.

### В папке **...** создать файл .env с содержимым переменных окружения:

```
DEBUG=True                                  # Or False
ALLOWED_HOSTS=Any,host                      # Any,host,that,you,want,to,use
SECRET_KEY=some_string                      # Any string like beleberda
```

### В папке **BIA-school-system** создайте виртуальное окружение и установите зависимости:
``` pip install -r requirements.txt ``` Python

### Перейдите в папку **school_system** и введите команду для создания суперпользователя:
``` python manage.py createsuperuser ``` Python

### В папке **school_system** введите команду для создания групп пользователей с правами:
``` python manage.py create_group ``` Python

### В папке **school_system** введите команду для запуска сервера:
``` python manage.py runserver ``` Python