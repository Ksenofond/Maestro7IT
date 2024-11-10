"""
📂 Приложение: "Блокнот на Flet" 🖥️

Flet: удобный фреймворк для создания приложений.
На нем можно создавать десктопные, мобильные и веб-приложения.

Flet основан на Flutter и предоставляет разработчикам готовые компоненты для конструирования GUI — графического интерфейса пользователя.
Создатели Flet не только используют готовые компоненты из Flutter, но и пишут свои.
Программы пока можно писать только на Python, но создатели обещают добавить и другие языки программирования.
"""

import flet as ft

ALLOW_MULTIPLE_FILES = False

def _(text: str) -> str:
    return text  # функция для перевода строк

# Создание кнопки открытия файла
def create_file_picker_button(on_click) -> ft.ElevatedButton:
    return ft.ElevatedButton(
        _("Open file"),
        icon=ft.icons.UPLOAD_FILE,
        on_click=on_click)

# Создание кнопки сохранения
def create_save_button(on_click) -> ft.ElevatedButton:
    return ft.ElevatedButton(
        _("Save file"),
        icon=ft.icons.SAVE,
        on_click=on_click)

# Функция для считывания содержимого открытого файла
def handle_file_picker_result(file_picker_result: ft.FilePickerResultEvent, text_field: ft.TextField):
    if file_picker_result.files:
        file = file_picker_result.files[0]
        with open(file.path, "r", encoding="utf-8") as f:
            content = f.read()
        text_field.value = content
    else:
        text_field.value = _("Completed")
    text_field.update()

# Функция для сохранения файла
def handle_save_file(text_field: ft.TextField):
    def save_file(file_picker_result: ft.FilePickerResultEvent):
        if file_picker_result.files:
            file = file_picker_result.files[0]
            with open(file.path, "w", encoding="utf-8") as f:
                f.write(text_field.value)
            text_field.value = _("Saved")
        else:
            text_field.value = _("Save failed")
        text_field.update()
    return save_file

# Основная функция программы
def main(page: ft.Page):
    page.title = 'Notepad Application'
    page.window_width = 1000
    page.window_height = 800
    file_picker_dialog = ft.FilePicker()
    save_file_dialog = ft.FilePicker()
    text_field = ft.TextField(multiline=True, height=600)  # create a multi-line text field

    file_picker_button = create_file_picker_button(
        lambda _: file_picker_dialog.pick_files(allow_multiple=ALLOW_MULTIPLE_FILES))

    save_button = create_save_button(
        lambda _: save_file_dialog.pick_files(allow_multiple=False))

    file_picker_dialog.on_result = lambda e: handle_file_picker_result(e, text_field)
    save_file_dialog.on_result = handle_save_file(text_field)

    page.overlay.append(file_picker_dialog)
    page.overlay.append(save_file_dialog)

    page.add(
        ft.Column(
            [
                file_picker_button,
                save_button,
                text_field,
            ]
        )
    )

# Запуск программы
ft.app(target=main)

''' Дата создания: 17.05.2024 '''
''' Преподаватель: Дуплей Максим Игоревич '''

''' Полезные ссылки: '''
# 1. 💠Telegram💠"Фишки программиста & UX/UI Дизайн": https://t.me/it_baza_znaniy
# 2. Хижина программиста: https://www.youtube.com/channel/UCqA5pl9NkVDrirMDlNVmU7g
# 3. Обучающие курсы на Stepik: https://stepik.org/users/150943726/teach

''' Контакты: '''
# 1. ▩ Номер телефона: +7-915-048-02-49
# 2. ▩ E-mail: maksimqwe42@mail.ru
