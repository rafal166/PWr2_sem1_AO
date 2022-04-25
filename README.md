# PWr - Informatyczne Systemy Automatyki 
# Algorytmy Optymalizacji

## Generator pozycji
Prosty program umożliwia wygenerowanie losowych pozycji. Przyjęto że pozycje generowane będą w okręgu, którego środek znajduję się we wcześniej zdefiniowanych współrzędnych, które odpowiadają położeniu centrum Wrocławia. Okrąg ma promień równy 0.8 stopnia co w przybliżeniu pokrywa całą powierzchnię wrocławia.

### Uruchomienie generatora
Program uruchamiany jest bez żadnych argumentów startowych w katalogu w którym się znajduje.
```
py generator_pozycji/index.py 
```
### Zapis danych
Dane zapisywane są w katalogu ``data`` w pliku o zdefiniowanej przez użytkownika nazwie podawanej po uruchomieniu programu. Dane zapisywane są w formacie CSV rozdzielonym ``;``.

---