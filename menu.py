"""
Модуль меню - пример нисходящего проектирования
"""

def main():
    """Главная функция программы"""
    print("Добро пожаловать в меню!")

    while True:
        show_main_menu()
        choice = get_user_choice()

        if choice == "0":
            break

        process_choice(choice)
        print("-" * 30)

    print("До свидания!")

def show_main_menu():
    """Показать главное меню"""
    print("\n" + "="*20)
    print("=== ГЛАВНОЕ МЕНЮ ===")
    print("="*20)
    print("1. Показать все опции")
    print("2. Добавить новую запись")
    print("3. Удалить запись")
    print("4. Поиск")
    print("0. Выход")
    print("-"*20)

def get_user_choice():
    """Получить выбор пользователя"""
    while True:
        choice = input("Выберите пункт меню: ")
        if validate_choice(choice):
            return choice
        else:
            print("Неверный выбор! Попробуйте снова.")

def validate_choice(choice):
    """Проверить корректность выбора"""
    valid_choices = ["0", "1", "2", "3", "4"]
    return choice in valid_choices

def process_choice(choice):
    """Обработать выбор пользователя"""
    if choice == "1":
        show_all_options()
    elif choice == "2":
        add_new_record()
    elif choice == "3":
        delete_record()
    elif choice == "4":
        search_records()

def show_all_options():
    """Показать все опции"""
    options = get_all_options()
    display_options(options)

def get_all_options():
    """Получить все опции (заглушка)"""
    return ["Опция 1", "Опция 2", "Опция 3"]

def display_options(options):
    """Отобразить список опций"""
    print("\n--- Доступные опции ---")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

def add_new_record():
    """Добавить новую запись"""
    record_data = get_record_data_from_user()
    success = save_record(record_data)
    show_result(success, "запись успешно добавлена", "ошибка добавления")

def get_record_data_from_user():
    """Получить данные записи от пользователя"""
    return "данные записи"

def save_record(record_data):
    """Сохранить запись (заглушка)"""
    return True

def delete_record():
    """Удалить запись"""
    record_id = get_record_id_from_user()
    success = remove_record(record_id)
    show_result(success, "запись успешно удалена", "ошибка удаления")

def get_record_id_from_user():
    """Получить ID записи от пользователя (заглушка)"""
    return "id записи"

def remove_record(record_id):
    """Удалить запись (заглушка)"""
    return True

def search_records():
    """Поиск записей"""
    search_query = get_search_query()
    results = perform_search(search_query)
    display_search_results(results)

def get_search_query():
    """Получить поисковый запрос (заглушка)"""
    return "поисковый запрос"

def perform_search(query):
    """Выполнить поиск (заглушка)"""
    return ["результат 1", "результат 2"]

def display_search_results(results):
    """Показать результаты поиска"""
    if results:
        print("\n--- Результаты поиска ---")
        for result in results:
            print(f"- {result}")
    else:
        print("Ничего не найдено.")

def show_result(success, success_msg, error_msg):
    """Показать результат операции"""
    if success:
        print(f"✓ {success_msg}")
    else:
        print(f"✗ {error_msg}")

if __name__ == "__main__":
    main()