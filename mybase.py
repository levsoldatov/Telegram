class mybase:
    def __init__(self):
        self.name_base = 'mybase.txt'

    def write_base(self,id):
        with open (self.name_base,'a',encoding='utf-8') as file:
            id = str(id)
            file.write(id+'\n')


    def read_base(self,id):
        id =str(id)
        with open(self.name_base,'r',encoding='utf-8')as file:
            base = file.read()
            if id in base:
                return id
            return 'no'