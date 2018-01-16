class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+ last +'@company.com'

        Employee.num_of_emp +=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Test1', 'User1', 5000)
emp_2 = Employee('Test2', 'User2', 6000)



#print(emp_1.fullname())
#print(emp_2.fullname())
#print(emp_1.email)
#print(emp_2.email)


print(emp_1.pay)
print(Employee.raise_amount)
#emp_1.apply_raise()
print(emp_1.pay)

#print(emp_1.__dict__)
#print(Employee.__dict__)
