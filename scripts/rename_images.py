import os
from pathlib import Path

def rename_images(folder_path, start_number):
    """
    Переименовывает все PNG-файлы в указанной папке,
    присваивая им порядковые номера, начиная с указанного.
    
    Args:
        folder_path (str): Путь к папке с изображениями.
        start_number (int): Номер, с которого начинается нумерация.
    """
    png_files = [file for file in os.listdir(folder_path) if file.endswith('.png')]
    
    for i, file in enumerate(png_files, start=start_number):
        old_path = os.path.join(folder_path, file)
        new_filename = f'{i}.png'
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)
        print(f'Renamed {file} to {new_filename}')

# Запрос пользователя на ввод пути к папке и номера первой картинки
folder_path = input('Введите путь к папке с изображениями: ')
start_number = int(input('Введите номер, с которого начинается нумерация: '))

# Вызов функции для переименования файлов
rename_images(folder_path, start_number)