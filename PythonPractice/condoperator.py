import  os
import  string

grade = int(raw_input('Enter your grade :'))

if grade >= 90:
    print('A grade')
elif grade >= 70:
    print('B grade')
elif grade >= 50:
    print('C grade')
elif grade >= 40:
    print('D grade')
else:
    print('Fail')


