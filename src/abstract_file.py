from abc import ABC, abstractmethod
from typing import List, Dict, Any
from src.vacancy_class import Vacancy


class VacancyStorage(ABC):
    def __init__(self, filename: str = "vacancies.json"):
        self._filename = filename

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Dict[str, Any]) -> List[Vacancy]:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def clear_storage(self) -> None:
        pass
