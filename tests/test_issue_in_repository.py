import pytest
import allure
from allure_commons.types import Severity
from selene import browser, have, be

@allure.epic('Знакомство с функционалом Allure')
@allure.feature('Тесты без именования шагов')
@allure.severity(Severity.TRIVIAL)
@allure.label('owner', 'Voronova K.')
@allure.description('Этот тест создан для демонстрации отчета без шагов')
@allure.title('Поиск задачи по номеру, без шагов Allure')
def test_issue_in_repository_without_steps():
    browser.open('https://github.com/')

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type('eroshenkoam/allure-example').press_enter()
    browser.element('[href="/eroshenkoam/allure-example"]').click()
    browser.element("#issues-tab").click()

    browser.all('.opened-by').element_by(have.text('#81')).should(be.visible)

@allure.epic('Знакомство с функционалом Allure')
@allure.feature('Тесты с именованием шагов')
@allure.story('Тесты с шагами внутри теста')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Voronova K.')
@allure.description('Этот тест создан для демонстрации отчета с шагами, описанными внутри теста')
@allure.title('Поиск задачи по номеру, с шагами Allure внутри теста')
def test_issue_in_repository_with_steps_inside_test():
    with allure.step('Открываем github.com'):
        browser.open('https://github.com/')

    with allure.step('Кликаем по строке поиска'):
        browser.element('.header-search-input').click()
    with allure.step('Ищем нужный репозиторий'):
        browser.element('.header-search-input').type('eroshenkoam/allure-example').press_enter()
    with allure.step('Переходим к репозиторию'):
        browser.element('[href="/eroshenkoam/allure-example"]').click()
    with allure.step('Кликаем по Issues'):
        browser.element("#issues-tab").click()

    with allure.step('Проверяем наличие задачи'):
        browser.all('.opened-by').element_by(have.text('#81')).should(be.visible)

@allure.epic('Знакомство с функционалом Allure')
@allure.feature('Тесты с именованием шагов')
@allure.story('Тесты с шагами, описанными в декораторах')
@allure.label('owner', 'Voronova K.')
@allure.description('Этот тест создан для демонстрации отчета с шагами, описанными в декораторах')
@allure.title('Поиск задачи по номеру, с шагами Allure в декораторах')
def test_issue_in_repository_with_steps_with_decorator():
    open_github()

    open_repository('/eroshenkoam/allure-example')
    open_issues()

    check_task_existence('#81')

@allure.step('Открываем github.com')
def open_github():
    browser.open('https://github.com/')

@allure.step('Находим и открываем репозиторий {repo}')
def open_repository(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type(repo).press_enter()
    browser.element(f'[href="{repo}"]').click()

@allure.step('Кликаем по Issues')
def open_issues():
    browser.element("#issues-tab").click()

@allure.step('Проверяем наличие задачи {task}')
def check_task_existence(task):
    browser.all('.opened-by').element_by(have.text(task)).should(be.visible)
