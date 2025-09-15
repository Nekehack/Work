import math

def circle_area(radius):
    """Площадь круга по радиусу."""
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным.")
    return math.pi * radius ** 2


def triangle_area(a, b, c):
    """Площадь треугольника по трём сторонам (формула Герона)."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны должны быть положительными.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует.")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def is_right_triangle(a, b, c):
    """Проверяет, является ли треугольник прямоугольным."""
    sides = sorted([a, b, c])
    return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-9


# === Полиморфический интерфейс ===

# Словарь: тип фигуры → функция вычисления площади
AREA_FUNCTIONS = {
    'circle': lambda r: circle_area(r),
    'triangle': lambda a, b, c: triangle_area(a, b, c)

    #Можно легко расширить, добавив строку и дописав функцию по вычислению площади
    # 'rectangle': lambda w, h: w * h
}


def calculate_area(shape_type, *args):
    """ Полиморфная функция: вычисляет площадь, не зная тип фигуры на этапе компиляции.

    параметр строка — тип фигуры ('circle', 'triangle')
    параметр аргументы: параметры фигуры (радиус, или три стороны и т.д.)
    возвращает площадь """
    if shape_type not in AREA_FUNCTIONS:
        available = ', '.join(AREA_FUNCTIONS.keys())
        raise ValueError(f"Неизвестный тип фигуры: {shape_type}. Доступные: {available}")

    try:
        return AREA_FUNCTIONS[shape_type](*args)
    except TypeError as e:
        raise TypeError(f"Неверное количество аргументов для '{shape_type}': {e}")
    except ValueError as e:
        raise e  # Перебрасываем дальше


def get_shape_from_user():
    # Имитация динамического выбора фигуры пользователемt
    print("Выберите фигуру: circle, triangle")
    shape_type = input(">").strip().lower()

    if shape_type == "circle":
        radius = float(input("Радиус: "))
        return "circle", (radius,)

    elif shape_type == "triangle":
        a = float(input("Сторона a: "))
        b = float(input("Сторона b: "))
        c = float(input("Сторона c: "))
        return "triangle", (a, b, c)

    else:
        raise ValueError("Неподдерживаемая фигура")


def main():
    try:
        shape_type, params = get_shape_from_user()
        area = calculate_area(shape_type, *params)
        print(f"Площадь: {area:.2f}")

        # Дополнительно: если треугольник — проверим, прямоугольный ли он
        if shape_type == "triangle" and len(params) == 3:
            a, b, c = params
            if is_right_triangle(a, b, c):
                print("Это прямоугольный треугольник!")

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()