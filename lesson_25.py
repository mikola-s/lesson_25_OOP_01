""" Написать класс для перевода температур из разных систем исчесления"""


class TemperatureScale:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.name_ru = kwargs['name_ru']
        self.abs_zero = kwargs['absolute_zero']
        self.freeze_point = kwargs['freezing_point']
        self.boil_point = kwargs['boiling_point']
        self.d_h20_aggregate = kwargs['boiling_point'] - kwargs['freezing_point']
        self.units = kwargs['units']
        self.val = None


class Temperature:
    def get_user_choice(self, args: list) -> list:
        """ запрашивает у пользователя данные в stdin """

        print(' Пользователь! \nвведи единицы температуры которую хочешь преобразовать\n'
              '(например: 1)\n'
              f'1. {args[0].name_ru}\n'
              f'2. {args[1].name_ru}\n'
              f'3. {args[2].name_ru}\n'
              )
        item = int(input()) - 1
        selected_scale = args[item]
        del args[item]

        print('теперь введи значение температуры (например: 100)\n')
        selected_scale.val = float(input())

        print('введи номер шкалы температуры в которую хочешь конвертировать\n'
              '(например: 1)\n'
              f'1. {args[0].name_ru} \n'
              f'2. {args[1].name_ru} \n')
        change_to_scale = args[int(input()) - 1]

        return [selected_scale, change_to_scale]

    def convert_temperature(self, ch_from: object, ch_to: object) -> object:
        """ вычисляет значение температуры в заданной шкале
        ch_to.val -- вычисляемая температура
        ch_to.abs_zero -- значение абсолютного нуля для вычисляемой температуры
        ch_from.val -- исходное значение температуры
        ch_from.abs_zero -- значение абсолютного нуля для исходной температуры
        unit_different -- отношение между единицами измерений шкал
        d_h20_aggregate -- значение для шаклы от точки замерзания до точки кипения воды
        """

        unit_different = ch_to.d_h20_aggregate / ch_from.d_h20_aggregate
        ch_to.val = (ch_from.val - ch_from.abs_zero) * unit_different + ch_to.abs_zero

        return ch_to

    def print_result(self, result):
        """выводит результаты вычислений в stdout"""
        print('Пользователь! результат моих вычислений:\n'
              f'{round(result.val, 2)} {result.units}')


kelvin = TemperatureScale(
    name='Kelvin',
    name_ru='Кельвин',
    absolute_zero=0,
    freezing_point=273.2,  # K
    boiling_point=373.2,
    units='K',
)

celsius = TemperatureScale(
    name='Celsius',
    name_ru='Цельсий',
    absolute_zero=-273.2,
    freezing_point=0,  # °C
    boiling_point=100,
    units='°C',
)

fahrenheit = TemperatureScale(
    name='Fahrenheit',
    name_ru='Фаренгейт',
    absolute_zero=-459.67,
    freezing_point=32,  # °F
    boiling_point=212,
    units='°F',
)

temperature_scales = [kelvin, celsius, fahrenheit]  # сисок с температурными шкалами

temp_change = Temperature()

user_choice = temp_change.get_user_choice(temperature_scales)  # данные от пользователя

convert_result = temp_change.convert_temperature(*user_choice)  # вычисления температуры

temp_change.print_result(convert_result)  # вывод результата в std_out
