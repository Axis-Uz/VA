from fun import *
from fun import voice

if __name__ == "__main__":
    def clear(): return os.system('cls')
    written_flag = False
    clear()
    wishMe()
    while True:
        if written_flag == False:
            query = acceptCommand()
        else:
            query = input("%s: " % (user_profile["name"])).lower().strip()
        query_key = parseQuery(query)
        if query and query_key:
            if query_key == "exit":
                exit(0)
            elif query_key == "lock":
                lockWin()
            elif query_key == "sleep":
                goToSleep()
            elif query_key == "recycle":
                emptyBin()
            elif query_key == "weather":
                retrieveWeather(query)
            elif query_key == "search":
                searchWikipedia(query)
            elif query_key == "solve":
                solveProblems()
            elif query_key == "music":
                playMusic(query)
            elif query_key == "youtube":
                playYouTube(query)
            elif query_key == "dictionary":
                useDictionary(query)
            elif query_key == "website":
                openWebsite(query)
            elif query_key == "facts":
                getFacts()
            elif query_key == "jokes":
                getJokes()
            elif query_key == "date":
                getDate()
            elif query_key == "time":
                getTime()
            elif query_key == "email":
                sendMail(query)
            elif query_key == "change-mode":
                written_flag = True if written_flag == False else False
            elif query_key == "cls":
                clear()
