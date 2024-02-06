class LogicGame:
    def __init__(self):
        # число которое получилось при прокрутке барабана
        self.random_number = None
        # общее кол-во очков
        self.points = 0
        self.new_count = 0
        self.stat = 0
        self.chanse = 0

    def set_stat(self,stat):
        self.stat +=stat


    def action(self,random_number):
        if random_number == '1':
            new_text = 'Вы заработали 100 очков'
            self.points += 100
            return new_text


        elif random_number == '2':
            new_text = 'Вы заработали 200 очков'
            self.points += 200
            return new_text

        elif random_number == '3':
            new_text = 'Вы заработали 300 очков'
            self.points += 300
            return new_text
        elif random_number == '4':
            new_text = 'Вы заработали 400 очков'
            self.points += 400
            return new_text
        elif random_number == '5':
            new_text = 'Вы заработали 500 очков'
            self.points += 500
            return new_text
        elif random_number == '6':
            new_text = 'Вы заработали 1000 очков'
            self.points += 1000
            return new_text
        elif random_number == '7':
            new_text = 'Вы заработали 1500 очков'
            self.points += 1500
            return new_text
        elif random_number == '8':
            new_text = 'Вы заработали 2000 очков'
            self.points += 2000
            return new_text
        elif random_number == '9':
            self.chanse += 1
            return 'Сектор приз на барабане!'



        #elif random_number == '10':
            #return 'Сектор приз на барабане!'

        return "Выбрана неверная команда"


    def get_points(self):
        return self.points

    def set_points(self,points):
        self.points = points

    def get_stat(self):
        return self.stat

    def get_chanse(self):
        return self.chanse

    def set_chanse(self,chanse):
        self.chanse = chanse