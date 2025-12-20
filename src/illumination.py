import numpy as np
import math


def get_illumination(power, px_mm, py_mm, sx_mm, sy_mm, sz_mm):
    """Формула подсчета освещенности в точке на плоскости z = 0 от точечного источника света"""
    # Переводим миллиметры в метры (делим на 1000)
    px_m = px_mm / 1000.0
    py_m = py_mm / 1000.0
    sx_m = sx_mm / 1000.0
    sy_m = sy_mm / 1000.0
    sz_m = sz_mm / 1000.0

    # Разницы координат в метрах
    diff_x = px_m - sx_m
    diff_y = py_m - sy_m
    diff_z = 0 - sz_m  # плоскость z = 0

    # Квадрат расстояния в метрах
    distance_squared = diff_x ** 2 + diff_y ** 2 + diff_z ** 2

    if distance_squared == 0:
        return 0  # Чтобы избежать деления на 0

    # Расстояние
    distance = math.sqrt(distance_squared)

    # Косинус угла между нормалью к плоскости (0,0,1) и направлением на источник
    # cos(θ) = |sz_m| / distance (нормаль направлена вверх, источник выше плоскости)
    cos_theta = abs(sz_m) / distance

    # Освещенность E = I * cos(θ) / r²
    illumination = power * cos_theta / distance_squared

    return illumination


def grid_centers(width_mm, height_mm, w_res, h_res):
    """Возвращает два массива координат центров пикселей по соответствующим осям"""
    step_x = width_mm / w_res
    step_y = height_mm / h_res

    x_centers = (-width_mm / 2.0) + (np.arange(w_res) + 0.5) * step_x
    y_centers = (-height_mm / 2.0) + (np.arange(h_res) + 0.5) * step_y
    return x_centers, y_centers