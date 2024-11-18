# Электронный дневник школы

Этот сайт - интерфейс для учеников школы. Здесь можно посмотреть оценки, расписание и прочую открытую информацию. Учителя заполняют базу данных через другой сайт. Ставят там оценки и т.д.

## Описание моделей

На сайте есть ученики: `Schoolkid`. Класс ученика определяется через комбинацию его полей `year_of_study` — год обучения и `group_letter` — литера класса. Вместе получается, например, 10А. Ученик связан со следующими моделями:

- `Mark` — оценка на уроке, от 2 до 5.
- `Commendation` — похвала от учителя, за особые достижения.
- `Chastisement` — замечание от учителя, за особые проступки.

Все 3 объекта связаны не только с учителем, который их создал, но и с учебным предметом (`Subject`). Примеры `Subject`:

- Математика 8 класса
- Геометрия 11 класса
- Русский язык 1 класса
- Русский язык 4 класса

`Subject` определяется не только названием, но и годом обучения, для которого учебный предмет проходит.

За расписание уроков отвечает модель `Lesson`. Каждый объект `Lesson` — урок в расписании. У урока есть комбинация `year_of_study` и `group_letter`, благодаря ей можно узнать для какого класса проходит этот урок. У урока есть `subject` и `teacher`, которые отвечают на вопросы "что за урок" и "кто ведёт". У урока есть `room` — номер кабинета, где он проходит. Урок проходит в дату `date`.

Расписание в школе строится по слотам:

- 8:00-8:40 — 1 урок
- 8:50-9:30 — 2 урок
- ...

У каждого `Lesson` есть поле `timeslot`, которое объясняет, какой номер у этого урока в расписании.

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE_NAME` — путь до базы данных, например: `schoolbase.sqlite3`

## Как запустить

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте БД командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

## Использование функций

Файл `script.py` содержит функции, которые помогут исправить оценки, удалить замечания и создать хороший комментарий от учителя.

Чтобы воспользоваться функциями необходимо в терминале запустить интерактивный режим Django shell:

`python3 manage.py shell`

Далее нужно будет подключить скрипты в терминале: 

`from script import *`

Затем запустите необходимую функцию для вас:

- Функция изменяет все плохие оценки на 5 для заданного ученика:
    ```
    fix_marks(child)
    ```
  - Функция удаляет все замечания для заданного ученика.
    ```
    remove_chastisement(child)
    ```
  - Функция создает похвалы от учителя по определенному предмету для заданного ученика.
    ```
    create_commendation(child, subject)
    ```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
