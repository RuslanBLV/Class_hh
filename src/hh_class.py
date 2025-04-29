from src.abstract_api import AbstractAPI
import requests
from typing import List, Dict


class HHRU(AbstractAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        self._session = requests.Session()

    def connect(self):
        """Метод подключения к API hh.ru."""
        response = self._session.get(self.BASE_URL)
        if response.status_code != 200:
            raise ConnectionError(f"Ошибка подключения: {response.status_code}")

    def get_vacancies(self, query: str) -> list:
        """Получение вакансий по ключевому слову."""
        params = {'text': query, 'per_page': 100}
        self.connect()  # Подключение перед запросом
        response = self._session.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            return response.json().get('items', [])
        else:
            raise Exception(f"Ошибка получения данных: {response.status_code}")
