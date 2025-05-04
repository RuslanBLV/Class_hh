from typing import Dict, Any


class Vacancy:
    """ Класс для представления вакансии. """
    __slots__ = ('_title', '_salary', '_company', '_url')

    def __init__(self, title: str, salary: float, company: str, url: str):
        """ Инициализация объекта вакансии. """
        self._title = title
        self._salary = salary if salary is not None else 0
        self._company = company
        self._url = url

    def to_dict(self) -> Dict[str, Any]:
        """ Преобразование объекта вакансии в словарь. """
        return {
            'title': self._title,
            'salary': self._salary,
            'company': self._company,
            'url': self._url
        }

    @staticmethod
    def _validate_title(title: str) -> str:
        """ Валидация названия вакансии. """
        if not isinstance(title, str) or not title:
            raise ValueError("Название вакансии должно быть непустой строкой.")
        return title

    @staticmethod
    def _validate_salary(salary: float) -> float:
        """ Валидация зарплаты вакансии. """
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Зарплата должна быть неотрицательным числом.")
        return salary

    @staticmethod
    def _validate_company(company: str) -> str:
        """ Валидация названия компании."""
        if not isinstance(company, str) or not company:
            raise ValueError("Название компании должно быть непустой строкой.")
        return company

    @staticmethod
    def _validate_url(url: str) -> str:
        """ Валидация URL вакансии. """
        if not isinstance(url, str) or not url.startswith("http"):
            raise ValueError("URL должен быть корректной строкой и начинаться с 'http'.")
        return url

    def __lt__(self, other):
        """Сравнение по зарплате (меньше)."""
        return self._salary < other._salary

    def __le__(self, other):
        """Сравнение по зарплате (меньше или равно)."""
        return self._salary <= other._salary

    def __gt__(self, other):
        """Сравнение по зарплате (больше)."""
        return self._salary > other._salary

    def __ge__(self, other):
        """Сравнение по зарплате (больше или равно)."""
        return self._salary >= other._salary

    def __eq__(self, other):
        """Сравнение по зарплате (равно)."""
        return self._salary == other._salary

    def __ne__(self, other):
        """Сравнение по зарплате (не равно)."""
        return self._salary != other._salary

    def __repr__(self):
        """ Строковое представление объекта вакансии. """
        return f"{self._title} - {self._salary} руб. ({self._company})"

    @property
    def url(self):
        """ Возвращает URL вакансии. """
        return self._url

