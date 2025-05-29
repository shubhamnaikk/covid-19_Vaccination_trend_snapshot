import requests

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
r = requests.get(url)
with open("owid-covid-data.csv", "wb") as f:
    f.write(r.content)
print("Downloaded CSV")