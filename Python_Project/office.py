#Nader John 

class Office:
    employeesNum = 0  

    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees if employees else []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1
        print(f"{employee.name} hired successfully :D")

    def fire(self, empId):
        emp = self.get_employee(empId)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1
            print(f"Employee {emp.name} (ID: {empId}) fired.")
        else:
            print(f"No employee found with ID {empId}")

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction
            print(f"Deducted {deduction} L.E from {emp.name}'s salary.")
        else:
            print(f"No employee found with ID {empId}")

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward
            print(f"Rewarded {reward} L.E to {emp.name}'s salary.")
        else:
            print(f"No employee found with ID {empId}")

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if not emp:
            print(f"No employee found with ID {empId}")
            return

        if emp.car.velocity == 0:
            arrival_time = float()
        else:
            arrival_time = moveHour + (emp.distanceToWork / emp.car.velocity)

        if arrival_time > 9.0: 
            deduction = emp.salary * 0.1  # Deduct 10%
            self.deduct(empId, deduction)
            print(f"{emp.name} was late! Arrival time: {arrival_time:.2f}")
        else:
            reward = emp.salary * 0.1  # Reward 10%
            self.reward(empId, reward)
            print(f"{emp.name} arrived on time at {arrival_time:.2f}")

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num
        print(f"Total employees updated to: {cls.employeesNum}")