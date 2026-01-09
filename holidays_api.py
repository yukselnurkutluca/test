import requests
url = "https://date.nager.at/api/v3/PublicHolidays/2025/TR"
response = requests.get(url)
holidays = response.json()

for holiday in holidays:
    print(holiday["date"], "-",
holiday["localName"])
