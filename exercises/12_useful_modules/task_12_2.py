# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress

ranges = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

def convert_ranges_to_ip_list(ranges_list):
    """
    docs string
    """
    result = []
    for ip_range in ranges_list:
        try:
            ipaddress.ip_network(ip_range)
            # print(ip_range,'correct ip')
            result.append(ip_range)
        except ValueError:
            # print(ip_range, 'not correct ip')
            # print(ip_range.split('-'))
            ip_addr = ip_range.split('-')[0] #str type
            ip_addr_last_octet=ip_range.split('-')[-1].split('.')[-1]
            # print('ip_addr=',ip_addr)
            # print('ip_addr_last_octet=',ip_addr_last_octet)
            for last_octet in range(int(ip_addr.split('.')[-1]),int(ip_addr_last_octet)+1):
                modified_ip=ip_addr.split('.')
                modified_ip[-1]=str(last_octet)
                ip_to_append='.'.join(modified_ip)
                result.append(ip_to_append)
    # print('result=',result)
    return(result)

convert_ranges_to_ip_list(ranges)
