from solar_objects import Star, Planet, Star2, Planet2

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, encoding='utf-8') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#' or line[0]== '-':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            elif object_type == "star2":
                star2 = Star2()
                parse_star2_parameters(line, star2)
                objects.append(star2)
            elif object_type == "planet2":
                planet2 = Planet2()
                parse_planet2_parameters(line, planet2)
                objects.append(planet2)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    if len(line.strip()) == 0 or line[0] == '#':
        return ""
    line = line.split()
    line[0] = line[0].lower()
    if line[0] == "star":
        star.R = float(line[1])
        star.color = line[2]
        star.m = float(line[3])
        star.x = float(line[4])
        star.y = float(line[5])
        star.Vx = float(line[6])
        star.Vy = float(line[7])



def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    if len(line.strip()) == 0 or line[0] == '#':
        return ""
    line = line.split()
    line[0] = line[0].lower()
    if line[0] == "planet":
        planet.R = float(line[1])
        planet.color = line[2]
        planet.m = float(line[3])
        planet.x = float(line[4])
        planet.y = float(line[5])
        planet.Vx = float(line[6])
        planet.Vy = float(line[7])

def parse_star2_parameters(line, star2):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    if len(line.strip()) == 0 or line[0] == '#':
        return ""
    line = line.split()
    line[0] = line[0].lower()
    if line[0] == "star2":
        star2.R = float(line[1])
        star2.color = line[2]
        star2.m = float(line[3])
        star2.x = float(line[4])
        star2.y = float(line[5])
        star2.Vx = float(line[6])
        star2.Vy = float(line[7])



def parse_planet2_parameters(line, planet2):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    if len(line.strip()) == 0 or line[0] == '#':
        return ""
    line = line.split()
    line[0] = line[0].lower()
    if line[0] == "planet2":
        planet2.R = float(line[1])
        planet2.color = line[2]
        planet2.m = float(line[3])
        planet2.x = float(line[4])
        planet2.y = float(line[5])
        planet2.Vx = float(line[6])
        planet2.Vy = float(line[7])



def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print("%s %d %s %f %f %f %f %f" % (obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy), file = out_file)


if __name__ == "__main__":
    print("This module is not for direct call!")

