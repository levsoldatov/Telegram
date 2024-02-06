import Tovars

class Magazin:

    # Хранение свойств магазина
    def __init__(self):
        self.dict_tovars = Tovars.dict_tovars
        self.tovar = ""
        self.mycount = 0
        self.stat = 0

    # Кол-во товаров
    def count_tovars(self):
        count = 0
        for k in self.dict_tovars:
            count +=1
        #print(count)
        return count

# Покупка товара
    def buy_tovar(self,mycount,name):
        for k in self.dict_tovars:
            if self.dict_tovars[k]['name'] == name:
                if self.dict_tovars[k]['price'] <= mycount:
                    self.tovar = 'Вы можете купить '+ self.dict_tovars[k]['name']
                    self.mycount = mycount - self.dict_tovars[k]['price']
                    self.stat = self.dict_tovars[k]['stat']
                    break
                else:
                    self.tovar = 'Не хватает очков для покупки ' + self.dict_tovars[k]['name']
                    break

            else:
                self.tovar = 'товара нет'
        #print(self.tovar,self.mycount)
        return self.tovar

    def get_newmycount(self):
        return self.mycount

    def get_new_stat(self):
        return self.stat

    def set_new_stat(self):
        self.stat = 0

