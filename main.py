from src.vacancy_class import Vacancy
from src.hh_class import HHRU
from src.json_file_class import JSONFile
from src.help import print_vacancies


def main():
    api = HHRU()
    file_manager = JSONFile()

    while True:
        print("\n1. Поиск вакансий")
        print("2. Получить вакансии")
        print("3. Удалить вакансию")
        print("4. Выход")

        choice = input("Выберите опцию: ")

        if choice == '1':
            query = input("Введите поисковый запрос: ")
            vacancies_data = api.get_vacancies(query)
            vacancies = [Vacancy(v['name'], v['alternate_url'], v.get('salary', None), v['snippet']['requirement']) for
                         v in vacancies_data]
            for vacancy in vacancies:
                file_manager.save_vacancy(vacancy)
            print(f"Найдено {len(vacancies)} вакансий.")

        elif choice == '2':
            vacancies = file_manager.load_vacancies()
            print_vacancies(vacancies)

        elif choice == '3':
            title = input("Введите название вакансии для удаления: ")
            file_manager.delete_vacancy(title)

        elif choice == '4':
            break


if __name__ == "__main__":
    main()
