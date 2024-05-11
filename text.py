# Функция для обработки текстового файла
def process_file(input_file, output_file):
    ips_seen = set()  # Множество для хранения уникальных IP-адресов

    with open(input_file, 'r') as file:
        lines = file.readlines()

    filtered_lines = [line.strip() for line in lines if 'Wrong Hash' in line] # Фильтрация записей с "Wrong Hash"

    with open(output_file, 'w') as file:
        for line in filtered_lines:
            ip = line.split()[1]  # Извлечение IP-адреса
            if ip not in ips_seen:
                ips_seen.add(ip)  # Добавление IP-адреса в множество
                file.write(f"iptables -A INPUT -s {ip} -j DROP\n")  # Запись в новый файл

# Запрос пользовательского ввода для входного и выходного файлов
input_file = input("Введите путь к входному файлу: ")
output_file = input("Введите путь к выходному файлу: ")

# Вызов функции обработки файла
process_file(input_file, output_file)
print("Работа выполнена успешно!")
