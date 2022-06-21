from solar_objects import *

G = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """
    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body is obj:
            continue
        if type(body) is Planet and type(obj) is not Star:
            continue
        if type(body) is Planet2 and type(obj) is not Star2:
            continue
        if type(body) is Star or type(body) is Star2:
            continue

        r = ((obj.x - body.x) ** 2 + (obj.y - body.y) ** 2) ** 0.5
        F = G * body.m * obj.m / r ** 2
        body.Fx += F * (obj.x - body.x) / r
        body.Fy += F * (obj.y - body.y) / r


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    ax = body.Fx / body.m
    ay = body.Fy / body.m
    body.Vx += ax*dt
    body.Vy += ay * dt
    body.x += body.Vx * dt
    body.y += body.Vy * dt

def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)









