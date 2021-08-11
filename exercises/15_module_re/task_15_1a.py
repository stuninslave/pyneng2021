# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""

import re

def get_ip_from_cfg(filename):
    result = {}
    with open(filename) as file:
        regex_ipmask = r' ip address (?P<ip>\S+) (?P<mask>\S+)'
        regex_intf = r'interface (?P<intf>\S+)'
        for line in file:
            match_ipmask = re.search(regex_ipmask, line)
            match_intf = re.search(regex_intf, line)
            if match_intf:
                intf=match_intf.group('intf')
            if match_ipmask:
                list_temp = (match_ipmask.group('ip'), match_ipmask.group('mask'))
                result.setdefault(intf)
                result[intf] = list_temp

    return(result)

print(get_ip_from_cfg('config_r1.txt'))