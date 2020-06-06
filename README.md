# Projekt-KS

## etap 1- analiza struktury [Ceneo.pl](https://www.ceneo.pl/)
|Składowa                |Selektor                                         |Nazwa zmiennej|
|------------------------|-------------------------------------------------|--------------|
|opinia                  |div.js_product-review                             |opinion       |
|identyfikator opinii    |["data-entry-id"]                                |opinion_id    |
|autor opinii            |div.reviewer-name-line                           |author        |
|rekomendacja            |div.product-review-summary > em                  |recommendation|
|ocena                   |span.review-score-count                          |stars         |
|treść opinii            |p.product-review-body                            |content       |
|lista wad               |div.cons-cell > ul                               |cons          |
|lista zalet             |div.pros-cell > ul                               |pros          |
|przydatne               |button.vote-yes > span                           |useful        |
|nieprzydatne            |button.vote-no > span                            |useless       |
|data wystawienia opinii |span.review-time > time:first-child["datetime"]  |opinion_date  |
|data zakupu             |span.review-time > time:nth-child(2)["datetime"] |purchase_date |

## etap 2- pobranie składowych pojedynczej opinii
-pobranie kodu jednej strony z opiniami o konkretnym produkcie
-wyciągniecie z kodu strony fragmentów odpowiadajacych poszczególnym opiniom
-zapisanie do pojedynczych zmiennych opinii wartosci poszczegolnych skladowych opinii

### etap 3- pobranie wszystkich opinii o pojedynczym produkcie
-zapisanie do struktury opinii
-przechodzenie po kolejnych stronach z opiniamii
-zapis wszystkich opinii o pojedynczym produkcie do pliku

## etap 4 -
-transformacja i wyczyszczenie danych 
-refaktoring kodu
-parametryzacja 

## Etap 5 (Pandas, Matplotlib)
-wczytywanie opinii do ramki 
-policzenie podstawowych statystyk
-narysownie wykresów funkcji

## Etap 6 interfejs webowy dla scrapera (Flask)
>   /Projekt KS
>>        /run.py  
>>        /config.py  
>>        /app  
>>>            /__init__.py
>>>            /views.py  
>>>            /models.py  
>>>            /static/  
>>>>                /main.css
>>>            /templates/  
>>>>                /layout.html
>>>>                /extract.html
>>>        /requirements.txt  
>>>        /.venv
