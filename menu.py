"""
Модуль меню - пример нисходящего проектирования
Итерация 4: Полная реализация с алгоритмом обработки матриц
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
    print("\n" + "="*40)
    print("=== СИСТЕМА ОБРАБОТКИ МАТРИЦ ===")
    print("="*40)
    print("1. Ввод исходных данных")
    print("2. Выполнение алгоритма")
    print("3. Вывод результата")
    print("0. Завершение работы")
    print("="*40)

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
    valid_choices = ["0", "1", "2", "3"]
    return choice in valid_choices

def process_choice(choice):
    """Обработать выбор пользователя"""
    if choice == "1":
        input_data()
    elif choice == "2":
        execute_algorithm()
    elif choice == "3":
        output_result()
    elif choice == "0":
        print("Завершение работы...")
        exit()

def input_data():
    """Ввод исходных данных"""
    global matrix, result_matrix

    print("\n" + "="*30)
    print("=== ВВОД ИСХОДНЫХ ДАННЫХ ===")
    print("="*30)
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
        print(f"Введите матрицу {n}x{m} построчно (числа через пробел):")

        for i in range(n):
            while True:
                row_input = input(f"Строка {i+1}: ")
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
    """Выполнение алгоритма по заданию"""
    global matrix, result_matrix

    if matrix is None:
        print("Ошибка: сначала введите данные!")
        return

    print("\n" + "="*30)
    print("=== ВЫПОЛНЕНИЕ АЛГОРИТМА ===")
    print("="*30)

    print("Исходная матрица:")
    print_matrix(matrix)

    # РЕАЛИЗАЦИЯ АЛГОРИТМА
    print("\nВыполнение алгоритма:")
    print("1. Добавление среднеарифметического значения к каждой строке")
    print("2. Сортировка строк по убыванию средних значений")

    # Создаем копию матрицы с добавленными средними значениями
    matrix_with_means = []
    for row in matrix:
        row_mean = sum(row) / len(row)
        new_row = row + [row_mean]  # Добавляем среднее значение в конец строки
        matrix_with_means.append(new_row)

    # Сортируем строки по убыванию средних значений (последний элемент)
    sorted_matrix = sorted(matrix_with_means, key=lambda x: x[-1], reverse=True)

    result_matrix = sorted_matrix

    print("✓ Алгоритм выполнен успешно!")

def output_result():
    """Вывод результата"""
    global result_matrix

    if result_matrix is None:
        print("Ошибка: сначала выполните алгоритм!")
        return

    print("\n" + "="*30)
    print("=== ВЫВОД РЕЗУЛЬТАТА ===")
    print("="*30)

    print("Результат работы алгоритма:")
    print("Матрица с добавленными средними значениями, отсортированная по убыванию:")
    print_matrix_with_means(result_matrix)

def print_matrix(mat):
    """Печать обычной матрицы"""
    if mat is None:
        print("Матрица не определена")
        return

    for row in mat:
        print(" ".join(f"{elem:8}" for elem in row))

def print_matrix_with_means(mat):
    """Печать матрицы со средними значениями"""
    if mat is None:
        print("Матрица не определена")
        return

    for i, row in enumerate(mat):
        # Выводим все элементы кроме последнего
        elements = " ".join(f"{elem:8}" for elem in row[:-1])
        # Последний элемент (среднее) выводим с округлением
        mean_value = f"{row[-1]:8.2f}"
        print(f"Строка {i+1}: {elements} | Среднее: {mean_value}")

if __name__ == "__main__":
    main()