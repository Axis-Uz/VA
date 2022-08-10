from fun import *

while waitForWake():
    while True:
        speak("Hello, I am . How can I help you?")
        query = acceptCommand()
        qk = parseQuery(query)
        if query and qk:
            if qk == "facts":
                getFacts()
            elif qk == "jokes":
                getJokes()
            elif qk == "news":
                getNews()
            elif qk == "search":
                searchWikipedia(query)
            elif qk == "solve":
                solveProblems()
            elif qk == "music":
                playMusic(query)
            elif qk == "youtube":
                playYouTube(query)
            elif qk == "dictionary":
                useDictionary(query)
            elif qk == "website":
                openWebsite(query)
            elif qk == 'change-voice':
                voice = changeVoice()
                wishMe()
            elif qk == "listen":
                pass
                speak("What can I do for you ?")
                query = acceptCommand().lower()
                qk = parseQuery(query)
            elif qk == "exit":
                # Crashes Jupyter
                quit(0)
            elif query == "sleep":
                break
            else:
                speak("I don't know that")
