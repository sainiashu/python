a = 5
while(a > 0):
    print(a)
    a-=1

while True:
    user_command = raw_input('Enter your command :')
    if user_command =='quit':
        break
    else:
        print('You typed :' + user_command)
