import sqlite3
from employeeclass import Employee

#conn = sqlite3.connect('employee.db')
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees(
                 first text,
                 last text,
                 pay integer
                 )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES(:first, :last, :pay)",
              {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emp_by_name(lastname):
    c.execute("SELECT *FROM employees WHERE last =:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay= :pay WHERE first = :first AND last= :last""",
        {'first':emp.first, 'last':emp.last, 'pay':pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first=:first AND last=:last",
                  {'first':emp.first, 'last': emp.last})


emp_1 = Employee('John','Doe', 5000)
emp_2 = Employee('Test','Doe', 6000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emp_by_name('Doe')
print(emps)

update_pay(emp_2, 85000)
remove_emp(emp_1)

emps = get_emp_by_name('Doe')
print(emps)
#
# c.execute("INSERT INTO employee VALUES(?,?,?)",(emp_1.first, emp_1.last, emp_1.pay))
# #
# # # use below recommended scripts
# c.execute("INSERT INTO employee VALUES(:first, :last, :pay)",{'first':emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
# #
# # conn.commit()
#
# #c.execute("SELECT *FROM employee WHERE last ='Smith'")
#
# #c.execute("SELECT *FROM employee WHERE last =?",('Doe',))
#
# #c.execute("SELECT *FROM employee WHERE last =:last",{'last':'Doe'})
#
# #print(c.fetchone())
# print(c.fetchall())
# #c.fetchmany(5)
#c.fetchall()
#
# #conn.commit()

conn.close()