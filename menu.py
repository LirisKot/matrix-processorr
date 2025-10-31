"""
Модуль меню - пример нисходящего проектирования
Итерация 3: Полная реализация структуры, алгоритм - заглушка
"""

# Глобальные переменные для хранения данных
matrix = None
result_matrix = None


def main():
    """Главная функция программы"""
    print("Добро пожаловать в систему обработки матриц!")

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
    print("\n" + "=" * 40)
    print("=== СИСТЕМА ОБРАБОТКИ МАТРИЦ ===")
    print("=" * 40)
    print("1. Ввод исходных данных")
    print("2. Выполнение алгоритма")
    print("3. Вывод результата")
    print("4. Завершение работы")
    print("=" * 40)


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
        input_data()
    elif choice == "2":
        execute_algorithm()
    elif choice == "3":
        output_result()
    elif choice == "4":
        print("Завершение работы...")
        exit()


def input_data():
    """Ввод исходных данных"""
    global matrix, result_matrix

    print("\n" + "=" * 30)
    print("=== ВВОД ИСХОДНЫХ ДАННЫХ ===")
    print("=" * 30)
    print("1. Ввод вручную")
    print("2. Случайная генерация")
    print("3. Назад")

    while True:
        sub_choice = input("Выберите способ ввода: ")
        if sub_choice in ["1", "2", "3"]:
            break
        print("Неверный выбор!")

    if sub_choice == "1":
        manual_input()
    elif sub_choice == "2":
        random_generation()
    elif sub_choice == "3":
        return

    # Сброс результатов при вводе новых данных
    result_matrix = None
    print("✓ Данные успешно введены!")


def manual_input():
    """Ручной ввод матрицы"""
    global matrix

    try:
        print("\n--- Ручной ввод матрицы ---")
        n = int(input("Введите количество строк (N): "))
        m = int(input("Введите количество столбцов (M): "))

        if n <= 0 or m <= 0:
            print("Ошибка: размеры должны быть положительными числами!")
            return

        matrix = []
        print(f"Введите матрицу {n}x{m} построчно:")

        for i in range(n):
            while True:
                row_input = input(f"Строка {i + 1}: ")
                try:
                    row = list(map(int, row_input.split()))
                    if len(row) != m:
                        print(f"Ошибка: в строке должно быть {m} элементов!")
                        continue
                    matrix.append(row)
                    break
                except ValueError:
                    print("Ошибка: вводите только целые числа!")

        print("\nВведенная матрица:")
        print_matrix(matrix)

    except ValueError:
        print("Ошибка ввода!")


def random_generation():
    """Случайная генерация матрицы"""
    global matrix
    import random

    try:
        print("\n--- Случайная генерация матрицы ---")
        n = int(input("Введите количество строк (N): "))
        m = int(input("Введите количество столбцов (M): "))
        min_val = int(input("Минимальное значение: "))
        max_val = int(input("Максимальное значение: "))

        if n <= 0 or m <= 0:
            print("Ошибка: размеры должны быть положительными числами!")
            return

        matrix = []
        for i in range(n):
            row = [random.randint(min_val, max_val) for _ in range(m)]
            matrix.append(row)

        print("\nСгенерированная матрица:")
        print_matrix(matrix)

    except ValueError:
        print("Ошибка ввода!")


def execute_algorithm():
    """Выполнение алгоритма по заданию - ЗАГЛУШКА"""
    global matrix, result_matrix

    if matrix is None:
        print("Ошибка: сначала введите данные!")
        return

    print("\n" + "=" * 30)
    print("=== ВЫПОЛНЕНИЕ АЛГОРИТМА ===")
    print("=" * 30)

    # ЗАГЛУШКА - здесь должен быть реальный алгоритм
    print("Алгоритм выполняется...")

    # Вместо реального алгоритма создаем заглушку
    result_matrix = "результат выполнения алгоритма"

    print("✓ Алгоритм выполнен успешно!")
    print("(реализация алгоритма оставлена в виде заглушки)")


def output_result():
    """Вывод результата"""
    global result_matrix

    if result_matrix is None:
        print("Ошибка: сначала выполните алгоритм!")
        return

    print("\n" + "=" * 30)
    print("=== ВЫВОД РЕЗУЛЬТАТА ===")
    print("=" * 30)

    print("Результат работы алгоритма:")
    print(result_matrix)

    print("\n(вывод реального результата оставлен в виде заглушки)")


def print_matrix(mat):
    """Печать матрицы"""
    if mat is None:
        print("Матрица не определена")
        return

    for row in mat:
        print(" ".join(f"{elem:4}" for elem in row))


if __name__ == "__main__":
    main()