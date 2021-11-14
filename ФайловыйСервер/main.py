import os
import shutil
from settings import *
print('Команды: \n'
      '1.Создание папки \n'
      '2.Удаление папки по имени \n'
      '3.Перемещение между папками \n'
      '4.Создание пустых файлов \n'
      '5.Запись текста в файл \n'
      '6.Просмотр содержимого текстового файла \n'
      '7.Удаление файлов по имени \n'
      '8.Копирование файлов из одной папки в другую \n'
      '9.Перемещение файлов \n'
      '10.Переименование файлов \n')
req = ''
def create():
    c_name = input('Введите имя папки: ')
    new_path = os.getcwd() + os.sep + c_name
    os.mkdir(new_path)
    print('Папка создана')
def delete():
    try:
        d_name = input('Введите имя папки: ')
        d_dir = os.path.dirname(os.getcwd())
        d_cdir = os.getcwd() + os.sep + d_name
        os.rmdir(d_cdir)
    except OSError:
        d_notempty = input('Вы уверены, что хотите удалить непустую папку? (Y / N): ')
        if d_notempty == 'Y':
            shutil.rmtree(d_cdir)
            print('Папка удалена')
        else:
            os.chdir(d_dir)
            print(os.getcwd())
def move():
    move_to = input('Введите путь перемещения: ')
    new_dir = os.getcwd() + os.sep + move_to
    os.chdir(new_dir)
    print(os.getcwd())
def create_empty_file():
    cef_name = input('Введите имя файла: ')
    open(cef_name, 'w')
    print('Путь созданного файла: ' + os.getcwd())
def write():
    w_name = str(input('Введите имя файла: '))
    w = open(w_name, 'w')
    w.write(input('Введите текст для записи в файл: '))
    w.close()
def view_content():
    v_name = str(input('Введите имя файла: '))
    v = open(v_name)
    print(v.read())
def delete_file():
    d_f_name = input('Введите имя файла: ')
    os.remove(d_f_name)
    print('Файл удалён')
def copy():
    global wd
    co_name = input('Введите имя файла: ')
    co_folder = input('Введите имя папки копирования: ')
    shutil.copy(os.getcwd() + os.sep + co_name, wd + os.sep + co_folder)
    print('Файл скопирован')
def move_files():
    global wd
    m_name = input('Введите имя файла:')
    m_folder = input('Введите имя папки перемещения:')
    os.replace(os.getcwd() + os.sep + m_name, wd + os.sep + m_folder + os.sep + m_name)
    print('Файл перемещён')
def rename():
    r_name = input('Введите имя файла: ')
    r_new_name = input('Новое название: ')
    os.rename(os.getcwd() + os.sep + r_name, os.getcwd() + os.sep + r_new_name)
    print('Файл переименован')
while req != '0':
    req = input('Введите номер команды (для выхода введите 0): ')
    if req == '1':
        create()
    elif req == '2':
        delete()
    elif req == '3':
        move()
    elif req == '4':
        create_empty_file()
    elif req == '5':
        write()
    elif req == '6':
        view_content()
    elif req == '7':
        delete_file()
    elif req == '8':
        copy()
    elif req == '9':
        move_files()
    elif req == '10':
        rename()