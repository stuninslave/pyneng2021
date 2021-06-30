# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_addr=input('Введите IP address? ')


octet1=int(ip_addr.split('.')[0])
octet2=int(ip_addr.split('.')[1])
octet3=int(ip_addr.split('.')[2])
octet4=int(ip_addr.split('.')[3])

if octet1 >= 0:
    if (octet1==octet2==octet3==octet4==0):
        print('unassigned')
    elif octet1 <=223:
        print('unicast')
    elif octet1 <=239:
        print('multicast')
    elif octet1<=255 and (octet2<octet1 or octet3< octet1 or octet4<octet1):
        print('unused')
    elif octet1==octet2==octet3==octet4==255:
        print('local broadcast')
