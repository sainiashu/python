import sqlite3
from employeeclass import  Employee

#conn = sqlite3.connect('employee.db')
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employee(
                 first text,
                 last text,
                 pay integer
                 )""")

emp_1 = Employee('John','Doe', 5000)
emp_2 = Employee('Test','Doe', 6000)

c.execute("INSERT INTO employee VALUES(?,?,?)",(emp_1.first, emp_1.last, emp_1.pay))
#
# # use below recommended scripts
c.execute("INSERT INTO employee VALUES(:first, :last, :pay)",{'first':emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
#
# conn.commit()

#c.execute("SELECT *FROM employee WHERE last ='Smith'")

c.execute("SELECT *FROM employee WHERE last =?",('Doe',))

c.execute("SELECT *FROM employee WHERE last =:last",{'last':'Doe'})

#print(c.fetchone())
print(c.fetchall())
#c.fetchmany(5)
#c.fetchall()

conn.commit()

conn.close()