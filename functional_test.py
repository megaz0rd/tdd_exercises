from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # Użytkownik dowiaduje się o aplikacji "To-do-list" i wchodzi na stronę
        self.browser.get('http://127.0.0.1:8000')

        # Zwraca uwagę, że tytuł strony i nagłówek zawierają słowo Listy
        self.assertIn("Listy", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Listy", header_text)


        # Od razu zostaje zachęcony, aby wpisać rzeczy do zrobienia
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Wpisz rzeczy do zrobienia'
            )

        # W polu tekstowym wpisał "Zrobić zakupy na obiad"
        inputbox.send_keys('Zrobić zakupy na obiad')

        # Po naciśnieęciu klawisza Enter strona została uaktualniona i wyświetla 
        # '1: Zrobić zakupy na obiad'
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Zrobić zakupy na obiad' for row in rows),
            "Nowy element nie znajduje się w tabeli"
        )

        # Na stronie nadal znajduje się pole tekstowe zachęcające do podania 
        # kolejnego zadania. Użytkownik wpisuje więc 'Ugotować z zakupionych
        # produktów obiad'
        self.fail('Zakończenie testu!')

# Strona ponownie została zaktualizowana i wyświetla już dwa elementy z listy 
# do zrobienia

# Użytkownik był ciekaw czy witryna zapamięta jego listę. Zwraca uwagę na 
# unikatowy adres URL z tekstem

# Przechodzi pod podany adres i widzi swoją listę

# Użytkownik kończy przygodę z listą

# browser.quit()

if __name__ == '__main__':
    unittest.main()
