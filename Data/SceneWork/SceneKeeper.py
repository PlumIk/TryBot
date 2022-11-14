from Scenes.HelloScene import HelloScene
from Scenes.SceneExample import SceneExample


def create_scene(num: int) -> SceneExample:
    """
    Создаёт сцену на осонове её номера.
    :param num: Номер сцены.
    :return: Созданная сцена.
    """
    if num == 0:
        return SceneExample()
    else:
        return HelloScene()


class SceneLoader:
    """Класс харнящий в себе сцены всех пользователей в данный момент ."""

    __scenesNum: dict
    __scenesExample: dict

    def __init_me(self):
        """Инициализация параметров."""
        self.__scenesNum = {}
        self.__scenesExample = {}

    def __new__(cls):
        """Инициализирует экземпляр класса типа Singleton."""
        if not hasattr(cls, 'instance'):
            cls.instance = super(SceneLoader, cls).__new__(cls)
            cls.__init_me(cls)
        return cls.instance

    def set_scene_num(self, uid: int, num: int) -> None:
        """
        Устанавливает сцену для пользователя.
        :param uid: ID пользователя.
        :param scene: экземпляр сцены.
        :param num: Номер сцены.
        """
        if num > 0:
            self.__scenesNum[uid] = num
            self.__scenesExample[uid] = create_scene(num)

    def find_scene(self, uid: int) -> SceneExample:
        """
        Создаёт или достаёт сцену.
        :param uid: ID пользователя.
        """
        if self.__scenesExample.get(uid) is None:
            if self.__scenesNum.get(uid) is None:
                self.__scenesExample[uid] = HelloScene()
            else:
                self.__scenesExample[uid] = create_scene(self.__scenesExample[uid])
        self.__scenesNum[uid] = self.__scenesExample[uid].LAST_VALID_SCENE

        return self.__scenesExample[uid]

