import os
#print(os.getcwd())


from datetime import  datetime

#print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'tem.txt')
print(file_path)

# for dirpath, dirname, filenames in os.walk('F:\PythonLearning\PythonPractice'):
#     print('Current Path :', dirpath)
#     print('Current Dir :', dirname)
#     print('File name :', filenames)
#     print()




#print(os.stat('test2.txt')).st_mtime
#mod_time = os.stat('test2.txt').st_mtime
#print(datetime.fromtimestamp(mod_time))


#os.chdir('F:\PythonLearning')
#print(os.getcwd())

#test = 'F:\PythonLearning'
#print(os.listdir(test))


#os.mkdir('os_demo2')
#os.rename('test1.txt', 'test2.txt')
#os.rmdir('os_demo2')
#os.makedirs('os_demo2/test')