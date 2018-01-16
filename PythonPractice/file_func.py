
#f = open('test.txt')

#print(f.name)
#f.close()

#with open('test.txt', 'r') as f:
    #f_content = f.read()
    #f_content = f.readline()
    #print(f_content)


# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line, end='')

# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.writelines(line)

# with open('image.png', 'rb') as rf:
#     with open('image1.png', 'wb') as wf:
#         for line in rf:
#             wf.writelines(line)


with open('test1.txt', 'r') as f:
    try:
        for line in f:
            print(line)
    except IOError:
        print('Unable to read the file')
    finally:
        print('You have read the file')


