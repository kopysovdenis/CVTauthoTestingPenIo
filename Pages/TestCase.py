from selenium import webdriver
from datetime import datetime
import unittest

from selenium.common.exceptions import NoSuchElementException

from Pages.ConfigElements import createBottom, editBottom, formTitle, formLogin, formText, publishBottom, \
    updateBottom, loginBottom, formPassword


class PenIoTestCase(unittest.TestCase):



    def setUp(self, url = 'http://pen.io'):
        self.nowTime = datetime.now().strftime('%d-%m-%Y_%H-%M')
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def testCreatePage(self, idUser, password):
        driver = self.driver
        try:
            self.assertTrue(self.check_exists_by_xpath(createBottom))

            inputFormLogin = driver.find_element_by_xpath(formLogin)
            inputFormLogin.send_keys(idUser)

            pswd = driver.find_element_by_xpath(formPassword)
            pswd.send_keys(password)

            createSubmit = driver.find_element_by_xpath(createBottom)
            createSubmit.click()

            if self.check_exists_by_xpath(formTitle):
                print('testCreatePage: pass')
            else:
                print('testCreatePage: Error click Create Page bottom. fail')
        except:
            print('testCreatePage: fail')
        finally:
            print('testCreatePage: finish')

    def testEditingPage(self):
        driver = self.driver
        try:
            inputFieldTiele = driver.find_element_by_xpath(formTitle)
            inputFieldText = driver.find_element_by_xpath(formText)
            inputSubmit = driver.find_element_by_xpath(publishBottom)

            inputFieldTiele.send_keys('Title Hello')
            inputFieldText.send_keys('Text Bonjorne')
            inputSubmit.click()
            print('testEditingPage: pass')
        except:
            print('testEditingPage: fail')
        finally:
            print('testEditingPage: finish')

    def testUpdatePage(self, idUser, password):
        driver = self.driver
        driver.get('http://'+idUser+'.pen.io')
        try:
            self.assertTrue(self.check_exists_by_xpath(editBottom))

            editSubmit = driver.find_element_by_xpath(editBottom)
            editSubmit.click()

            if self.check_exists_by_xpath(loginBottom):
                pswd = driver.find_element_by_xpath(formPassword)
                pswd.send_keys(password)
                loginSubmit = driver.find_element_by_xpath(loginBottom)
                loginSubmit.click()

            self.assertTrue(self.check_exists_by_xpath(updateBottom))

            title = driver.find_element_by_xpath(formTitle)
            title.clear()
            title.send_keys('hello Mama)')

            text = driver.find_element_by_xpath(formText)
            text.clear()
            text.send_keys('hello Papa)')

            updateSubmit = driver.find_element_by_xpath(updateBottom)
            updateSubmit.click()
            print('testUpdatePage: pass')
        except:
            print('testUpdatePage: fail')
            # self.driver.close()
        finally:
            print('testUpdatePage: finish')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()