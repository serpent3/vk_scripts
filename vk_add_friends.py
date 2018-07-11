import argparse
import time
import vk_api
import random

from vk_auth import vk_auth


# Список возможных друзей этого аккаунта 
def vk_getSuggestions(vk, s_filter=""):
    get = vk.friends.getSuggestions(filter=s_filter)
    for i in get["items"]:
        yield i['id']


if __name__ == '__main__':
    parent_parser = argparse.ArgumentParser(add_help=True)
    parent_parser.add_argument('-l', action='store', help='Логин от вк аккаунта')
    parent_parser.add_argument('-p', action='store', help='Пароль от вк аккаунта')
    args = parent_parser.parse_args()

    vk = vk_auth(args.l, args.p)
    
    for i in vk_getSuggestions(vk, "mutual"):
        r = vk.friends.add(user_id=i)
        print("{}".format("Ok" if r == 1 else r))
        # Пауза от 12 до 50 секунд
        time.sleep(random.random()*random.randrange(9, 26) + random.randrange(11, 24))
    
