# -*- coding: utf-8 -*-
"""
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка,
где есть MAC-адрес, должна быть обработана таким образом, чтобы
на стандартный поток вывода была выведена таблица вида:

100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.
sw1#sh mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
 100    01bb.c580.7000    DYNAMIC     Gi0/1
 200    0a4b.c380.7c00    DYNAMIC     Gi0/2
 300    a2ab.c5a0.700e    DYNAMIC     Gi0/3
 10     0a1b.1c80.7000    DYNAMIC     Gi0/4
 500    02b1.3c80.7b00    DYNAMIC     Gi0/5
 200    1a4b.c580.7000    DYNAMIC     Gi0/6
 300    0a1b.5c80.70f0    DYNAMIC     Gi0/7
 10     01ab.c5d0.70d0    DYNAMIC     Gi0/8
 1000   0a4b.c380.7d00    DYNAMIC     Gi0/9
"""

with open('CAM_table.txt','r') as f:
    for line in f:
        printline=line.split()

        if len(printline)==4 and printline[0][0].isdigit():

            print(f'{printline[0]:<8}{printline[1]:<20}{printline[3]:<8}')
