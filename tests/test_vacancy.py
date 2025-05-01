# -*- coding: utf-8 -*-
import unittest
from src.vacancy_class import Vacancy


class TestVacancy(unittest.TestCase):
    def test_vacancy_initialization_with_valid_salary(self):
        vacancy = Vacancy("Вакансия 1", 50000, "Компания A", "http://example.com")
        self.assertEqual(vacancy._title, "Вакансия 1")
        self.assertEqual(vacancy._salary, 50000)
        self.assertEqual(vacancy._company, "Компания A")
        self.assertEqual(vacancy.url, "http://example.com")

    def test_vacancy_initialization_with_none_salary(self):
        vacancy = Vacancy("Вакансия 2", None, "Компания B", "http://example.com")
        self.assertEqual(vacancy._title, "Вакансия 2")
        self.assertEqual(vacancy._salary, 0)  # Проверяем, что зарплата по умолчанию 0
        self.assertEqual(vacancy._company, "Компания B")
        self.assertEqual(vacancy.url, "http://example.com")

    def test_vacancy_string_representation(self):
        vacancy = Vacancy("Вакансия 3", 70000, "Компания C", "http://example.com")
        self.assertEqual(str(vacancy), "Вакансия 3 - 70000 руб. (Компания C)")

    def test_vacancy_initialization_with_zero_salary(self):
        vacancy = Vacancy("Вакансия 4", 0, "Компания D", "http://example.com")
        self.assertEqual(vacancy._salary, 0)  # Проверяем, что зарплата остается 0