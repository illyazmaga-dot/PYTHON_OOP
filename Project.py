import requests
from bs4 import BeautifulSoup


class SiteDatabase:
    def __init__(self):
        self.sites = []
    def add_site(self, url):
        if url not in self.sites:
            self.sites.append(url)
    def remove_site(self, url):
        if url in self.sites:
            self.sites.remove(url)
    def clear_all(self):
        self.sites.clear()
    def get_sites(self):
        return self.sites


class WebParser:
    def search_on_site(self, url, phrase):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            for tag in soup(["script", "style"]):
                tag.decompose()
            text = soup.get_text().lower()
            return text.count(phrase.lower())
        except Exception:
            return 0


class UserInterface:
    def __init__(self, database, parser):
        self.database = database
        self.parser = parser
        self.last_results = {}
    def show_menu(self):
        print("\n1 — Додати сайт")
        print("2 — Видалити сайт")
        print("3 — Очистити базу сайтів")
        print("4 — Пошук")
        print("5 — Останні результати")
        print("0 — Вихід")
    def search(self):
        phrase = input("Введіть слово або фразу: ")
        self.last_results.clear()
        for site in self.database.get_sites():
            count = self.parser.search_on_site(site, phrase)
            self.last_results[site] = count
            print(f"{phrase} — {count} входжень на {site}")


def run():
    db = SiteDatabase()
    parser = WebParser()
    ui = UserInterface(db, parser)
    while True:
        ui.show_menu()
        choice = input("Ваш вибір: ")
        if choice == "1":
            db.add_site(input("URL: "))
        elif choice == "2":
            db.remove_site(input("URL: "))
        elif choice == "3":
            db.clear_all()
        elif choice == "4":
            ui.search()
        elif choice == "5":
            print(ui.last_results)
        elif choice == "0":
            break


if __name__ == "__main__":
    run()