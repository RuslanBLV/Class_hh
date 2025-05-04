from abc import ABC, abstractmethod
from typing import List, Dict, Any
from src.vacancy_class import Vacancy


class VacancyStorage(ABC):
    """ Абстрактный класс для хранения вакансий. """
    def __init__(self, filename: str = "vacancies.json"):
        """ Инициализация хранилища вакансий. """
        self._filename = filename

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """ Добавление вакансии в хранилище. """
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Dict[str, Any]) -> List[Vacancy]:
        """ Получение списка вакансий по заданным критериям. """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """ Удаление вакансии из хранилища. """
        pass

    @abstractmethod
    def clear_storage(self) -> None:
        """ Очистка хранилища от всех вакансий. """
        pass
