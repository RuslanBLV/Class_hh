from abc import ABC, abstractmethod


class AbstractJobAPI(ABC):
    """ Абстрактный класс для работы с API вакансий. """
    @abstractmethod
    def _connect(self):
        """ Подключение к API (приватный метод). """
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, per_page: int = 20):
        """ Получение вакансий по ключевому слову. """
        pass
