# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
result=ospf_route.strip().split()
Prefix,AD_Metric,NextHop,LastUpdate,OutboundInterface=result[0],result[1].strip('[]'),result[3].strip(','),result[4].strip(','),result[5]

print(f'''
{'Prefix':20} {Prefix:15}
{'AD/Metric':20} {AD_Metric:15}
{'Next-Hop':20} {NextHop:15}
{'Last update':20} {LastUpdate:15}
{'Outbound Interface':20} {OutboundInterface:15}
''')





#print(test)
###
#result[1].strip('[]')
#print(result)
#print(type(result))
###