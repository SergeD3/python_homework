# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group


class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_contact(wd)
        self.fill_contact_form(wd, Group(middle_name="middle name 1", first_name="name 1", last_name="last name 1", user_nick="nick 1", user_title="title 1", user_company="wrum",
                               user_adress="lazer 5, Moscow", user_home="784763587643", user_mob="746358746357", user_email="weuyrt@iwer.ri", user_bday="17", user_bmonth="October",
                               user_byear="1980", user_group="new group2", user_addr2="lazer 5, Russian Federation", user_phone2="rgegregreg", user_note="notes from user"))
        self.contact_lv(wd)
        self.logout(wd)

    def logout(self, wd):
        # выпиливаемся из системы
        wd.find_element_by_link_text("Logout").click()

    def contact_lv(self, wd):
        # переходим на форму списка контактов - убеждаемся, что контакт создался
        wd.find_element_by_link_text("home").click()

    def fill_contact_form(self, wd, group):
        # заполняем поля
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(group.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(group.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(group.user_nick)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(group.user_title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(group.user_company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(group.user_adress)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(group.user_home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(group.user_mob)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(group.user_email)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(group.user_bday)
        wd.find_element_by_xpath("//option[@value='17']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(group.user_bmonth)
        wd.find_element_by_xpath("//option[@value='October']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(group.user_byear)
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(group.user_group)
        wd.find_element_by_xpath("(//option[@value='10'])[3]").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(group.user_addr2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(group.user_phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(group.user_note)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_add_contact(self, wd):
        # переходим в раздел добавления контакта
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        # представляемся системе
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_homepage(self, wd):
        # открываем сайт
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
