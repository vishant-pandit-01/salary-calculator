
class Company:
    
    def salary(self):
        name = input("Enter your name: ")
        phone = input("Enter your phone: ")
        total_salary = float(input("Enter your monthly salary: "))
        leave_days = int(input("Enter number of leave days: "))
        bonus = float(input("Enter bonus amount: "))
        overtime_days = int(input("Enter overtime days: "))
        
        total_days = 30
        attendance = total_days - leave_days
        per_day_salary = total_salary / total_days
        deduction = per_day_salary * leave_days
        overtime_pay = per_day_salary * overtime_days
        
        final_salary = total_salary - deduction + bonus + overtime_pay

        print("\n===== Salary Details =====")
        print("Name:", name)
        print("Phone:", phone)
        print("Attendance:", attendance)
        print("Leave Deduction:", round(deduction, 2))
        print("Bonus:", bonus)
        print("Overtime Pay:", round(overtime_pay, 2))
        print("Final Salary:", round(final_salary, 2))


emp = Company()
emp.salary()
