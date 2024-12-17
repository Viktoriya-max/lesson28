def custom_write(file_name, strings):
    strings_positions = {}
    line_number = 1
    file = open(file_name, 'a', encoding='utf-8')
    for i in strings:
        byte = file.tell()
        file.write(f'{i}\n')
        strings_positions.update({(line_number, byte) : str(i)})
        line_number += 1
    file.close()
    return strings_positions

info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)