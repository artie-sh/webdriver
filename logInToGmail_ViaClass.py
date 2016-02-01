import unittest
from selenium import webdriver
import library.paths as paths
from library.report import Report

class logInToGmail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/artie-sh/Documents/webdriver/chromedriver')

    def test_search_in_python_org(self):

        driver = self.driver
        driver.maximize_window()
        report = Report()

        driver.get('http://www.google.pl')
        gmail = driver.find_element_by_link_text('Gmail')
        assert gmail
        report.add_screen()

        gmail.click()
        email_input = driver.find_element_by_id('Email')
        next_button = driver.find_element_by_id('next')
        assert email_input and next_button
        email_input.send_keys(paths.username)
        driver.implicitly_wait(1000)
        report.add_screen()
        next_button.click()

        passwd = driver.find_element_by_id('Passwd')
        sign_in = driver.find_element_by_id('signIn')
        assert passwd and sign_in
        passwd.send_keys(paths.password)
        driver.implicitly_wait(1000)
        report.add_screen()
        sign_in.click()

        assert 'Artie' in driver.page_source
        driver.implicitly_wait(1000)
        report.add_screen()
        report.close()


#    def tearDown(self):
 #       self.driver.close()

if __name__ == "__main__":
    unittest.main()