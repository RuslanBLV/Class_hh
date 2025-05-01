from src.json_file_class import JsonVacancyStorage
from src.help import user_interaction

if __name__ == "__main__":
    storage = JsonVacancyStorage()
    user_interaction(storage)
