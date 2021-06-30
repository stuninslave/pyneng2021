# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

config_template = {
'access' : '\n'.join(access_template),
'trunk' : '\n'.join(trunk_template)
}

questions = {
'access':'Введите номер VLAN',
'trunk':'Введите разрешенные VLANы'
}

interface_type = input('Введите тип интерфейса? (access, trunk) ')
interface_number = input('Введите тип и номер интерфейса? ')
vlan = input(questions[interface_type]+' ')
print(f'interface {interface_number}')
print(f'''{config_template[interface_type].format(vlan)}
'''
)