# PWr - Informatyczne Systemy Automatyki 
# Algorytmy Optymalizacji

## Generator pozycji
Prosty program umożliwia wygenerowanie losowych pozycji. Przyjęto że pozycje generowane będą na prostokącie, którego lewa dolna krawędz znajduję się we wcześniej zdefiniowanych współrzędnych. Dodatkowo określamy długości boków naszego prostokąta. Przyjęte współrzędne wraz z długościami boków w przybliżeniu pokrywają powierzchnię centrum Wrocławia.

### Uruchomienie generatora
Program uruchamiany jest bez żadnych argumentów startowych w katalogu w którym się znajduje.
```
py generator_pozycji/index.py 
```
### Zapis danych
Dane zapisywane są w katalogu ``data`` w pliku o zdefiniowanej przez użytkownika nazwie podawanej po uruchomieniu programu. Dane zapisywane są w formacie CSV rozdzielonym ``;``.

---
### Algorytm optymalizacji
Program wypisuje w konsoli wyliczone współrzędne paczkomatów dla każdego regionu z osobna oraz maksymalne odległości paczkomatów od klientów. Dodatkowo dane zostają przedstawione na mapie, która obejmuje wcześniej zdefioniowany obszar.

### Uruchomienie algorytmu optymalizacji
Program uruchamiany jest bez żadnych argumentów startowych w katalogu w którym się znajduje.
```
py algorytm.py 
```
W pierwszej kolejności zostaniemy poproszeni o zdefiniowanie ilości paczkomatów, które chcemy rozdzielić na wcześniej zdefiniowanym obszarze. Następnie musimy podać nazwę pliku, w którym są zapisane dane naszych klientów.