class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

        #Employee.num_of_emp += 1

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('John','Smith')
emp_1.fullname = 'Ashu Saini'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname