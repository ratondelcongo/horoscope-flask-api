import requests
from bs4 import BeautifulSoup

ZODIAC_NAMES = {
    "aries": 1,
    "tauro": 2,
    "geminis": 3,
    "cancer": 4,
    "leo": 5,
    "virgo": 6,
    "libra": 7,
    "escorpio": 8,
    "sagitario": 9,
    "capricornio": 10,
    "acuario": 11,
    "piscis": 12
}

ZODIAC_NUMBERS = {
    "1" : "aries",
    "2" : "tauro",
    "3" : "geminis",
    "4" : "cancer",
    "5" : "leo",
    "6" : "virgo",
    "7" : "libra",
    "8" : "escorpio",
    "9" : "sagitario",
    "10" : "capricornio",
    "11" : "acuario",
    "12" : "piscis"
}

def get_horoscope(zodiac_sign: str):
    res = requests.get(f'https://www.lavanguardia.com/horoscopo/signos-zodiaco-{zodiac_sign}/horoscopo-diario')
    soup = BeautifulSoup(res.text, 'html.parser')
    data = soup.select('#main > div > section.section-holder.sign-detail-section > div > div > div > p')
    return data[0].text.strip()