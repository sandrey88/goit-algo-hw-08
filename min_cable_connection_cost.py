import heapq


def min_cable_connection_cost(cable_lengths):
    """
    Ця функція знаходить порядок об'єднання мережевих кабелів,
    щоб мінімізувати загальні витрати на їх з'єднання.

    """
    if len(cable_lengths) <= 1:
        return 0  # Немає кабелів для об'єднання, витрати 0.

    # Створення купи з кабелів
    heapq.heapify(cable_lengths)

    # Відображення початкової купи
    sorted_heap = heapq.nsmallest(len(cable_lengths), cable_lengths)
    print()
    print(f"Відсортовані кабелі за довжиною (початкова купа):\n{sorted_heap}")
    print()

    total_cost = 0
    step_num = 1
    while len(cable_lengths) > 1:
        # Витягування двох найкоротших кабелі з купи
        cable1 = heapq.heappop(cable_lengths)
        cable2 = heapq.heappop(cable_lengths)

        # Обчислення витрати на з'єднання цих двох кабелів
        connection_cost = cable1 + cable2

        # Додавання витрат до загальної суми
        total_cost += connection_cost

        # Додавання нового кабелю назад до купи
        heapq.heappush(cable_lengths, connection_cost)

        # Вивід інформації про поточний крок
        print(f"Крок {step_num}: з'єднуємо кабелі довжиною {cable1} і {cable2}, витрати: {connection_cost}")
        print(f"Поточний стан купи: {cable_lengths}\n")

        step_num += 1

    return total_cost

# Набір кабелів різної довжини (приклад)
cable_lengths = [5, 3, 7, 2, 6, 10]

# Приклад використання ф-ї для знаходження мінімальних витрат
min_cost = min_cable_connection_cost(cable_lengths.copy())
print(f"Мінімальні витрати на з'єднання кабелів (сума всіх витрат): {min_cost}")
print()