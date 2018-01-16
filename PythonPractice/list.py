import  string

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(raw_input('Choose a number :'))
new_list = []
for i in a:
    if i < num:
        new_list.append(i)
print new_list

# print the list
for elem in a:
    print elem

list_of_students = ['John', 'Tom', 'Harry']
name = raw_input('Type name to check :')
if name in list_of_students:
    print('This student is Enrolled')
else:
    print('Student is not Enrolled')


name = 'Testing'
for i in name:
    print 'One Letter of name :' + i