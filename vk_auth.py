import vk_api


def vk_auth(login, passw):
    vk_session = vk_api.VkApi(login, passw)
    vk_session.auth()
    vk = vk_session.get_api()
    return vk
