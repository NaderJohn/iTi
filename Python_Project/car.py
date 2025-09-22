#Nader John 

class Car:
    def __init__(self, name, fuelRate, velocity=0):
        self.name = name
        self.fuelRate = min(max(fuelRate, 0), 100)  
        self.velocity = min(max(velocity, 0), 200)  

    def run(self, velocity, distance):
        
        self.velocity = min(max(velocity, 0), 200)
        
        needed_fuel = distance * 0.1

        if self.fuelRate <= 0:
            self.stop(distance)
            return

        if self.fuelRate < needed_fuel:
            max_distance = self.fuelRate / 0.1
            self.fuelRate = 0
            self.stop(distance - max_distance)
        else:
            self.fuelRate -= needed_fuel
            self.stop(0)

    def stop(self, left_distance):
        self.velocity = 0
        if left_distance <= 0:
            print("You have arrived at your destination.")
        else:
            print(f"Car stopped! {left_distance:.1f} km left to destination.")