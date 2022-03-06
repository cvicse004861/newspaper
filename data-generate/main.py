import pandas as pd
import json
import os

def generate():

    w = True
    v = '22030201'

    if not os.path.exists('out'):
        os.mkdir('out')

    #收费站
    station_node = {}
    station_csv = pd.read_csv('raw/station.csv')
    for i in range(len(station_csv)):
        id = station_csv.id[i] #国标id
        name = station_csv.name[i] #名称
        lat = station_csv.lat[i] #纬度
        lng = station_csv.lng[i] #经度
        station_node[id] = {
            'name': name,
            'lat': lat,
            'lng': lng
        }
    if w:
        station_node_json = json.dumps(station_node, ensure_ascii=False)
        with open('out/station.' + v + '.json', 'w', encoding='utf-8') as out:
            out.write(station_node_json)

    #门架
    ganrty_actual_node = {}
    ganrty_virtual_node = {}
    ganrty_csv = pd.read_csv('raw/gantry.csv')
    for i in range(len(ganrty_csv)):
        id = ganrty_csv['收费门架编号'][i]
        name = ganrty_csv['门架名称'][i]
        clazz = ganrty_csv['门架种类'][i]
        lat = ganrty_csv['纬度'][i]
        lng = ganrty_csv['经度'][i]
        hex = ganrty_csv['门架HEX字符串'][i]
        rhex = ganrty_csv['反向门架HEX字符串'][i]
        node = {
            'name': name,
            'lat': lat,
            'lng': lng,
            'hex': hex,
            'rhex': rhex
        }
        if clazz == '虚拟门架':
            ganrty_virtual_node[id] = node
        else:
            ganrty_actual_node[id] = node
    if w:
        ganrty_actual_node_json = json.dumps(ganrty_actual_node, ensure_ascii=False)
        ganrty_virtual_node_json = json.dumps(ganrty_virtual_node, ensure_ascii=False)
        with open('out/gantry.actual.' + v + '.json', 'w', encoding='utf-8') as out:
            out.write(ganrty_actual_node_json)
        with open('out/gantry.virtual.' + v + '.json', 'w', encoding='utf-8') as out:
            out.write(ganrty_virtual_node_json)

    #服务区
    service_node = {}
    service_csv = pd.read_csv('raw/service.csv')
    for i in range(len(service_csv)):
        id = str(service_csv['公路ID'][i]) + str(service_csv['序号'][i]).rjust(6, '0')
        name = service_csv['服务区名称'][i]
        lng = service_csv['服务区经度'][i]
        lat = service_csv['服务区纬度'][i]
        upstream = str(service_csv['服务区上游门架'][i]).split('|')
        downstream = str(service_csv['服务区下游门架'][i]).split('|')
        service_node[id] = {
            'name': name,
            'lng': lng,
            'lat': lat,
            'upstream': upstream,
            'downstream': downstream
        }
    if w:
        service_node_json = json.dumps(service_node, ensure_ascii=False)
        with open('out/service.' + v + '.json', 'w', encoding='utf-8') as out:
            out.write(service_node_json)

    ref_csv = pd.read_csv('raw/ref.csv')
    ref = []
    for i in range(len(ref_csv)):
        current = ref_csv.current[i]
        next = ref_csv.next[i]
        ref.append([current, next])
    if w:
        ref_json = json.dumps(ref, ensure_ascii=False)
        with open('out/ref.' + v + '.json', 'w', encoding='utf-8') as out:
            out.write(ref_json)

if __name__ == '__main__':
    generate()