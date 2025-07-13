import abc 
class Employee(abc.ABC): 
    """
    Base class for all employee types.
    Handles common interface for every employee type.
    """
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    @abc.abstractmethod
    def calculate_payroll(self):
        """
        Abstract method to be implemented by derived classes.
        Returns the weekly salary for the employee.
        """
        pass

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}"


class SalaryEmployee(Employee):
    """
    Derived class for employees paid a fixed weekly salary.
    """
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name) # Initialize members of the base class
        if not isinstance(weekly_salary, (int, float)) or weekly_salary < 0:
            raise ValueError("Weekly salary must be a non-negative number.")
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        """
        Calculates and returns the weekly salary for a SalaryEmployee.
        """
        return self.weekly_salary

    def __str__(self):
        return f"{super().__str__()}, Type: Salary Employee, Weekly Salary: ${self.weekly_salary:.2f}"

# (iii) Add an HourlyEmployee to the HR system
class HourlyEmployee(Employee):
    """
    Derived class for manufacturing workers paid by the hour.
    """
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name) # Initialize members of the base class
        if not isinstance(hours_worked, (int, float)) or hours_worked < 0:
            raise ValueError("Hours worked must be a non-negative number.")
        if not isinstance(hourly_rate, (int, float)) or hourly_rate < 0:
            raise ValueError("Hourly rate must be a non-negative number.")

        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        """
        Calculates and returns the weekly salary for an HourlyEmployee.
        Returns the hours worked times the hourly rate.
        """
        return self.hours_worked * self.hourly_rate

    def __str__(self):
        return (f"{super().__str__()}, Type: Hourly Employee, Hours Worked: {self.hours_worked},"
                f" Hourly Rate: ${self.hourly_rate:.2f}, Weekly Salary: ${self.calculate_payroll():.2f}")

# (iv) Create a CommissionEmployee class
class CommissionEmployee(SalaryEmployee): # Inherits from SalaryEmployee
    """
    Derived class for sales associates paid a fixed salary plus commission.
    """
    def __init__(self, emp_id, name, weekly_salary, commission_value):
        # Initialize SalaryEmployee's members (emp_id, name, weekly_salary)
        super().__init__(emp_id, name, weekly_salary)
        if not isinstance(commission_value, (int, float)) or commission_value < 0:
            raise ValueError("Commission value must be a non-negative number.")
        self.commission_value = commission_value

    def calculate_payroll(self):
        """
        Calculates and returns the weekly salary for a CommissionEmployee.
        Leverages the base class (SalaryEmployee) for fixed salary and adds commission.
        """
        # Call the base class's calculate_payroll to get the fixed weekly salary
        fixed_salary = super().calculate_payroll()
        return fixed_salary + self.commission_value

    def __str__(self):
        return (f"{super().__str__().replace('Salary Employee', 'Commission Employee')}, " # Adjust type string
                f"Commission: ${self.commission_value:.2f}, Total Weekly Salary: ${self.calculate_payroll():.2f}")


# --- HR System Simulation ---
class HRSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            print("Error: Only Employee objects can be added to the HR system.")
            return
        self.employees.append(employee)
        print(f"Added employee: {employee.name} (ID: {employee.emp_id})")

    def run_payroll(self):
        print("\n--- Running Weekly Payroll ---")
        total_payroll_cost = 0
        if not self.employees:
            print("No employees in the system.")
            return

        for employee in self.employees:
            try:
                salary = employee.calculate_payroll()
                print(f"Processing payroll for {employee.name} (ID: {employee.emp_id}): ${salary:.2f}")
                total_payroll_cost += salary
            except Exception as e:
                print(f"Error calculating payroll for {employee.name} (ID: {employee.emp_id}): {e}")
        print(f"--- Total Weekly Payroll Cost: ${total_payroll_cost:.2f} ---")

    def display_employees(self):
        print("\n--- Current Employees ---")
        if not self.employees:
            print("No employees in the system.")
            return
        for employee in self.employees:
            print(employee)



if __name__ == "__main__":
    hr_system = HRSystem()


    try:
        john = SalaryEmployee("EMP001", "John Doe", 1000)
        alice = HourlyEmployee("EMP002", "Alice Smith", 40, 25) # 40 hours * $25/hour = $1000
        bob = CommissionEmployee("EMP003", "Bob Johnson", 600, 200) # $600 fixed + $200 commission = $800
        carol = SalaryEmployee("EMP004", "Carol White", 1200)
        david = HourlyEmployee("EMP005", "David Brown", 35, 30) # 35 hours * $30/hour = $1050
        eve = CommissionEmployee("EMP006", "Eve Davis", 700, 350) # $700 fixed + $350 commission = $1050

      
        hr_system.add_employee(john)
        hr_system.add_employee(alice)
        hr_system.add_employee(bob)
        hr_system.add_employee(carol)
        hr_system.add_employee(david)
        hr_system.add_employee(eve)

          
        hr_system.display_employees()

        
        hr_system.run_payroll()

    except ValueError as ve:
        print(f"Initialization Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

