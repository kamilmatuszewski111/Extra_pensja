from bs4 import BeautifulSoup
from collections import Counter


def load_html(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def extract_draws(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    draws = []

    for draw_item in soup.find_all("div", class_="result-item"):
        draw_number = draw_item.find("p", class_="result-item__number")
        numbers = [num.get_text(strip=True) for num in draw_item.find_all("div", class_="scoreline-item")]

        if draw_number and numbers:
            draws.append({"Numer losowania": draw_number.get_text(strip=True), "Liczby": numbers})

    return draws


def split_draws(draws):
    ekstra_pensja = [(d["Liczby"][:5], d["Liczby"][5:6]) for i, d in enumerate(draws) if i % 2 == 0]
    ekstra_premia = [(d["Liczby"][:5], d["Liczby"][5:6]) for i, d in enumerate(draws) if i % 2 == 1]

    return {
        "ekstra_pensja_liczby": sum([x[0] for x in ekstra_pensja], []),
        "ekstra_pensja_liczba_ekstra": sum([x[1] for x in ekstra_pensja], []),
        "ekstra_premia_liczby": sum([x[0] for x in ekstra_premia], []),
        "ekstra_premia_liczba_ekstra": sum([x[1] for x in ekstra_premia], [])
    }


def percentage_sorted(numbers):
    counter = Counter(map(int, numbers))
    total = len(numbers)
    return dict(
        sorted({num: round((count / total) * 100, 3) for num, count in counter.items()}.items(), key=lambda x: x[1],
               reverse=True))


html_content = load_html("eksta_pensja_html2.html")
all_draws = extract_draws(html_content)
split_data = split_draws(all_draws)

for category, numbers in split_data.items():
    print(f"{category}: {percentage_sorted(numbers)}")
