from selenium import webdriver

browser = webdriver.Firefox()

# Użytkownik dowiaduje się o aplikacji "To-do-list" i wchodzi na stronę
browser.get('http://127.0.0.1:8000')

# Zwraca uwagę, że tytuł strony i nagłówek zawierają słowo Listy
assert "Listy" in browser.title

# Od razu zostaje zachęcony, aby wpisać rzeczy do zrobioenia

# W polu tekstowym wpisał "Zrobić zakupy"

# Po naciśnieęciu klawisza Enter strona została uaktualniona i wyświetla 
# '1: Zrobić zakupy"