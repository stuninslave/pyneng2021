# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
alive=['1.1.1.1','2.2.2.2']
dead=['192.168.0.7','192.168.2.2']

from tabulate import tabulate

def print_ip_table(alive_ip_list,dead_ip_list):
    """
    docstring
    """
    result = dict.fromkeys(['Reachable','Unreachable'])
    result['Reachable'] = alive_ip_list
    result['Unreachable'] = dead_ip_list
    print(tabulate(result,headers="keys"))


print_ip_table(alive,dead)