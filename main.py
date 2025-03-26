from bs4 import BeautifulSoup
from collections import Counter

with open(r"eksta_pensja_html2.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")
draw_items = soup.find_all("div", class_="result-item")
all_draws = []

for draw_item in draw_items:
    draw_number_tag = draw_item.find("p", class_="result-item__number")
    if draw_number_tag:
        draw_number = draw_number_tag.get_text(strip=True)
    else:
        continue

    balls_box = draw_item.find("div", class_="result-item__balls-box")
    if balls_box:
        numbers = [num.get_text(strip=True) for num in balls_box.find_all("div", class_="scoreline-item")]
    else:
        numbers = []

    all_draws.append({
        "Numer losowania": draw_number,
        "Liczby": numbers
    })

ekstra_pensja_liczby = []
ekstra_pensja_liczba_ekstra = []
ekstra_premia_liczby = []
ekstra_premia_liczba_ekstra = []
for i, j in enumerate(all_draws):
    if i % 2 == 1:
        ekstra_premia_liczby.append(j['Liczby'][:5])
        ekstra_premia_liczba_ekstra.append(j['Liczby'][5:6])

    else:
        ekstra_pensja_liczby.append(j['Liczby'][:5])
        ekstra_pensja_liczba_ekstra.append(j['Liczby'][5:6])


sum_ekstra_pensja_liczby = [int(num) for sublist in ekstra_pensja_liczby for num in sublist]
sum_ekstra_pensja_liczba_ekstra = [int(num) for sublist in ekstra_pensja_liczba_ekstra for num in sublist]
sum_ekstra_premia_liczby = [int(num) for sublist in ekstra_premia_liczby for num in sublist]
sum_ekstra_premia_liczba_ekstra = [int(num) for sublist in ekstra_premia_liczba_ekstra for num in sublist]


def percentage_sorted(lista):
    counter = Counter(lista)
    total_count = len(lista)
    percentage_result = {num: round((count / total_count) * 100, 3) for num, count in counter.items()}
    sorted_percentage_result = dict(sorted(percentage_result.items(), key=lambda item: item[1], reverse=True))
    print(sorted_percentage_result)

percentage_sorted(sum_ekstra_pensja_liczby)
percentage_sorted(sum_ekstra_pensja_liczba_ekstra)
percentage_sorted(sum_ekstra_premia_liczby)
percentage_sorted(sum_ekstra_premia_liczba_ekstra)
