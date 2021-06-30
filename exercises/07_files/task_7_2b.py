# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv

filename=argv[1]
dst_filename=argv[2]

with open(filename,'r') as src, open(dst_filename,'w') as dst:
    for line in src:
        if line.startswith('!'):
            continue
        else:
            ignored=False
            for command in ignore:
                if command in line:
                    ignored=True
                    break
            if ignored==False:
                dst.write(line)