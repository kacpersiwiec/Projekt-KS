#import bibliotek
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# wyswietlenie zawartości katalogu opinions_json
input_directory = "./opinions_json"
print(*os.listdir(input_directory))

# wczytanie identyfiaktora produktu< którego opinie będa analizowene
product_id = input("Podaj identyfikator produktu: ")

# wczytanie do ramki danych opinii o pojedynczym produkcie
opinions = pd.read_json(input_directory + "/" + product_id + ".json")
opinions = opinions.set_index("opinion_id")

# podstawowe statystyki
average_score = opinions.stars.mean().round(2)
pros = opinions.pros.count()
cons = opinions.cons.count()
stars = opinions.stars.value_counts().sort_index().reindex(
    list(np.arange(0, 5.5, 0.5)), fill_value=0)


print(
    f"Srednia ocena: {average_score}\nLiczba opinii z zaletami: {pros}\nLiczba opinii z wadami: {cons}\n{stars}")

# histogram częstości występowania poszczególnych ocen (gwiazdek)
recommendation = opinions.recommendation.value_counts()
fig, ax = plt.subplots()
stars.plot.bar(color="#f5c3c2")
plt.title("***Gwiazdki***")
plt.xlabel("liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.xticks(rotation=0)
# plt.show()
plt.savefig("figures_png/" + product_id+"_bar.png")
plt.close()


# wykres ile osób polaca a ile nie poleca
fig, ax = plt.subplots()
recommendation.plot.pie(label="", autopct="%1.1f%%",
                        colors=["#89cff0", "#f5c3c2"])
plt.title("REKOMENDACJA")
# plt.show()
plt.savefig("figures_png/" + product_id+"_bar.png")
plt.close()

opinions["purchased"] = opinions["purchase_date"].apply(
    lambda x: False if x == None else True)
stars_purchased = pd.crosstab(opinions["stars"], opinions["purchased"])
