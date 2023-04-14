from googlesearcher.visiturl import *
# returns url string "https://www.kununu.com/de/company-name/kommentare"
def makeGoogleSearch(queryfield):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    # to search
    query = "kununu " + queryfield
    counter = 0

    for querySingleResult in search(query, tld="co.in", num=10, stop=10, pause=2):
        counter = counter +1
        if counter == 2:
           print('querySingleResult: ' + querySingleResult)
        urlString = querySingleResult + "/kommentare"
        return urlString

def browsePageNumbers(urlString):
    htmlResulString = str(makeUrlRequest(urlString))
    counter = 1
    nextPageUrl = urlString + '/' + str(counter)
    while counter < 6 and makeGoogleSearch(nextPageUrl) != None and makeGoogleSearch(nextPageUrl) != '':
        counter += 1
        # print('pagecount: ', counter)
        nextPageUrl = urlString + '/' + str(counter)
        print('nextPageUrl: ', nextPageUrl)
        try:
            htmlResulString = htmlResulString + str(makeUrlRequest(nextPageUrl))
            # print('htmlResultAppend!')
        except:
            print('no more pages!')
            break
    return htmlResulString

