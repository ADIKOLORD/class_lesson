class Samsung:
aafffaaaafdaffafddfddfffsdfdddsfdfaa
    def __init__(self, color: str, memory: int, battery: int):
        '''
        Обязательные аргументы при создании Экземпляра
        '''
        self.color = color
        self.memory = memory
        self.battery = battery

    def info_mobile(self):
        info = f'Телефон: Samsung\nColor: {self.color}\nMemory: {self.memory}\nBattery: {self.battery}'
        print(info)

    def add_battery(self, how_much: int):
        '''
        Функция для увеличение батареи
        '''
        self.battery = self.battery + how_much

    def change_color(self, new_color):
        '''
        Функция для изменение цвета на новый!
        '''
        self.color = new_color

    @staticmethod
    def root_document():
        '''
        Бул метод: башка методдор или аттрибуттар менен такыр байланышы жок

        Мисалы башында self.color, self.memory, self.battery деп создать эттик.

        Аны add_battery деген методдун ичинде колдондук

        А бирок info_root_class деген методдун ичинде колдоно албайбыз

        Бир соз менен айтканда качан, Класстын (Samsung) аттрибут и функцияларына
        байланышпаган метод тузгубуз келгенде колдонобуз!
        '''

        doc = 'Компания: Samsung\nДиректор: ADIKO\nБюджет: 750000$'
        print(doc)


s1 = Samsung('Blue', 128, 75)
s1.info_mobile()

s1.add_battery(13)
s1.info_mobile()


class SamsungMax(Samsung):

    def __init__(self, color, memory, battery):
        super().__init__(color, memory, battery)

    def finger_print(self):
        print('Типа отпечатка пальца')


sm1 = SamsungMax('Black', 128, 75)
sm1.info_mobile()
