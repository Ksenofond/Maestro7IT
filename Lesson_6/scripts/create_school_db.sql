-- Шаг 1: Создание базы данных
CREATE DATABASE school;
USE school;

-- Шаг 2: Таблица для хранения информации о классах
CREATE TABLE classes (
    id INT AUTO_INCREMENT PRIMARY KEY,              -- Уникальный идентификатор класса
    grade INT NOT NULL,                             -- Номер класса (например, 1, 2, 3)
    letter VARCHAR(1),                              -- Буква класса (например, "А", "Б")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Дата создания записи
);

-- Шаг 3: Таблица для хранения информации о учениках
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,              -- Уникальный идентификатор ученика
    first_name VARCHAR(100) NOT NULL,               -- Имя ученика
    last_name VARCHAR(100) NOT NULL,                -- Фамилия ученика
    birthdate DATE,                                 -- Дата рождения
    gender CHAR(1),                                 -- Пол (M или F)
    class_id INT,                                   -- Идентификатор класса (ссылка на таблицу `classes`)
    address TEXT,                                   -- Адрес ученика
    phone VARCHAR(15),                              -- Телефон ученика
    email VARCHAR(100),                             -- Электронная почта ученика
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Дата добавления записи
    FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE SET NULL
);

-- Шаг 4: Таблица для хранения информации о преподавателях
CREATE TABLE teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,             -- Уникальный идентификатор преподавателя
    first_name VARCHAR(100) NOT NULL,              -- Имя преподавателя
    last_name VARCHAR(100) NOT NULL,               -- Фамилия преподавателя
    subject VARCHAR(100),                          -- Преподаваемый предмет
    phone VARCHAR(15),                             -- Телефон преподавателя
    email VARCHAR(100),                            -- Электронная почта преподавателя
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Дата добавления записи
);

-- Шаг 5: Таблица для хранения информации о предметах
CREATE TABLE subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,             -- Уникальный идентификатор предмета
    name VARCHAR(100) NOT NULL,                    -- Название предмета (например, "Математика")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Дата добавления предмета
);

-- Шаг 6: Таблица для хранения расписания уроков
CREATE TABLE schedules (
    id INT AUTO_INCREMENT PRIMARY KEY,            -- Уникальный идентификатор записи
    class_id INT,                                 -- Идентификатор класса (ссылка на таблицу `classes`)
    teacher_id INT,                               -- Идентификатор преподавателя (ссылка на таблицу `teachers`)
    subject_id INT,                               -- Идентификатор предмета (ссылка на таблицу `subjects`)
    day_of_week VARCHAR(20),                      -- День недели (например, "Понедельник")
    start_time TIME,                              -- Время начала урока
    end_time TIME,                                -- Время окончания урока
    FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);

-- Шаг 7: Таблица для хранения оценок учеников
CREATE TABLE grades (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Уникальный идентификатор записи
    student_id INT,                          -- Идентификатор ученика (ссылка на таблицу `students`)
    subject_id INT,                          -- Идентификатор предмета (ссылка на таблицу `subjects`)
    grade INT NOT NULL,                      -- Оценка
    date DATE NOT NULL,                      -- Дата выставления оценки
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);

-- Шаг 8: Таблица для учета посещаемости учеников
CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,                 -- Уникальный идентификатор записи
    student_id INT,                                    -- Идентификатор ученика (ссылка на таблицу `students`)
    class_id INT,                                      -- Идентификатор класса (ссылка на таблицу `classes`)
    date DATE NOT NULL,                                -- Дата посещаемости
    status ENUM('present', 'absent', 'late') NOT NULL, -- Статус посещаемости (присутствует, отсутствует, опоздал)
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE
);

-- Шаг 9: Таблица для хранения информации о родителях учеников
CREATE TABLE parents (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Уникальный идентификатор записи
    student_id INT,                          -- Идентификатор ученика (ссылка на таблицу `students`)
    first_name VARCHAR(100) NOT NULL,        -- Имя родителя
    last_name VARCHAR(100) NOT NULL,         -- Фамилия родителя
    phone VARCHAR(15),                       -- Телефон родителя
    email VARCHAR(100),                      -- Электронная почта родителя
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);

-- Пример вставки данных (по желанию)
-- Вставка данных в таблицу классов
INSERT INTO classes (grade, letter) VALUES (1, 'A');
INSERT INTO classes (grade, letter) VALUES (1, 'B');

-- Вставка данных в таблицу студентов
INSERT INTO students (first_name, last_name, birthdate, gender, class_id, address, phone, email)
VALUES ('Иван', 'Иванов', '2009-05-15', 'M', 1, 'Москва, ул. Примерная, д. 1', '1234567890', 'ivanov@example.com');

-- Вставка данных в таблицу преподавателей
INSERT INTO teachers (first_name, last_name, subject, phone, email)
VALUES ('Мария', 'Петрова', 'Математика', '0987654321', 'petrova@example.com');

-- Вставка данных в таблицу предметов
INSERT INTO subjects (name) VALUES ('Математика');
INSERT INTO subjects (name) VALUES ('Русский язык');

-- Вставка данных в таблицу расписания
INSERT INTO schedules (class_id, teacher_id, subject_id, day_of_week, start_time, end_time)
VALUES (1, 1, 1, 'Понедельник', '08:00', '09:30');

-- Вставка данных в таблицу оценок
INSERT INTO grades (student_id, subject_id, grade, date)
VALUES (1, 1, 5, '2024-11-17');

-- Вставка данных в таблицу посещаемости
INSERT INTO attendance (student_id, class_id, date, status)
VALUES (1, 1, '2024-11-17', 'present');

-- Вставка данных в таблицу родителей
INSERT INTO parents (student_id, first_name, last_name, phone, email)
VALUES (1, 'Елена', 'Иванова', '9876543210', 'ivanova@example.com');
