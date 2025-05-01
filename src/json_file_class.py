from src.abstract_file import VacancyStorage
import json
from src.vacancy_class import Vacancy
from typing import List, Dict, Any


class JsonVacancyStorage(VacancyStorage):
    def __init__(self, filename: str = "vacancies.json"):
        super().__init__(filename)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self._load_vacancies()
        if not any(v['url'] == vacancy._url for v in vacancies):  # Проверка на дубликаты по URL
            vacancies.append(vacancy.to_dict())
            with open(self._filename, 'w', encoding='utf-8') as f:
                json.dump(vacancies, f, indent=4, ensure_ascii=False)

    def get_vacancies(self, criteria: Dict[str, Any]) -> List[Vacancy]:
        vacancies = self._load_vacancies()
        filtered_vacancies = [
            Vacancy(**v) for v in vacancies if all(v[k] == v_criteria for k, v_criteria in criteria.items() if k in v)
        ]
        return filtered_vacancies

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self._load_vacancies()
        vacancies = [v for v in vacancies if v['url'] != vacancy._url]  # Удаление по URL
        with open(self._filename, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, indent=4)

    def clear_storage(self) -> None:
        with open(self._filename, 'w', encoding='utf-8') as f:
            json.dump([], f)  # Очистка файла

    def _load_vacancies(self) -> List[Dict[str, Any]]:
        try:
            with open(self._filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Возврат пустого списка, если файл не найден или пуст
