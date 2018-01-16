import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('sample-dir-one'):
    print('Dir name one')

with change_dir('sample-dir-two'):
    print('Dir name two')
