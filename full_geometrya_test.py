# test_shapes_polymorphic.py

import unittest
import math
from full_geometrya import (
    circle_area,
    triangle_area,
    is_right_triangle,
    calculate_area,
    AREA_FUNCTIONS
)


class TestShapeFunctions(unittest.TestCase):

    def test_circle_area(self):
        # Тест площади круга
        self.assertAlmostEqual(circle_area(1), 3.141592653589793, places=5)
        self.assertAlmostEqual(circle_area(5), 78.53981633974483, places=5)
        self.assertEqual(circle_area(0), 0)

    def test_circle_negative_radius(self):
        # Отрицательный радиус должен вызывать ValueError
        with self.assertRaises(ValueError):
            circle_area(-1)

    def test_triangle_area(self):
        # Тест площади треугольника (3-4-5)
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6.0, places=5)
        self.assertAlmostEqual(triangle_area(5, 5, 5), 10.825317547305483, places=5)

    def test_triangle_invalid_sides(self):
        # Невалидные стороны должны вызывать ошибки
        with self.assertRaises(ValueError):
            triangle_area(1, 1, 3)  # не проходит неравенство треугольника
        with self.assertRaises(ValueError):
            triangle_area(0, 1, 1)
        with self.assertRaises(ValueError):
            triangle_area(-1, 2, 2)

    def test_right_triangle(self):
        # Проверка распознавания прямоугольных треугольников
        self.assertTrue(is_right_triangle(3, 4, 5))
        self.assertTrue(is_right_triangle(5, 12, 13))
        self.assertFalse(is_right_triangle(2, 3, 4))


class TestPolymorphicArea(unittest.TestCase):

    def test_calculate_area_circle(self):
        # Тест: calculate_area для круга
        area = calculate_area('circle', 1)
        self.assertAlmostEqual(area, math.pi, places=5)

        area = calculate_area('circle', 2)
        self.assertAlmostEqual(area, 4 * math.pi, places=5)

    def test_calculate_area_triangle(self):
        # Тест: calculate_area для треугольника
        area = calculate_area('triangle', 3, 4, 5)
        self.assertAlmostEqual(area, 6.0, places=5)

    def test_calculate_area_unknown_shape(self):
        # Неизвестный тип фигуры вызывает ValueError
        with self.assertRaises(ValueError) as cm:
            calculate_area('hexagon', 1)
        self.assertIn("hexagon", str(cm.exception))
        self.assertIn("circle, triangle", str(cm.exception))  # проверяем список доступных

    def test_calculate_area_wrong_args_count(self):
        # Неверное количество аргументов вызывает TypeError
        with self.assertRaises(TypeError):
            calculate_area('circle')  # нет радиуса

        with self.assertRaises(TypeError):
            calculate_area('circle', 1, 2)  # слишком много

        with self.assertRaises(TypeError):
            calculate_area('triangle', 3, 4)  # не хватает одной стороны

        with self.assertRaises(TypeError):
            calculate_area('triangle', 3, 4, 5, 6)  # слишком много

    def test_calculate_area_propagates_errors(self):
        # Ошибки изнутри функций должны передаваться дальше
        with self.assertRaises(ValueError):
            calculate_area('circle', -5)  # отрицательный радиус

        with self.assertRaises(ValueError):
            calculate_area('triangle', 1, 1, 3)  # недопустимый треугольник


class TestAreaFunctionsRegistry(unittest.TestCase):
    def test_supported_shapes(self):
        # Поддерживаются только ожидаемые фигуры
        self.assertIn('circle', AREA_FUNCTIONS)
        self.assertIn('triangle', AREA_FUNCTIONS)
        self.assertNotIn('rectangle', AREA_FUNCTIONS) #если добавлять фигуру (сейчас закоментировано)