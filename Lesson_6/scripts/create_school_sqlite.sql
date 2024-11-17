-- Шаг 1: Таблица для хранения информации о классах
CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,          -- Уникальный идентификатор класса
    grade INTEGER NOT NULL,                        -- Номер класса (например, 1, 2, 3)
    letter TEXT,                                   -- Буква класса (например, "А", "Б")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Дата создания записи
);

-- Шаг 2: Таблица для хранения информации о учениках
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,           -- Уникальный идентификатор ученика
    first_name TEXT NOT NULL,                       -- Имя ученика
    last_name TEXT NOT NULL,                        -- Фамилия ученика
    birthdate DATE,                                 -- Дата рождения
    gender TEXT,                                    -- Пол (M или F)
    class_id INTEGER,                               -- Идентификатор класса (ссылка на таблицу `classes`)
    address TEXT,                                   -- Адрес ученика
    phone TEXT,                                     -- Телефон ученика
    email TEXT,                                     -- Электронная почта ученика
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Дата добавления записи
    FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE SET NULL
);

-- Шаг 3: Таблица для хранения информации о преподавателях
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,          -- Уникальный идентификатор преподавателя
    first_name TEXT NOT NULL,                       -- Имя преподавателя
    last_name TEXT NOT NULL,                        -- Фамилия преподавателя
    subject TEXT,                                   -- Преподаваемый предмет
    phone TEXT,                                     -- Телефон преподавателя
    email TEXT,                                     -- Электронная почта преподавателя
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Дата добавления записи
);

-- Шаг 4: Таблица для хранения информации о предметах
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,          -- Уникальный идентификатор предмета
    name TEXT NOT NULL,                             -- Название предмета (например, "Математика")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Дата добавления предмета
);

-- Шаг 5: Таблица для хранения расписания уроков
CREATE TABLE IF NOT EXISTS schedules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,         -- Уникальный идентификатор записи
    class_id INTEGER,                              -- Идентификатор класса (ссылка на таблицу `classes`)
    teacher_id INTEGER,                            -- Идентификатор преподавателя (ссылка на таблицу `teachers`)
    subject_id INTEGER,                            -- Идентификатор предмета (ссылка на таблицу `subjects`)
    day_of_week TEXT,                              -- День недели (например, "Понедельник")
    start_time TIME,                               -- Время начала урока
    end_time TIME,                                 -- Время окончания урока
    FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);

-- Шаг 6: Таблица для хранения оценок учеников
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,        -- Уникальный идентификатор записи
    student_id INTEGER,                           -- Идентификатор ученика (ссылка на таблицу `students`)
    subject_id INTEGER,                           -- Идентификатор предмета (ссылка на таблицу `subjects`)
    grade INTEGER NOT NULL,                       -- Оценка
    date DATE NOT NULL,                           -- Дата выставления оценки
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);

-- Шаг 7: Таблица для учета посещаемости учеников
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,               -- Уникальный идентификатор записи
    student_id INTEGER,                                  -- Идентификатор ученика (ссылка на таблицу `students`)
    class_id INTEGER,                                    -- Идентификатор класса (ссылка на таблицу `classes`)
    date DATE NOT NULL,                                  -- Дата посещаемости
    status TEXT CHECK(status IN ('present', 'absent', 'late')) NOT NULL,  -- Статус посещаемости
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE
);

-- Шаг 8: Таблица для хранения информации о родителях учеников
CREATE TABLE IF NOT EXISTS parents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,            -- Уникальный идентификатор записи
    student_id INTEGER,                               -- Идентификатор ученика (ссылка на таблицу `students`)
    first_name TEXT NOT NULL,                         -- Имя родителя
    last_name TEXT NOT NULL,                          -- Фамилия родителя
    phone TEXT,                                        -- Телефон родителя
    email TEXT,                                        -- Электронная почта родителя
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);
