from selenium import webdriver

browser = webdriver.Firefox()

# Użytkownik dowiaduje się o aplikacji "To-do-list" i wchodzi na stronę
browser.get('http://127.0.0.1:8000')

# Zwraca uwagę, że tytuł strony i nagłówek zawierają słowo Listy
assert "Listy" in browser.title

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

browser.quit()
