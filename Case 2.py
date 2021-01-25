class Road:
    th: float = 5

    def __init__(self, length: [int, float], width: [int, float]):
        self._length = float(length)
        self._width = float(width)

    def mass(self, thickness: float) -> [float, None]:
        try:
            return (self._length * self._width
                    * thickness * self.th / 1000)
        except TypeError:
            return None


if __name__ == '__main__':
    try:
        road = Road(5000, 20)
        print(
            'Масса дорожного покрытия составит:',
            road.mass(25),
            'тонн'
        )
    except TypeError:
        print('Класс Road требует 2 позиционных аргумента')
