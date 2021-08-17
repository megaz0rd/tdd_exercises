from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # Użytkownik dowiaduje się o aplikacji "To-do-list" i wchodzi na stronę
        self.browser.get('http://127.0.0.1:8000')
        self.browser.implicitly_wait(3)

        # Zwraca uwagę, że tytuł strony i nagłówek zawierają słowo Listy
        self.assertIn("Listy", self.browser.title)
        self.fail('Zakończenie testu!')

# Od razu zostaje zachęcony, aby wpisać rzeczy do zrobienia

# W polu tekstowym wpisał "Zrobić zakupy na obiad"

# Po naciśnieęciu klawisza Enter strona została uaktualniona i wyświetla 
# '1: Zrobić zakupy na obiad'

# Na stronie nadal znajduje się pole tekstowe zachęcające do podania kolejnego 
# zadania. Użytkownik wpisuje więc 'Ugotować z zakupionych produktów obiad'

# Strona ponownie została zaktualizowana i wyświetla już dwa elementy z listy 
# do zrobienia

# Użytkownik był ciekaw czy witryna zapamięta jego listę. Zwraca uwagę na 
# unikatowy adres URL z tekstem

# Przechodzi pod podany adres i widzi swoją listę

# Użytkownik kończy przygodę z listą

# browser.quit()

if __name__ == '__main__':
    unittest.main()
