from src.json_file_class import JsonVacancyStorage
import requests
from src.vacancy_class import Vacancy
from typing import List, Dict, Any


def search_vacancies(query: str) -> List[Dict[str, Any]]:
    """ Ищет вакансии по заданному запросу на сайте hh.ru. """
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": query,
        "area": 113,  # ID области, например, Москва
        "per_page": 20  # Количество вакансий на странице
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        print(f"Ошибка при получении данных: {response.status_code}")
        return []


def user_interaction(storage: JsonVacancyStorage) -> None:
    """ Обрабатывает взаимодействие с пользователем для управления вакансиями. """
    while True:
        print("\nДобро пожаловать в систему управления вакансиями!")
        print("Выберите действие:")
        print("1. Ввести поисковый запрос для запроса вакансий из hh.ru")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии с ключевым словом в описании")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            search_query = input("Введите поисковый запрос: ")
            vacancies_data = search_vacancies(search_query)

            if vacancies_data:
                for vacancy in vacancies_data:
                    # Создаем объект Vacancy и добавляем его в хранилище
                    new_vacancy = Vacancy(
                        title=vacancy['name'],
                        company=vacancy['employer']['name'],
                        salary=vacancy['salary']['from'] if vacancy['salary'] else None,
                        url=vacancy['alternate_url']
                    )
                    storage.add_vacancy(new_vacancy)
                print(f"Запрос на вакансии по запросу '{search_query}' выполнен и сохранен.")
            else:
                print("Вакансии не найдены.")

        elif choice == '2':
            try:
                n = int(input("Введите количество вакансий для получения по зарплате: "))
                if n <= 0:
                    print("Количество должно быть положительным числом.")
                    continue

                # Получение всех вакансий и сортировка по зарплате
                vacancies = storage.get_vacancies({})
                top_vacancies = sorted(vacancies, key=lambda v: (v._salary is None, v._salary), reverse=True)[:n]

                if top_vacancies:
                    print(f"Топ {n} вакансий по зарплате:")
                    for vacancy in top_vacancies:
                        print(
                            f"- {vacancy._title} от {vacancy._company}: {vacancy._salary} руб. (Ссылка: {vacancy._url})")
                else:
                    print("Вакансии не найдены.")

            except ValueError:
                print("Пожалуйста, введите корректное число.")

        elif choice == '3':
            keyword = input("Введите ключевое слово для поиска в описании: ")
            vacancies = storage.get_vacancies({})
            filtered_vacancies = [v for v in vacancies if
                                  keyword.lower() in v._title.lower() or keyword.lower() in v._company.lower()]

            if filtered_vacancies:
                print(f"Вакансии с ключевым словом '{keyword}':")
                for vacancy in filtered_vacancies:
                    print(f"- {vacancy._title} от {vacancy._company}: {vacancy._salary} руб. (Ссылка: {vacancy._url})")
            else:
                print("Вакансии не найдены.")

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите действие от 1 до 4.")
