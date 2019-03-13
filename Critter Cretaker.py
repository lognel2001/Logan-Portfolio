# Critter Care taker
# Logan Nelson

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass__time(self,amount):
        self.hunger += 1 +(amount//4)
        self.boredom += 1 +(amount//4)
        print(self.hunger)
        print(self.boredom)

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "joyess day"
        elif 5 <= unhappiness <= 10:
            m = "ehh"
        elif 11 <= unhappiness <= 15:
            m = "smad"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass__time(0)
    
    def eat(self, food = 4):
        print("Burp! Excuse me! Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass__time(food)

    def play(self, fun = 4):
        print("YeeHaw!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass__time(fun)


def main():
    crit_name = input("What will your critters name be?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker
    
        1 - Leave your Critter forever :(
        2 - Listen to your critters stories
        3 - Feed your critter food
        4 - Play catch with your critter
        """)
    
        choice = input("Choice: ")
        print()

        
        if choice == "1":
            print("Good-bye.")

        
        elif choice == "2":
            crit.talk()
        
        
        elif choice == "3":
            food = int(input("How much do you want to feed your critter?"))
            crit.eat(food)
         
        
        elif choice == "4":
            fun = int(input("How much do you want to play with your critter?"))
            crit.play(fun)

main()
