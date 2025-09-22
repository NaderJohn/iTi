#Nader John 

import re
from car import Car
from employee import Employee
from office import Office

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def create_employee():
    print("\n=== New Employee ===")
    
    # Basic info
    name = input("Name: ")
    emp_id = int(input("Employee ID: "))
    
    # Email validation
    while True:
        email = input("Email: ")
        if validate_email(email):
            break
        print("Invalid email! Please try again.")
    
    
    salary = float(input("Salary (L.E): "))
    money = float(input("Pocket money (L.E): "))
    
  
    health = int(input("Health rate (0-100): "))
    health = max(0, min(100, health))
    
   
    car_name = input("Car name: ")
    fuel_rate = int(input("Car fuel rate (0-100): "))
    car = Car(car_name, fuel_rate)
    
    
    distance = float(input("Distance to work (km): "))
    
    return Employee(
        name=name,
        money=money,
        mood="Neutral",
        healthRate=health,
        emp_id=emp_id,
        car=car,
        email=email,
        salary=salary,
        distanceToWork=distance
    )

def Daily_routine(office):
   
    print("\n Working Day ")
    
    for emp in office.get_all_employees():
        print(f"\n {emp.name}'s Day ")
        
       
        sleep = int(input(f"How many hours did {emp.name} sleep? "))
        emp.sleep(sleep)
        
        
        move_hour = float(input(f"When did {emp.name} leave home? (e.g. 7.5 for 7:30 AM): "))
        emp.drive()
        office.check_lateness(emp.id, move_hour)
        
        # Work
        work_hours = int(input(f"How many hours did {emp.name} work? "))
        emp.work(work_hours)
        
        # Meals
        meals = int(input(f"How many meals did {emp.name} eat (1-3)? "))
        emp.eat(meals)
        
        # Shopping
        items = int(input(f"How many items did {emp.name} buy? "))
        emp.buy(items)
        
      
        print(f"\n{emp.name}'s Status:")
        print(f"- Mood: {emp.mood}")
        print(f"- Health: {emp.healthRate}%")
        print(f"- Money: {emp.money} L.E")
        print(f"- Salary: {emp.salary} L.E")

def main():
    print("\n( ITI Office Management System )")
    
   
    office_name = input("\nEnter office name: ")
    office = Office(office_name)
    
   
    while True:
        print("\nMenu:")
        print("1. Hire Employee")
        print("2. Start employee daily routine")
        print("3. View Employees")
        print("4. Fire Employee")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == "1":
            emp = create_employee()
            office.hire(emp)
        elif choice == "2":
            if not office.get_all_employees():
                print("No employees to show")
            else:
                Daily_routine(office)
        elif choice == "3":
            employees = office.get_all_employees()
            if employees:
                print("\nCurrent Employees:")
                for emp in employees:
                    print(f"ID: {emp.id}, Name: {emp.name}, Salary: {emp.salary} L.E")
            else:
                print("No employees hired yet")
        elif choice == "4":
            emp_id = int(input("Enter employee ID to fire: "))
            office.fire(emp_id)
        elif choice == "5":
            print("\nFinal Office Status:")
            print(f"Office Name: {office.name}")
            print(f"Total Employees: {Office.employeesNum}")
            print("Thank you Eng.omar for your effort , Goodbye :D ")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()