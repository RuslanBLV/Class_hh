from abc import ABC, abstractmethod
from typing import List, Dict


class AbstractAPI(ABC):
    @abstractmethod
    def connect(self):
        """Подключение к API."""
        pass

    @abstractmethod
    def get_vacancies(self, query: str) -> list:
        """Получение вакансий по запросу."""
        pass
