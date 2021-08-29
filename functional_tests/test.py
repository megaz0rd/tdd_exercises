import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(StaticLiveServerTestCase):

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
        self.assertIn("Utwórz", header_text)

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
        time.sleep(1)

        user_list_url = self.browser.current_url
        self.assertRegex(user_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Zrobić zakupy na obiad')

        # Na stronie nadal znajduje się pole tekstowe zachęcające do podania 
        # kolejnego zadania. Użytkownik wpisuje więc 'Ugotować z zakupionych
        # produktów obiad'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Ugotować z zakupionych produktów obiad')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Strona ponownie została zaktualizowana i wyświetla już dwa elementy z
        # listy do zrobienia
        self.check_for_row_in_list_table('1: Zrobić zakupy na obiad')
        self.check_for_row_in_list_table(
            '2: Ugotować z zakupionych produktów obiad'
            )
        
        # Nowy użytkownij zaczyna korzystać z witryny

        ## Używamy nowej sesji przeglądarki, aby mieć pewność, że żadne
        ## informacje dotyczące poprzednego użytkownika nie zostaną ujawnione
        ## np. przez cookies
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Nowy użytkownik odwiedza stronę główną
        # Nie ma tam żadnych śladów list innego użytkownika
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Zrobić zakupy na obiad', page_text)
        self.assertNotIn('Posprzątać pokój', page_text)

        # Nowy użytkownik tworzy listę, wprowadzając nowy element.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Zrobić pranie')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Nowy użytkownik otrzymuje unikatowy adres URL do listy
        newuser_list_url = self.browser.current_url
        self.assertRegex(newuser_list_url, '/lists/.+')
        self.assertNotEqual(newuser_list_url, user_list_url)

        # Ponownie brak jakiegokolwiek śladu po liście poprzedniego użytkownika
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Zrobić zakupy na obiad', page_text)
        self.assertIn('Zrobić pranie', page_text)

        # Obaj użytkownicy kończą pracę
        
    def test_layout_and_styling(self):
        # Użytkownik przeszedl na stornę główną
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # Zauważa elegancko wyśrodkowane pole tekstowe
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

        # Po utworzeniu nowej listy pole tekstowe pozostaje wyśrodkowane
        inputbox.send_keys('testing\n')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )