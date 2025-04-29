class Vacancy:
    __slots__ = ('_title', '_url', '_salary', '_description')

    def __init__(self, title: str, url: str, salary: float, description: str):
        self._title = title
        self._url = url
        self._salary = self._validate_salary(salary)
        self._description = description

    @staticmethod
    def _validate_salary(salary):
        return salary

    def __lt__(self, other):
        return (self._salary or 0) < (other._salary or 0)

    def __str__(self):
        return f"Вакансия: {self._title}, Зарплата: {self._salary}, Ссылка: {self._url}, Описание: {self._description}"
