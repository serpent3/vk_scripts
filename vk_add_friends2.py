import vk_api
import time
import random

login =
passw =

def vk_auth(login, passw):
    vk_session = vk_api.VkApi(login, passw)
    vk_session.auth()
    vk = vk_session.get_api()
    return vk
    
vk = vk_auth(login, passw)

# Список возможных друзей этого аккаунта 
def vk_getSuggestions(vk, s_filter=""):
    get = vk.friends.getSuggestions(filter=s_filter)
    for i in get["items"]:
        yield i['id']


for i in vk_getSuggestions(vk, "mutual"):
    r = vk.friends.add(user_id=i)
    print("{}".format("Ok" if r == 1 else r))
    # Пауза от 12 до 50 секунд
    time.sleep(random.random()*random.randrange(9, 26) + random.randrange(11, 24))
    

    
