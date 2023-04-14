from bs4 import BeautifulSoup
from decimal import Decimal
import re

def getRatings(htmlText):
    soup = BeautifulSoup(htmlText, 'html.parser')
    findSuspiciousKeyWords(soup.text)
    ratingValues =[]
    ratingLines = soup.find_all('span', attrs={"class": "h3-semibold index__score__16yy9"})
    for ratingLine in ratingLines:
        ratingStr = ratingLine.text
        rating = Decimal(ratingStr.replace(',','.'))
        ratingValues.append(rating)
        print(rating)
    return ratingValues

def findSuspiciousKeyWords(htmlTextBodyAsString):
    anwalt = re.findall('anwalt', htmlTextBodyAsString.lower())
    fake = re.findall('fake', htmlTextBodyAsString.lower())
    loesch = re.findall('löschen', htmlTextBodyAsString.lower())
    unterdrueck = re.findall('unterdrück', htmlTextBodyAsString.lower())
    suspiciousKeyWordCounter = len(anwalt) + len(fake) + len(loesch) + len(unterdrueck)
    print('suspicious keywords: ', suspiciousKeyWordCounter)
    return suspiciousKeyWordCounter

