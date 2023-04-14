import string

companyName = ''
nameInUrl = ''
specialCharacters = ['(', ')', ':',  ' ', '_', '[', ']']
dotChar = '.'


def replaceSpecialCharacters(companyName):
    companyNameAsCharArray = [*companyName]
    result = ''
    for element in companyNameAsCharArray:
        element = replaceSpecialCharacterWithDash(element)
        element = replaceSpecialCharacterOfDot(element)
        result += element
    print('result: ' + result)
    return result


def replaceSpecialCharacterWithDash(singleCharOfCompanyName):
    for character in specialCharacters:
        if singleCharOfCompanyName == character:
            print('found dash char')
            singleCharOfCompanyName = '-'
    return singleCharOfCompanyName

def replaceSpecialCharacterOfDot(singleCharOfCompanyName):
    if singleCharOfCompanyName == dotChar:
            print('found dot char')
            singleCharOfCompanyName = ''
    return singleCharOfCompanyName

def makeUrl(companyName):
    urlFirstpart = 'https://www.kununu.com/de/'
    urlLastPart = replaceSpecialCharacters(companyName)
    result = urlFirstpart + urlLastPart + "/kommentare"
    print('make URL, result is: ', result)
    return result
