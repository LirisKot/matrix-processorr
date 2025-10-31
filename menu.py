"""
Модуль меню - пример нисходящего проектирования
Итерация 3: Полная реализация функционала
"""

# Глобальная переменная для хранения данных
records = [
    {"id": 1, "name": "Пример записи 1", "description": "Это первая тестовая запись"},
    {"id": 2, "name": "Пример записи 2", "description": "Это вторая тестовая запись"}
]


def main():
    """Главная функция программы"""
    print("Добро пожаловать в систему управления записями!")

    while True:
        show_main_menu()
        choice = get_user_choice()

        if choice == "0":
            break

        process_choice(choice)
        input("\nНажмите Enter для продолжения...")

    print("До свидания!")


def show_main_menu():
    """Показать главное меню"""
    print("\n" + "=" * 20)
    print("=== ГЛАВНОЕ МЕНЮ ===")
    print("=" * 20)
    print("1. Показать все записи")
    print("2. Добавить новую запись")
    print("3. Удалить запись")
    print("4. Поиск записей")
    print("0. Выход")
    print("-" * 20)


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
        show_all_records()
    elif choice == "2":
        add_new_record()
    elif choice == "3":
        delete_record()
    elif choice == "4":
        search_records()


def show_all_records():
    """Показать все записи"""
    if not records:
        print("Нет доступных записей.")
        return

    print("\n--- Все записи ---")
    for record in records:
        print(f"ID: {record['id']}, Название: {record['name']}")
        print(f"   Описание: {record['description']}")
        print("-" * 30)


def add_new_record():
    """Добавить новую запись"""
    print("\n--- Добавление новой записи ---")

    name = input("Введите название записи: ").strip()
    if not name:
        print("Название не может быть пустым!")
        return

    description = input("Введите описание записи: ").strip()

    new_record = {
        "id": generate_new_id(),
        "name": name,
        "description": description
    }

    records.append(new_record)
    print("✓ Запись успешно добавлена!")


def generate_new_id():
    """Сгенерировать новый ID для записи"""
    if records:
        return max(record["id"] for record in records) + 1
    return 1


def delete_record():
    """Удалить запись"""
    if not records:
        print("Нет записей для удаления.")
        return

    print("\n--- Удаление записи ---")
    show_all_records()

    try:
        record_id = int(input("Введите ID записи для удаления: "))
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return

    success = remove_record(record_id)
    if success:
        print("✓ Запись успешно удалена!")
    else:
        print("✗ Запись с таким ID не найдена")


def remove_record(record_id):
    """Удалить запись по ID"""
    global records
    for i, record in enumerate(records):
        if record["id"] == record_id:
            del records[i]
            return True
    return False


def search_records():
    """Поиск записей"""
    print("\n--- Поиск записей ---")

    search_query = input("Введите поисковый запрос: ").strip().lower()
    if not search_query:
        print("Поисковый запрос не может быть пустым!")
        return

    results = perform_search(search_query)
    display_search_results(results)


def perform_search(query):
    """Выполнить поиск по имени и описанию"""
    results = []
    for record in records:
        if (query in record["name"].lower() or
                query in record["description"].lower()):
            results.append(record)
    return results


def display_search_results(results):
    """Показать результаты поиска"""
    if results:
        print(f"\n--- Найдено записей: {len(results)} ---")
        for record in results:
            print(f"ID: {record['id']}, Название: {record['name']}")
            print(f"   Описание: {record['description']}")
            print("-" * 30)
    else:
        print("Записи по вашему запросу не найдены.")


if __name__ == "__main__":
    main()