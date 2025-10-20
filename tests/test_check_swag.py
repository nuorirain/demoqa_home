import pytest
from pages.swag_labs import SwagLabs


def test_icon_presence(driver):
    page = SwagLabs(driver) 
    page.visit()             
    assert page.exist_icon(), "Логотип не найден" 


def test_username_field_presence(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_username_field(), "Поле имени пользователя не найдено"


def test_password_field_presence(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_password_field(), "Поле пароля не найдено"
