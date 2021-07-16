# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

list_of_ips=['8.8.8.8','127.0.0.1','192.160.0.1']


def ping_ip_addresses(ip_addresses_list):
    """
    docstring
    """
    alive_list=[]
    dead_list=[]
    for ip in ip_addresses_list:
        reply=subprocess.run(['ping','-c','3','-n',ip],stdout=subprocess.PIPE)
        if reply.returncode==0:
            alive_list.append(ip)
        else:
            dead_list.append(ip)

    return(alive_list,dead_list)

ping_ip_addresses(list_of_ips)