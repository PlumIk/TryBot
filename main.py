from vk_api.longpoll import VkEventType

from Data.SceneWork.SceneKeeper import SceneLoader
from Models.SceneParamsExample import SceneParams
from VkMessenger.VkMessengerMain import VkMessengerMain

if __name__ == "__main__":
    ''' Инициализирует программу '''
    vk = VkMessengerMain()
    scenes = SceneLoader()
    for event in vk.get_long_pool().listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                params = SceneParams()
                params.USER_MESSAGE = event.text
                scenes.find_scene(event.user_id).start_work(event.user_id, params)
