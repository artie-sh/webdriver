import unittest
from selenium import webdriver
import library

class logInToGmail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/artie-sh/Documents/webdriver/chromedriver')

    def test_search_in_python_org(self):

        driver = self.driver
        driver.maximize_window()
        report = library.get_report()

        driver.get('http://www.google.pl')
        gmail = driver.find_element_by_link_text('Gmail')
        assert gmail
        library.add_screen(report, library.take_screen())

        gmail.click()
        email_input = driver.find_element_by_id('Email')
        next_button = driver.find_element_by_id('next')
        assert email_input and next_button
        email_input.send_keys(library.username)
        driver.implicitly_wait(1000)
        library.add_screen(report, library.take_screen())
        next_button.click()

        passwd = driver.find_element_by_id('Passwd')
        sign_in = driver.find_element_by_id('signIn')
        assert passwd and sign_in
        passwd.send_keys(library.password)
        driver.implicitly_wait(1000)
        library.add_screen(report, library.take_screen())
        sign_in.click()

        assert 'Artie' in driver.page_source
        driver.implicitly_wait(1000)
        library.add_screen(report, library.take_screen())
        library.close_report(report)


#    def tearDown(self):
 #       self.driver.close()

if __name__ == "__main__":
    unittest.main()