from Models.SceneParamsExample import SceneParams
from Scenes.SceneExample import SceneExample
import Data.MessegesTexts as texts


class HelloScene(SceneExample):
    """Сцена приветствия."""

    def __init__(self):
        """Инициализирует экземпляр класса."""
        self.SCENE_NUM = 1
        self.LAST_VALID_SCENE = self.SCENE_NUM

    def start_work(self, uid: int, params: SceneParams) -> None:
        """
        Метод работы сцены.
        :param params: Параметры сцены.
        :param uid: ID пользователя.
        """
        self.wright_message(uid, texts.HELLO_TEXT)
