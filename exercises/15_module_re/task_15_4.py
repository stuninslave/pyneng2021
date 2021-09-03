# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""

import re

def get_ints_without_description(filename):
        regex = r'interface (?P<intf_name>\S+)'
        is_desc = False
        interface_name = ''
        result=[]
        with open(filename) as file:
            for line in file:
                if line.startswith('interface'):
                    match = re.search(regex,line)
                    interface_name = match.group('intf_name')
                    #print('intf line',interface_name)
                if line.startswith(' description'):
                    is_desc = True

                if line.startswith('!'):
                    if interface_name and not is_desc:
                        #print('desc OK')
                        result.append(interface_name)
                    interface_name = ''
                    is_desc = False



        print(result)
        return(result)

get_ints_without_description('config_r1.txt')