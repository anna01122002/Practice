import os
global wd
wd = input('Введите путь рабочей директории: ')
try:
    os.chdir(wd)
except FileNotFoundError:
    os.mkdir(wd)
    os.chdir(wd)
def backwk():
    lastdir = os.path.dirname(os.getcwd())
    if os.getcwd() != wd:
        os.chdir(lastdir)
        print(os.getcwd())
    else:
        print('Нельзя выходить за рабочую директорию')