class Fighter():
    health = 100
    damage = 10

    def __init__(self,name):
        self.name = name
        
    def attack(self,other_guy):
        other_guy.health = other_guy.health - self.damage
        print("{} was attacked by {}".format(other_guy.name,self.name))
        print("{} wins over {}".format(self.name,other_guy.name))
        
    def __str__(self):
        return "{}: health={} ".format(self.name,self.health)
    

moses = input("Enter Fighter 1 name: \n")
opp = input("Enter Opponent name: \n")     
moses = Fighter(moses)
oop = Fighter(opp)
moses.attack(opp)
print(moses)
print(opp)

        
