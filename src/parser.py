def parser(file_path: str, filename_eng: str = 'English', filename_rus: str = 'Russian') -> None:
    """
    Парсит файл по пути file_path и записывает резульаты
    в файлы filename_eng и filename_rus
    """

    with open(file_path, 'r', encoding='utf8') as file:
        while True:
            string_list = file.readline().split('\t')
            try:
                if string_list[0][0] in ('#', '\n'):
                    continue
            except IndexError:
                break

            words = [word.strip() for word in string_list[0].split(';')]
            translations = [word.strip() for word in string_list[1].split(';')]
            with open(f'{filename_eng}.txt', 'a', encoding='utf8') as english_file, \
                    open(f'{filename_rus}.txt', 'a', encoding='utf8') as rus_file:
                for word in words:
                    for translation in translations:
                        english_file.write(f'{word}\n')
                        rus_file.write(f'{translation}\n')
