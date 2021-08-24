import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self):
        # Użytkownik dowiaduje się o aplikacji "To-do-list" i wchodzi na stronę
        self.browser.get(self.live_server_url)

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

        # Po naciśnięciu klawisza Enter strona została uaktualniona i wyświetla 
        # '1: Zrobić zakupy na obiad'
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)
        self.check_for_row_in_list_table('1: Zrobić zakupy na obiad')

        # Na stronie nadal znajduje się pole tekstowe zachęcające do podania 
        # kolejnego zadania. Użytkownik wpisuje więc 'Ugotować z zakupionych
        # produktów obiad'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Ugotować z zakupionych produktów obiad')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        # Strona ponownie została zaktualizowana i wyświetla już dwa elementy z
        # listy do zrobienia
        self.check_for_row_in_list_table('1: Zrobić zakupy na obiad')
        self.check_for_row_in_list_table(
            '2: Ugotować z zakupionych produktów obiad'
            )
        
        # Użytkownik był ciekaw czy witryna zapamięta jego listę. Zwraca uwagę 
        # na unikatowy adres URL z tekstem
        self.fail('Zakończenie testu!')

        # Przechodzi pod podany adres i widzi swoją listę

        # Użytkownik kończy przygodę z listą

        # browser.quit()
