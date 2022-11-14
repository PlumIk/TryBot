import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

import Data.params as app_params


class VkMessengerMain:
    """Класс для связи с ВК."""

    def __new__(cls):
        """
        Инициализирует экземпляр класса типа Singleton.
        :rtype: object
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(VkMessengerMain, cls).__new__(cls)
            cls.__vk = vk_api.VkApi(token=app_params.token)
        return cls.instance

    def get_long_pool(self) -> VkLongPoll:
        """
        Возвращает класс для взаимодействия с запросами.
        :return: Класс для взаимодействия с запросами.
        """
        return VkLongPoll(self.__vk)

    def write_msg(self, user_id: int, message: str) -> None:
        """
        Пишет сообщение пользователю.
        :param user_id: ID пользователя.
        :param message: Сообщение пользолвателю.
        """
        print(user_id, message)
        self.__vk.method('messages.send',
                         {'user_id': user_id, 'message': message, 'random_id': int(random.random() * 10_000)})
