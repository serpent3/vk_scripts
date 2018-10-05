#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import time
import csv
import vk_api


def vk(args):
    vk_session = vk_api.VkApi(args.login, args.passw)
    vk_session.auth()
    vk = vk_session.get_api()
    
    # Только посты за последнюю неделю 
    end_time = int(time.time())
    start_time = end_time - 604800 
    
    q = vk.newsfeed.search(q=args.q, start_time=start_time, end_time=end_time, count=200)
    
    with open(args.f + ".csv", 'w',encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        for item in q['items']:
            if len(item['text']) < int(args.len): 
                writer.writerow(["https://vk.com/wall%d_%d" % (item['owner_id'], item['id']), item['text']])
                

if __name__ == '__main__':
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('-login', action='store', help='Логин от вк аккаунта')
    parent_parser.add_argument('-passw', action='store', help='Пароль от вк аккаунта')
    parent_parser.add_argument('-q', action='store', help='Запрос для поиска, например "нужен программист"')
    parent_parser.add_argument('-f', action='store', help='Имя файла куда сохранять результаты')
    parent_parser.add_argument('-len', action='store', help='ограничение подлинне поста')
    args = parent_parser.parse_args()
    
    vk(args) 
    

    
    
    
    
    
    
    
    
    
    
