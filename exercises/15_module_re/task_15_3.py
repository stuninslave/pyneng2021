# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re

def convert_ios_nat_to_asa(ios_file,asa_file):
    regex_ios = r'ip nat inside source static tcp (?P<ip>\S+) (?P<port>\d+)\s+\w+\s+\w+\S+\s+(?P<num>\d+)'

    with open(ios_file,'r') as file, open(asa_file, 'w') as dst:
        for line in file:

            match = re.search(regex_ios, line)
            if match:
                ip, port, port2 = match.groups()
                write_line = f'object network LOCAL_{ip}\n host {ip}\n nat (inside,outside) static interface service tcp {port} {port2}\n'
                dst.write(write_line)


convert_ios_nat_to_asa('cisco_nat_config.txt','dst_file.txt')
