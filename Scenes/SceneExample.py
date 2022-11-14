import Data.MessegesTexts as texts
from Data.SceneWork.SceneKeeper import SceneLoader
from Models.SceneParamsExample import SceneParams
from VkMessenger.VkMessengerMain import VkMessengerMain


class SceneExample:
    """Базовый класс сцены."""

    SCENE_NUM: int = 0
    """Номер данной сцены."""

    LAST_VALID_SCENE: int = 0
    """Номер последней сцены, которую можно безопасно загрузить."""

    VkMessenger: VkMessengerMain = VkMessengerMain()
    """Экземпляр объекта для связи с ВК."""

    Scenes: SceneLoader = SceneLoader()
    """Класс для переключения сцен"""

    DEFAULT_SCENE: int = 1
    """Сцена по умолчанию."""

    def start_work(self, uid: int, params: SceneParams) -> None:
        """
        Метод работы сцены.
        :param params: Параметры сцены.
        :param uid: ID пользователя.
        """
        self.wright_message(uid, texts.ERROR_TEXT)

    def wright_message(self, uid: int, message: str) -> None:
        """
        Отправляет запрос на отправку сообщения пользователю.
        :param uid: ID пользователя.
        :param message: Сообщение для пользователя.
        """
        self.VkMessenger.write_msg(uid, message)

    def set_default(self, uid: int):
        """
        Возвращает на стартовую сцену.
        :param uid: ID пользователя.
        """
        SceneLoader.set_scene_num(uid, self.DEFAULT_SCENE)
        SceneLoader.find_scene(uid).start_work(uid, None)
