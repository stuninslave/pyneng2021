# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
IpCorrect=False

while IpCorrect==False:
    ip_addr=input('Введите IP address? ')
    ip_addr_dec=ip_addr.split('.')

    try:
        octet1=int(ip_addr.split('.')[0])
        octet2=int(ip_addr.split('.')[1])
        octet3=int(ip_addr.split('.')[2])
        octet4=int(ip_addr.split('.')[3])

        if len(ip_addr_dec) == 4 and octet1<=255 and octet2<=255 and octet3<=255 and octet4<=255:

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
            IpCorrect=True
        else:
            print('Неправильный IP address')

    except (ValueError,IndexError):
        print('Неправильный IP-адрес')