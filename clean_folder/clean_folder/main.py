from pathlib import Path
import shutil
import sys
import file_parser as parser
from normalize import normalize


def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archive(filename: Path, target_folder: Path):
    # Створюємо папку для архіву
    target_folder.mkdir(exist_ok=True, parents=True)
    # Створюємо папку куди розпакуємо архів
    # Беремо суфікс у файла і удаляємо replace(filename.suffix, '')
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))

    # Створюємо папку для архіву з іменем файлу
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Це не архів {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Помилка видалення папки {folder}')


def main(folder: Path):
    parser.scan(folder)
    for file in parser.JPEG_IMAGES:
        handle_media(file, folder / 'images')
    for file in parser.JPG_IMAGES:
        handle_media(file, folder / 'images')
    for file in parser.PNG_IMAGES:
        handle_media(file, folder / 'images')
    for file in parser.SVG_IMAGES:
        handle_media(file, folder / 'images')
    for file in parser.MP3_AUDIO:
        handle_media(file, folder / 'audio')

    for file in parser.MY_OTHER:
        handle_other(file, folder / 'MY_OTHER')
    for file in parser.ARCHIVES:
        handle_archive(file, folder / 'archives')

    # Виконуємо реверс списку для того щоб видалити всі папки
    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)



def start_scan():
    try:
        sys.argv[1]
    except IndexError:
        print(f'Cant start program because of {IndexError:}.')
        print('Correct input -> python main.py "Folder for Start name"')
    else:
        folder_for_scan = Path(sys.argv[1])
        print(f'Start in folder {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())

if __name__ == '__main__':
    start_scan()


# TODO: запускаємо:  python3 main.py `назва_папки_для_сортування`