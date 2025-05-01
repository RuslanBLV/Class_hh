from src.abstract_api import AbstractJobAPI
import requests
from typing import List, Dict


class HHAPI(AbstractJobAPI):
    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__headers = {
            "User-Agent": "Mozilla/5.0"
        }

    def _connect(self):
        """Подключение к API hh.ru (приватный метод)."""
        response = requests.get(self.__base_url, headers=self.__headers)
        if response.status_code != 200:
            raise ConnectionError(f"Не удалось подключиться к API, статус-код: {response.status_code}")
        return response.json()

    def get_vacancies(self, keyword: str, per_page: int = 20):
        """Получение вакансий по ключевому слову."""
        self._connect()  # Проверяем соединение перед отправкой запроса

        params = {
            'text': keyword,
            'per_page': per_page
        }

        response = requests.get(self.__base_url, headers=self.__headers, params=params)

        if response.status_code != 200:
            raise ConnectionError(f"Ошибка при получении данных, статус-код: {response.status_code}")

        data = response.json()

        # Сбор данных о вакансиях в формате списка словарей
        vacancies = data.get('items', [])

        return vacancies
