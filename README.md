# Projekt-KS
## etap 1- analiza struktury [Ceneo.pl](https://www.ceneo.pl/)
|Składowa                |Selektor                                         |Nazwa zmiennej|
|------------------------|-------------------------------------------------|--------------|
|opinia                  |li.js_product-review                             |              |
|identyfikator opinii    |["data-entry-id"]                                |              |
|autor opinii            |div.reviewer-name-line                           |              |
|rekomendacja            |div.product-review-summary > em                  |              |
|ocena                   |span.review-score-count                          |              |
|treść opinii            |p.product-review-body                            |              |
|lista wad               |div.cons-cell > ul                               |              |
|lista zalet             |div.pros-cell > ul                               |              |
|przydatne               |button.vote-yes > span                           |              |
|nieprzydatne            |button.vote-no > span                            |              |
|data wystawienia opinii |span.review-time > time:first-child["datetime"]  |              |
|data zakupu             |span.review-time > time:nth-child(2)["datetime"] |              |

## etap 2- pobranie składowych pojedynczej opinii
-pobranie kodu jednej strony z opiniami o konkretnym produkcie
-wyciągniecie z kodu strony fragmentów odpowiadajacych poszczególnym opiniom
-zapisanie do pojedynczych zmiennych opinii wartosci poszczegolnych skladowych opinii