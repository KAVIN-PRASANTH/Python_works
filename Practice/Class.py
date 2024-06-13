class Animal():
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        self.helo()
    def helo(self):
        print("kavin",self.name)
       
dog=Animal(gender="male",name="cat")


