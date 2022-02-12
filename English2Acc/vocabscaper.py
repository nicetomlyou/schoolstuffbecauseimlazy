from bs4 import BeautifulSoup
import requests


def getdef(soup):
    results = soup.find(class_="dtText")
    results = results.prettify()
    # print(results)
    halfparsed = results.split(':\n </strong>\n')
    #print(halfparsed)
    parsedarr = halfparsed[1].split('\n</span>\n')
    #print(parsedarr[0])
    return parsedarr[0]


def getpos(soup):
    try:
        results = soup.find(class_="fl")
        results = results.prettify()
        halfparsed = results.split('href="/dictionary/')
        parsedarr = halfparsed[1].split('"')
        #print(parsedarr)
        return parsedarr[0]
    except:
        return None

def getsynonyms(thesoup):
    results = thesoup.find(class_="mw-list")
    results = results.prettify()
    # print(results)
    halfparsed = results.split('href="/thesaurus/', 100)
    # print(halfparsed)
    synonymsarr = []
    for num in range(-1, len(halfparsed)):
        if num % 2 == 0:
            parsedarr = halfparsed[num - 1].split('"')
            synonymsarr.append(parsedarr[0])
    return synonymsarr


def getvariations(soup, pos):
    if pos.count("verb") > 0:
        results = soup.find(class_="vg-ins")
        results = results.prettify()
        halfparsed = results.split('<span class="if">')
        parsedarr = halfparsed[1].split("</span")
        return parsedarr[0]
        # halfparsed = results.split('href="/dictionary/')
        # parsedarr = halfparsed[1].split('"')
        # return parsedarr[0]
    else:
        return None

def requestall(word):
    page = requests.get("https://www.merriam-webster.com/dictionary/" + word)
    thesaurus = requests.get("https://www.merriam-webster.com/thesaurus/" + word)
    soup = BeautifulSoup(page.content, "html.parser")
    thesoup = BeautifulSoup(thesaurus.content, "html.parser")
    partofspeech = getpos(soup)
    definition = getdef(soup)
    synonyms = getsynonyms(thesoup)
    variation = getvariations(soup, partofspeech)
    return partofspeech, definition, synonyms, variation
    # print(results)


#bruh, bruh2, bruh3 = requestall("cry")
# print(bruh + " " + bruh2)


def structurize(word, definition, synonyms, partofspeech, maxsynonyms=2, variation = None):
    #definition = definition.strip("\n  ")
    #definition = definition.strip('<strong class="mw_t_bc">\n:')
    definition = definition.replace(' <strong class="mw_t_bc">\n', "")
    string = word + "(" + partofspeech + ")\ndefinition: "
    string = string + definition + "\nsynonyms: "
    for num in range(maxsynonyms):
        if num + 1 == maxsynonyms:
            string = string + synonyms[num]
        else:
            string = string  + synonyms[num] + ", "
    if variation == None:
        print(string)
    else:
        string = string + "\nvariation: " +variation.strip("\n  ")
        print(string)


def poopeverythingout(word, maxsynonyms=2):
    pos, defi, syn, var = requestall(word)
    #print(defi)
    structurize(word, defi, syn, pos, maxsynonyms, var)


inpword = input("word")

poopeverythingout(inpword)
#getvariations("cry", "verb")
