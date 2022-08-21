from fun import *

with_params = {
    "youtube": playYouTube,
    "facts": getFacts,
    "email": sendMail,
    "dictionary": useDictionary,
    "search": searchWikipedia,
    "website": openWebsite,
    "music": playMusic,
}

without_params = {
    "sleep": goToSleep,
    "solve": solveProblems,
    "weather": retrieveWeather,
    "lock": lockWin,
    "date": getDate,
    "time": getTime,
    "jokes": getJokes,
    "news": getNews,
    "recycle": emptyBin,
}
if __name__ == "__main__":
    def clear(): return os.system('cls')
    written_flag = False
    clear()
    # while isConnected():
    while written_flag:
        wishMe()
        if written_flag == False:
            query = acceptCommand()
        else:
            query = input("%s: " % (user_profile["name"])).lower().strip()
        query_key = parseQuery(query)
        if query and query_key:
            if query_key in without_params:
                without_params[query_key]()
            elif query_key in with_params:
                with_params[query_key](query)
            elif query_key == "cls":
                clear()
            elif query_key == "exit":
                speak("Goodbye 👋🏻")
                exit(0)
            elif query_key == "change-mode":
                print(query_key)
                written_flag = True if written_flag == False else False
                print(written_flag)
    else:
        speak("No Internet Connection 🙀 ", 'red')
        speak("Please Connect to Internet 😓", 'red')
        # acceptCommand
