class Robot:
    
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def intro(self):
        return "my name is: {}, i am {} years old,my color is {}".format(self.name,age,self.color)


r = Robot("sucka",23,"red")
rr = Robot("ffggka",24,"blue")
r.intro()
rr.intro()
