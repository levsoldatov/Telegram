# костюм,шапка,телефон,шуба,машина
import random
import Fortune



class KolesoFortuni:

    def __init__(self):
        self.random_predmet = random.choices(Fortune.present, weights=[40, 30, 20, 7, 3], k=1)[0]
        self.chanse = 0

    def get_random_predmet(self):
        return self.random_predmet


    def get_stat(self):
        self.stat = self.random_predmet['stat']
        return self.stat


    def popitka(self,chanse):
        if 0 < chanse:
            self.chanse = chanse - 1
            massage = ['Колесо фортуны запущено!',self.random_predmet]

        else:
            massage = ['У вас не хватает попыток',]

        return massage


    def get_chanse(self):
        return self.chanse