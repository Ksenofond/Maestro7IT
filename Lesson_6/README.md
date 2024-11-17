# Небольшой проект: создание базы данных для работы школы

Этот проект включает в себя базу данных для управления информацией о школе, включая данные о классах, учениках, преподавателях, расписаниях, оценках и посещаемости.

## Структура базы данных

База данных состоит из нескольких таблиц, каждая из которых хранит различные типы данных.
Описание каждой таблицы и ее полей представлено ниже.

### Таблицы

#### 1. `classes`
Таблица для хранения информации о классах школы.

- **id** (INT, AUTO_INCREMENT, PRIMARY KEY) — Уникальный идентификатор класса.
- **grade** (INT) — Номер класса (например, 1, 2, 3).
- **letter** (VARCHAR(1)) — Буква класса (например, "А", "Б").
- **created_at** (TIMESTAMP) — Дата создания записи.

#### 2. `students`
Таблица для хранения информации о учениках.

- **id** (INT, AUTO_INCREMENT, PRIMARY KEY) — Уникальный идентификатор ученика.
- **first_name** (VARCHAR(100)) — Имя ученика.
- **last_name** (VARCHAR(100)) — Фамилия ученика.
- **birthdate** (DATE) — Дата рождения.
- **gender** (CHAR(1)) — Пол ученика (M или F).
- **class_id** (INT) — Идентификатор класса, в котором учится ученик (ссылка на таблицу `classes`).
- **address** (TEXT) — Адрес ученика.
- **phone** (VARCHAR(15)) — Телефон ученика.
- **email** (VARCHAR(100)) — Электронная почта ученика.
- **created_at** (TIMESTAMP) — Дата добавления записи.

#### 3. `teachers`
Таблица для хранения информации о преподавателях.

- **id** (INT, AUTO_INCREMENT, PRIMARY KEY) — Уникальный идентификатор преподавателя.
- **first_name** (VARCHAR(100)) — Имя преподавателя.
- **last_name** (VARCHAR(100)) — Фамилия преподавателя.
- **subject** (VARCHAR(100)) — Преподаваемый предмет.
- **phone** (VARCHAR(15)) — Телефон преподавателя.
- **email** (VARCHAR(100)) — Электронная почта преподавателя.
- **created_at** (TIMESTAMP) — Дата добавления записи.

#### 4. `subjects`
Таблица для хранения информации о предметах.

- **id** (INT, AUTO_INCREMENT, PRIMARY KEY) — Уникальный идентификатор предмета.
- **name** (VARCHAR(100)) — Название предмета (например, "Математика").
- **created_at** (TIMESTAMP) — Дата добавления предмета.

#### 5. `schedules`
Таблица для хранения расписания уроков.

- **id** (INT, AUTO_INCREMENT, PRIMARY KEY) — Уникальный идентификатор записи.
- **class_id** (INT) — Идентификатор класса (ссылка на таблицу `classes`).
- **teacher_id** (INT) — Идентификатор преподавателя (ссылка на таблицу `teachers`).
- **subject_id** (INT) — Идентификатор предмета (ссылка на таблицу `subjects`).
- **day_of_week** (VARCHAR(20)) — День недели (например, "Понедельник").
- **start_time** (TIME) — Время начала урока.
- **end_time** (TIME) — Время окончания урока.

#### 6. `grades`
Таблица для хранения оценок учеников.

- **id** (INT, AUTO_INCREMENT, PRIMARY KEY) — Уникальный идентификатор записи.
- **student_id** (INT) — Идентификатор ученика (ссылка на таблицу `students`).
- **subject_id** (INT) — Идентификатор предмета (ссылка на таблицу `subjects`).
- **grade** (INT) — Оценка ученика.
- **date** (DATE) — Дата выставления оценки.

#### 7. `attendance`
Таблица для хранения информации о посещаемости учеников.

- **id** (INT, AUTO_INCREMENT, PRIMARY KEY) — Уникальный идентификатор записи.
- **student_id** (INT) — Идентификатор ученика (ссылка на таблицу `students`).
- **class_id** (INT) — Идентификатор класса (ссылка на таблицу `classes`).
- **date** (DATE) — Дата посещаемости.
- **status** (ENUM('present', 'absent', 'late')) — Статус посещаемости (присутствует, отсутствует, опоздал).

#### 8. `parents`
Таблица для хранения информации о родителях учеников.

- **id** (INT, AUTO_INCREMENT, PRIMARY KEY) — Уникальный идентификатор записи.
- **student_id** (INT) — Идентификатор ученика (ссылка на таблицу `students`).
- **first_name** (VARCHAR(100)) — Имя родителя.
- **last_name** (VARCHAR(100)) — Фамилия родителя.
- **phone** (VARCHAR(15)) — Телефон родителя.
- **email** (VARCHAR(100)) — Электронная почта родителя.

## Взаимосвязи между таблицами

1. **students** связаны с **classes** через поле `class_id`
2. **schedules** ссылаются на **classes**, **teachers** и **subjects** через внешние ключи `class_id`, `teacher_id` и `subject_id`
3. **grades** ссылаются на **students** и **subjects** через внешние ключи `student_id` и `subject_id`
4. **attendance** ссылается на **students** и **classes** через внешние ключи `student_id` и `class_id`
5. **parents** ссылаются на **students** через внешний ключ `student_id`

## Как использовать

1. Для создания базы данных выполните скрипт SQL, который находится в файле `create_database.sql`
2. Убедитесь, что у вас установлен MySQL или MariaDB.
3. Используйте SQL-скрипт для создания структуры базы данных.
4. Для взаимодействия с базой данных используйте предпочтительный инструмент или язык программирования (например, Python, PHP, Java).

## Заключение

Эта база данных предоставляет основу для управления данными в школьной системе.
Она охватывает информацию о студентах, преподавателях, предметах, расписаниях, оценках и посещаемости, что позволяет эффективно управлять школьным процессом.

**Авторы:** Егорова КП и Дуплей МИ

**Дата:** 17.11.2024