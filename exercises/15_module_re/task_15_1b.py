# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a
на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
образом, чтобы в значении словаря она возвращала список кортежей
для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
несколько кортежей. Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность
IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""

import re

def get_ip_from_cfg(filename):
    result = {}
    with open(filename) as file:
        regex_ipmask = r' ip address (?P<ip>\S+) (?P<mask>\S+)'
        regex_intf = r'interface (?P<intf>\S+)'
        ip_addr_list=[]
        list_temp=()
        intf=''
        for line in file:

            match_ipmask = re.search(regex_ipmask, line)
            match_intf = re.search(regex_intf, line)
            if match_intf:
                intf=match_intf.group('intf')

            if match_ipmask:
               list_temp = (match_ipmask.group('ip'), match_ipmask.group('mask'))
               ip_addr_list.append(list_temp)
               print(ip_addr_list)
            if '!' in line and intf and ip_addr_list:
                result.setdefault(intf)
                result[intf] = ip_addr_list
                intf=''
                ip_addr_list = []

    return(result)

print(get_ip_from_cfg('config_r2.txt'))