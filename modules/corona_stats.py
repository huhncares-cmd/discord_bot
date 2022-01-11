import requests
from bs4 import BeautifulSoup as bs

def get_data():
    URL = "https://www.worldometers.info/coronavirus/#countries"

    soup = bs(requests.get(URL).content, "html.parser")

    table = soup.find("table", id="main_table_countries_today")
    table_data = table.tbody.find_all("tr")

    dictionary = {}

    for i in range(len(table_data)):
        row = table_data[i]
        cols = row.find_all("td")
        country = cols[1].text.strip()
        total_cases = cols[2].text.strip()
        new_cases = cols[3].text.strip()
        total_deaths = cols[4].text.strip()
        new_deaths = cols[5].text.strip()
        total_recovered = cols[6].text.strip()
        new_recovered = cols[7].text.strip()
        active_cases = cols[8].text.strip()
        critical_cases = cols[9].text.strip()
        dictionary[country] = [active_cases, critical_cases, total_cases, new_cases, total_deaths, new_deaths, total_recovered, new_recovered]

    return dictionary

if __name__ == "__main__":
    covid_data = get_data()
    print(covid_data["Germany"])