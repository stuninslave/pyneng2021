# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    access_ports={}
    trunk_ports={}
    access_port=False
    arldy_written=False
    with open(config_filename, 'r') as file:

        for line in file:
            if line.startswith('!'):
                if access_port and not alrdy_written:
                    access_ports.setdefault(key)
                    access_ports[key]=1
                    access_port=False
                    alrdy_written=True

            if line.startswith('interface') and 'thernet' in line:
                access_port=False
                alrdy_written=False
                key=line.rstrip().split()[-1] #remember KEY for dict
            elif 'switchport mode access' in line:
                access_port=True # enabling access port tumbler

            elif 'switchport trunk allowed' in line:

                digit_vlan_list=[int(item) for item in line.rstrip().split()[-1].split(',')]
                trunk_ports.setdefault(key)
                trunk_ports[key]=digit_vlan_list           #write list of trunk allowed vlans to KEY
                alrdy_written=True

            elif 'switchport access vlan' in line:
                access_vlan=int(line.rstrip().split()[-1])
                access_ports.setdefault(key)
                access_ports[key]=access_vlan                 #write access vlan with KEY
                alrdy_written=True
                access_port=False #disabling no specific access vlan Checking tumbler

    #print(access_ports)
    #print(trunk_ports)
    result=tuple()
    result=(access_ports,trunk_ports)
    print(result)
    return(result)



get_int_vlan_map('config_sw2.txt')