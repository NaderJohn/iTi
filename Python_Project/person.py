#Nader John 

class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = min(max(healthRate, 0), 100)  # Ensure health between 0-100

    def sleep(self, hours):
        if hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"
        print(f"{self.name} is {self.mood.lower()} after sleeping {hours} hours.")

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        else:
            self.healthRate = 50
        print(f"{self.name}'s health is now {self.healthRate}% after {meals} meals.")

    def buy(self, items):
        cost = 10 * items
        self.money -= cost
        print(f"{self.name} spent {cost} L.E on {items} items. Remaining money: {self.money} L.E")