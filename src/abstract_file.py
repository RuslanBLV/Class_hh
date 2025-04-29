from abc import ABC, abstractmethod
from typing import List


class AbstractFile(ABC):
    @abstractmethod
    def load_vacancies(self) -> list:
        """Загрузка вакансий из файла."""
        pass

    @abstractmethod
    def save_vacancy(self, vacancy) -> None:
        """Сохранение вакансии в файл."""
        pass

    @abstractmethod
    def delete_vacancy(self, title: str) -> None:
        """Удаление вакансии из файла."""
        pass
