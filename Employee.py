#CANTILLAS MARK G.
#https://www.w3schools.com/
#https://www.javatpoint.com/
#https://www.python.org/
class Employee:
    def __init__(self, name, title, salary):
        # Initialize Employee object with name, title, and salary attributes
        self.name = name
        self.title = title
        self.salary = salary

    def display_info(self):
        # Display employee information
        print("\n Employee Information:")
        print(f" Name: {self.name}")
        print(f" Title: {self.title}")
        print(f" Salary: ${self.salary}")

    def give_raise(self, amount):
        # Give a raise to the employee
        self.salary += amount
        print(f"{self.name} received a raise of ${amount}")


class Developer (Employee):
    def __init__(self, name, title, salary, languages):
        # Initialize Developer object with additional Languages attribute
        super().__init__(name, title, salary)
        self.languages = languages

    def display_info(self):
        # Override display_info method to include programming Languages
        super().display_info()
        print("\n Programming Languages:")
        for language in self.languages:
            print(f" - {language}")


class Manager(Employee):
    def __init__(self, name, title, salary, employees=None):
        # Initialize Manager object with an optional List of employees
        super().__init__(name, title, salary)
        self.employees = employees if employees else []

    def add_employee(self, employee):
        # Add an employee to the manager's List of direct reports
        self.employees.append(employee)

    def display_info(self):
        # Override display_info method to include direct reports' information
        super().display_info()
        if self.employees:
            print("\n Employees Reporting:")
            for employee in self.employees:
                print(f" - {employee.name}")
        else:
            print("\n No employees reporting to this manager.")


# Instantiate objects
employee = Employee("Alice Cayetano", "HR Assistant", 50000)
developer = Developer("Colong Aladin John", "Software Developer", 80000, ["Python", "Java"])
manager = Manager("Jane Claude catulmmo", "Software Manager", 100000, [developer])

# Display information
employee.display_info()
developer.display_info()
manager.display_info()
