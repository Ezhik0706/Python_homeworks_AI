"""
Запросите у пользователя значения выручки
и издержек фирмы. Определите, с каким финансовым
результатом работает фирма (прибыль — выручка
больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма
отработала с прибылью, вычислите рентабельность
выручки (соотношение прибыли к выручке). Далее
запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.
"""
revenue = int(input("Введите сумму выручки компании:" + " "))
costs = int(input("Введите сумму издержек компании:" + " "))
if revenue > costs:
    print("Финансовый результат Вашей компании положительный - Прибыль")
    profitability = (revenue - costs)/revenue #рентабельность продаж
    print(f"Рентабельность Вашей компании равна {profitability:.2f}")
    quantity_staff = int(input("Введите количество сотрудников Вашей компании:" + " "))
    profit_staff = (revenue - costs) / quantity_staff
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет {profit_staff:.2f}")
elif revenue < costs:
    print("Финансовый результат Вашей компании отрицательный - Убыток")
else:
    print("Финансовый результат Вашей компании - достигнута точка безубыточности")