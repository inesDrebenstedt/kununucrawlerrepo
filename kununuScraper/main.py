from stringtools.preparename import *
from stringtools.extracting import *
from googlesearcher.searchwithgoogle import *
from googlesearcher.visiturl import *
from mathtools.analyseratings import *
# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Kununu Scraper')

# 1. returns string "https://www.kununu.com/de/company-name/Kommentare"
url =  makeGoogleSearch('dfv deutsche familienversicherung')
#print('URL result: ' + str(url))

# 2. returns string of html body
htmlResultBody = str(makeUrlRequest(url))
# append html string result from other pages ...kommentare/2 etc.
htmlResultBody = htmlResultBody + browsePageNumbers(url)

# 3. returns array of decimals
ratings = getRatings(htmlResultBody)

# 4. makes X,Y plot with data points
generateXYdata(ratings)

