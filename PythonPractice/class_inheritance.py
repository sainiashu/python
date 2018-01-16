class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+ last +'@company.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        #super(Developer,self).__init__( first, last, pay)
        Employee.__init__(self,first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first, last, pay, employee=None):
        Employee.__init__(self,first, last, pay)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    def add_emp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_emps(self):
        for emp in self.employee:
            print('-->', emp.fullname())


dev_1 = Developer('Test1', 'User1', 5000, 'Python')
dev_2 = Developer('Test2', 'User2', 6000, 'Java')

mgr_1 = Manager('John', 'Smith', '9000', [dev_1])

#print(isinstance(mgr_1,Developer))
print(issubclass(Manager,Developer))

#print(mgr_1.email)

#mgr_1.add_emp(dev_2)
#mgr_1.remove_emp(dev_1)
#mgr_1.print_emps()

#print(dev_1.email)
#print(dev_1.prog_lang)


#print(help(Developer))
#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)

