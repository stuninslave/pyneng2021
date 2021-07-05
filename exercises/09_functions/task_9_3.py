# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    access_ports={}
    trunk_ports={}
    with open(config_filename, 'r') as file:

        for line in file:

            if line.startswith('interface'):

                key=line.rstrip().split()[-1] #remember KEY for dict

            elif 'switchport trunk allowed' in line:

                digit_vlan_list=[int(item) for item in line.rstrip().split()[-1].split(',')]
                trunk_ports.setdefault(key)
                trunk_ports[key]=digit_vlan_list           #write list of trunk allowed vlans to KEY

            elif 'switchport access vlan' in line:
                access_vlan=int(line.rstrip().split()[-1])
                access_ports.setdefault(key)
                access_ports[key]=access_vlan                 #write access vlan with KEY


    #print(access_ports)
    #print(trunk_ports)
    result=tuple()
    result=(access_ports,trunk_ports)
    return(result)

get_int_vlan_map('config_sw1.txt')