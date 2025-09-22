#Nader John 

from person import Person
from car import Car

class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork  

    def work(self, hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours > 8:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"
        print(f"{self.name} is {self.mood.lower()} after working {hours} hours.")

    def drive(self):
        print(f"{self.name} is driving to work...")
        self.car.run(60, self.distanceToWork) 

    def refuel(self, gasAmount=100):
        self.car.fuelRate = min(self.car.fuelRate + gasAmount, 100)
        print(f"Car refueled to {self.car.fuelRate}%")

    def send_email(self, to, subject, body):
        email_content = f"""
        From: {self.email}
        To: {to}
        Subject: {subject}
        
        {body}
        """
        print("Email sent successfully")
        print(email_content)