from src.abstract_file import AbstractFile
import json
from src.vacancy_class import Vacancy


class JSONFile(AbstractFile):
    def __init__(self, filename='vacancies.json'):
        self._filename = filename

    def load_vacancies(self) -> list:
        try:
            with open(self._filename, 'r', encoding='utf-8') as f:
                vacancies_data = json.load(f)
                return [Vacancy(**data) for data in vacancies_data]
        except FileNotFoundError:
            return []

    def save_vacancy(self, vacancy) -> None:
        vacancies = self.load_vacancies()
        if vacancy not in vacancies:  # Проверка на дубликаты
            vacancies.append(vacancy)
            with open(self._filename, 'w', encoding='utf-8') as f:
                json.dump([v.__dict__ for v in vacancies], f, ensure_ascii=False)

    def delete_vacancy(self, title: str) -> None:
        vacancies = self.load_vacancies()
        vacancies = list(filter(lambda v: v.title != title, vacancies))
        with open(self._filename, 'w', encoding='utf-8') as f:
            json.dump([v.__dict__ for v in vacancies], f, ensure_ascii=False)
