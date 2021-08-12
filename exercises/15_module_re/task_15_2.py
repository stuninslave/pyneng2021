# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import re

def parse_sh_ip_int_br(filename):
    regex = r'(?P<intf>\w+\S+) \s+ (?P<ip>\S+) \s+\w+\s+\w+\s+(?P<status>\w+\s?\w+)\s+(?P<protocol>\w+)'
    result=[]
    with open(filename) as file:
        for line in file:
            match=re.search(regex,line)
            if match:
                result.append(match.groups())

    return(result)

parse_sh_ip_int_br('sh_ip_int_br.txt')