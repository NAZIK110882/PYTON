employees = {}   # словник співробітників: {id: emp_dict} — ID стабільні і не зсуваються після видалення
_next_id = 0     # лічильник для видачі нових ID

VALID_STATUSES = ("працює", "у відпустці", "звільнений")


def create_employee(name, ratings, position, department, salary, status="працює"):
    return {
        "name": name,
        "ratings": ratings,       # список оцінок ефективності
        "info": (position, department),  # кортеж (посада, відділ)
        "salary": salary,         # числове поле
        "status": status,         # текстове поле
    }


def input_status():
    while True:
        status = input(
            "Введіть статус (працює / у відпустці / звільнений) "
            "[за замовчуванням 'працює']: "
        ).strip()
        if not status:
            return "працює"
        if status in VALID_STATUSES:
            return status
        print(f"Невірний статус. Дозволені варіанти: {', '.join(VALID_STATUSES)}")


def input_salary():
    while True:
        try:
            salary = float(input("Введіть зарплату: "))
        except ValueError:
            print("Зарплата має бути числом. Спробуйте ще раз.")
            continue
        if salary < 0:
            print("Зарплата не може бути від'ємною. Спробуйте ще раз.")
            continue
        return salary


def input_ratings():
    while True:
        raw = input("Введіть оцінки ефективності через пробіл: ").split()
        try:
            ratings = list(map(float, raw))
        except ValueError:
            print("Оцінки мають бути числами. Спробуйте ще раз.")
            continue
        if any(r < 0 for r in ratings):
            print("Оцінки не можуть бути від'ємними. Спробуйте ще раз.")
            continue
        return ratings


def input_employee_data(existing_name=None):
    default_hint = f" [Enter — залишити '{existing_name}']" if existing_name else ""
    name_input = input(f"Введіть ПІБ співробітника{default_hint}: ").strip()
    name = name_input if name_input else (existing_name if existing_name else "")
    while not name:
        name = input("ПІБ не може бути порожнім. Введіть ПІБ співробітника: ").strip()

    ratings = input_ratings()
    position = input("Введіть посаду: ")
    department = input("Введіть відділ: ")
    salary = input_salary()
    status = input_status()

    return name, ratings, position, department, salary, status


def print_employee(eid, emp):
    print(f"ID: {eid}")
    print(f"ПІБ: {emp['name']}")
    print(f"Оцінки ефективності: {emp['ratings']}")
    print(f"Посада: {emp['info'][0]} | Відділ: {emp['info'][1]}")
    print(f"Зарплата: {emp['salary']:.2f} грн | Статус: {emp['status']}")
    print("-" * 40)


def add_employee():
    global _next_id
    name, ratings, position, department, salary, status = input_employee_data()
    emp = create_employee(name, ratings, position, department, salary, status)
    eid = _next_id
    employees[eid] = emp
    _next_id += 1
    print(f"Співробітника {name} додано з ID: {eid}\n")


def get_employee(eid):
    return employees.get(eid)


def find_employees(name_query):
    name_query = name_query.lower()
    return [
        (eid, e)
        for eid, e in employees.items()
        if name_query in e["name"].lower()
    ]


def show_employees():
    if not employees:
        print("Список співробітників порожній.\n")
        return
    for eid in sorted(employees):
        print_employee(eid, employees[eid])
    print()


def edit_employee():
    try:
        eid = int(input("Введіть ID співробітника для редагування: "))
    except ValueError:
        print("ID має бути цілим числом.\n")
        return

    emp = get_employee(eid)
    if emp:
        print(f"Редагування даних співробітника: {emp['name']}")
        name, ratings, position, department, salary, status = input_employee_data(
            existing_name=emp["name"]
        )
        employees[eid] = create_employee(
            name, ratings, position, department, salary, status
        )
        print("Дані успішно оновлено!\n")
    else:
        print("Співробітника з таким ID не знайдено.\n")


def delete_employee():
    try:
        eid = int(input("Введіть ID співробітника для видалення: "))
    except ValueError:
        print("ID має бути цілим числом.\n")
        return

    if eid in employees:
        deleted = employees.pop(eid)
        print(f"Співробітника {deleted['name']} видалено.\n")
    else:
        print("Співробітника з таким ID не знайдено.\n")


def search_by_id():
    try:
        eid = int(input("Введіть ID співробітника: "))
    except ValueError:
        print("ID має бути цілим числом.\n")
        return

    emp = get_employee(eid)
    if emp:
        print_employee(eid, emp)
    else:
        print("Співробітника з таким ID не знайдено.\n")


def search_by_name():
    query = input("Введіть ім'я для пошуку: ")
    results = find_employees(query)
    if results:
        for eid, emp in results:
            print_employee(eid, emp)
    else:
        print("Співробітників не знайдено.\n")


def statistics():
    if not employees:
        print("Список співробітників порожній.\n")
        return

    salaries = [e["salary"] for e in employees.values()]
    avg_salary = sum(salaries) / len(salaries)

    all_ratings = [r for e in employees.values() for r in e["ratings"]]

    print("=== Статистика компанії ===")
    print(f"Загальна кількість співробітників: {len(employees)}")
    print(f"Середня зарплата: {avg_salary:.2f} грн")
    print(f"Максимальна зарплата: {max(salaries):.2f} грн")
    print(f"Мінімальна зарплата: {min(salaries):.2f} грн")

    if all_ratings:
        print(f"Середня оцінка ефективності: {sum(all_ratings)/len(all_ratings):.2f}")
        print(f"Найвища оцінка ефективності: {max(all_ratings)}")
    else:
        print("Оцінки ефективності відсутні.")
    print()


def menu():
    options = {
        "1": add_employee,
        "2": show_employees,
        "3": search_by_id,
        "4": search_by_name,
        "5": edit_employee,
        "6": delete_employee,
        "7": statistics,
    }

    while True:
        print("==== Управління Співробітниками ====")
        print("1. Додати співробітника")
        print("2. Показати всіх співробітників")
        print("3. Пошук за ID")
        print("4. Пошук за ім'ям")
        print("5. Редагувати співробітника")
        print("6. Видалити співробітника")
        print("7. Статистика компанії")
        print("8. Вихід")

        choice = input("Ваш вибір: ")

        if choice in options:
            options[choice]()
            input("Натисніть Enter, щоб продовжити...")
            print()
        elif choice == "8":
            print("Завершення роботи програми...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.\n")


if __name__ == "__main__":
    menu()