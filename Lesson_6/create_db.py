import sqlite3
import os

# Функция для выполнения SQL скрипта из файла
def execute_sql_script(db_file, sql_file):
    # Создаем подключение к базе данных
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Открываем файл SQL и выполняем его содержимое
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_script = f.read()

    try:
        # Выполняем SQL-скрипт
        cursor.executescript(sql_script)
        conn.commit()
        print("База данных успешно создана и заполнена данными.")
    except sqlite3.Error as e:
        print(f"Ошибка при выполнении SQL: {e}")
    finally:
        # Закрываем соединение
        conn.close()

# Путь к файлу SQL и к базе данных
sql_file = r'C:\Users\egoro\PycharmProjects\Maestro7IT\Lesson_6\scripts\create_school_sqlite.sql'
db_file = 'school.db'  # Имя файла базы данных (можно указать полный путь)

# Проверка существования файла SQL
if not os.path.exists(sql_file):
    print(f"Файл {sql_file} не найден. Проверьте путь.")
else:
    # Выполняем создание базы данных
    execute_sql_script(db_file, sql_file)
