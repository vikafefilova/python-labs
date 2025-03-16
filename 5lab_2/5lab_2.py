#1
'''import os
import shutil
import sys

def find_small_files(folder):
    small_files = []
    # Проход по всем файлам в указанной папке
    for dirpath, _, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # Проверка размера файла
            if os.path.getsize(file_path) < 2048:  # 2 КБ = 2048 байт
                small_files.append(file_path)
    return small_files

def main(folder):
    # Получаем список малых файлов
    small_files = find_small_files(folder)
    # Выводим список найденных файлов
    if small_files:
        print("Найдены файлы меньше 2К:")
        for file in small_files:
            print(file)
        # Создаем папку small
        small_folder = os.path.join(folder, "small")
        os.makedirs(small_folder, exist_ok=True)
        # Копируем найденные файлы в папку small
        for file in small_files:
            shutil.copy(file, small_folder)
        print(f"Все найденные файлы скопированы в папку: {small_folder}")
    else:
        print("Файлы меньше 2К не найдены.")

if __name__ == "__main__":
    # Проверяем передан ли путь к папке
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = os.getcwd()  # Сканируем текущую папку по умолчанию
    main(folder_path)'''




#2
'''import os
import argparse

def check_files_in_directory(dirpath, filenames):
    present_files = []
    absent_files = []

    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        if os.path.isfile(file_path):
            present_files.append(filename)
        else:
            absent_files.append(filename)

    return present_files, absent_files

def folder_info(dirpath):
    total_files = 0
    total_size = 0

    for _, _, files in os.walk(dirpath):
        total_files += len(files)
        total_size += sum(os.path.getsize(os.path.join(dirpath, f)) for f in files)

    return total_files, total_size

def main(dirpath, filenames):
    if filenames:
        present_files, absent_files = check_files_in_directory(dirpath, filenames)

        # Выводим списки на экран
        print("Присутствующие файлы:")
        for file in present_files:
            print(file)

        print("\nОтсутствующие файлы:")
        for file in absent_files:
            print(file)

        # Запись списков в файлы
        with open("present_files.txt", "w") as present_file:
            for file in present_files:
                present_file.write(file + "\n")

        with open("absent_files.txt", "w") as absent_file:
            for file in absent_files:
                absent_file.write(file + "\n")

    else:
        total_files, total_size = folder_info(dirpath)
        print(f"В папке '{dirpath}' всего файлов: {total_files}")
        print(f"Общий размер файлов: {total_size} байт")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Проверка наличия файлов в директории.")
    parser.add_argument("--dirpath", type=str, default=os.getcwd(), help="Путь к папке (по умолчанию текущая папка).")
    parser.add_argument("--files", nargs='*', help="Список имен файлов для проверки.")

    args = parser.parse_args()
    main(args.dirpath, args.files)'''




#3
import os
import argparse

def create_missing_files(dirpath, missing_files):
    created_files = []
    for filename in missing_files:
        file_path = os.path.join(dirpath, filename)
        # Создаем файл, если он не существует
        if not os.path.isfile(file_path):
            with open(file_path, 'w') as f:
                f.write(f'This is a placeholder for {filename}\n')
            created_files.append(filename)
    return created_files

def main(dirpath, missing_files_file):
    if not os.path.isfile(missing_files_file):
        print(f'Файл со списком отсутствующих файлов не найден: {missing_files_file}')
        return

    with open(missing_files_file, 'r') as f:
        missing_files = [line.strip() for line in f if line.strip()]

    if not missing_files:
        print('Список отсутствующих файлов пуст.')
        return

    created_files = create_missing_files(dirpath, missing_files)

    if created_files:
        print(f'Созданы следующие отсутствующие файлы в директории "{dirpath}":')
        for file in created_files:
            print(file)
    else:
        print('Нет отсутствующих файлов для создания.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Создание отсутствующих файлов из списка.")
    parser.add_argument("--dirpath", type=str, required=True, help="Путь к папке, где будут созданы файлы.")
    parser.add_argument("--missing_files_file", type=str, required=True, help="Путь к файлу со списком отсутствующих файлов.")

    args = parser.parse_args()
    main(args.dirpath, args.missing_files_file)