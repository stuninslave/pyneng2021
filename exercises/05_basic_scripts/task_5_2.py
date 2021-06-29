# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

prefix=input('Введите IP-подсеть в формате x.x.x.x/yy? ')
network=prefix.split('/')[0]
mask=prefix.split('/')[-1]

octet1=int(network.split('.')[0])
octet2=int(network.split('.')[1])
octet3=int(network.split('.')[2])
octet4=int(network.split('.')[3])
mask=int(mask)
mask_bin='1'*mask+'0'*(32-mask)
moctet1=int(mask_bin[0:8], 2)
moctet2=int(mask_bin[8:16], 2)
moctet3=int(mask_bin[16:24], 2)
moctet4=int(mask_bin[24:32], 2)


print(f'''
Network:
{octet1:<10}{octet2:<10}{octet3:<10}{octet4:<10}
{octet1:08b}  {octet2:08b}  {octet3:08b}  {octet4:08b}

Mask:
/{mask}
{moctet1:<10}{moctet2:<10}{moctet3:<10}{moctet4:<10}
{moctet1:08b}  {moctet2:08b} {moctet3:08b} {moctet4:08b}
''')