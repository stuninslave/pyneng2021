# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
import re
import csv

def write_dhcp_snooping_to_csv(filenames,output):
    csv_list=[]
    Columns_name=['switch','mac','ip','vlan','interface']
    csv_list.append(Columns_name)
    for filename in filenames:
        with open(filename,'r') as f:
            switch=filename.split('_')[0] #  записть в переменную имя свича
            for line in f:
                # Распарсить строку конфига по regexp в лист.
                regex=r'(?P<mac>\S\S:\S\S:\S\S:\S\S:\S\S:\S\S)\s+(?P<ip>\d+\.\d+\.\d+\.\d+)\s+\d+\s+\S+\s+(?P<vlan>\d+)\s+(?P<intf>\S+)'
                match=re.search(regex,line)
                if match:
                    mac,ip,vlan,intf=match.groups()
                    list1=[switch,mac,ip,vlan,intf]
                    csv_list.append(list1)
                # дописать распарсенную строку в список списков с указанием имени свича

    #экспорт списка списков в CSV
    #print(csv_list)
    with open(output,'w') as dest_file:
        writer= csv.writer(dest_file, quoting=csv.QUOTE_NONNUMERIC)
        for row in csv_list:
            writer.writerow(row)

write_dhcp_snooping_to_csv(['sw1_dhcp_snooping.txt','sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt'],'sw_csv.txt')

