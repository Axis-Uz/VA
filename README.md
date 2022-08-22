# VA
 Implementation Virtual Assistant
 
## Features

## Before You Start
1. Go to `data/user_profile.json` and set up your profile and contact list.
2. Generate a Password for your Gmail[^5]
3. You can go to `data/va_settings.json` to add your favorite website
4. Go to `data/voices.json` to change your voice by setting `default = "true"`

## Default Commands
| Action                         | Commands                                                        |
| :----------------------------- | :-------------------------------------------------------------- |
| Play Random Local Music[^1]    | *Play Music*                                                    |
| Play Specific LocalMusic[^1]   | *I wan to listen to (music-name)*                               |
| Open a website[^2]             | *Open website (website-name)*, *I want to visit (website-name)* |
| Search Wikipedia               | *Search (?)*, *I want to search (?)*                            |
| Search Youtube                 | *Youtube (?)*                                                   |
| Tell a Joke                    | *Tell me a Joke*, *I want to hear a joke*                       |
| Tell the Time                  | *What is the time now*, *Time*                                  |
| Tell the Date                  | *What is the date*, *Date*                                      |
| Send a Mail[^3]                | *Send a Mail*, *Send a Mail to (contact-name)*                  |
| Lookup in Dictionary           | *lookup/look up/dictionary/define (word)*                       |
| Solve Problems & GK            | *ask wolf*,*solve*,*I have a Question*                          |
| Definition of Scientific Terms | *define*                                                        |
| News                           | *Top headlines*, *Top news*                                     |
| Weather[^4]                    | *Weather*, *What is the Forecast Today*,*Forecast Weather*      |
| Tell a Facts                   | *Tell me Fact*, *I want to hear a fact*                         |
| Change Input Mode              | *Write Mode*, *Typing Mode*, *Voice Mode*, *Change Mode*        |
| Clear Output Screen            | *Clear*                                                         |
| Enter Sleep State              | *Sleep Mode*,*Go To Sleep*                                      |
| Lock The Device                | *Windows Lock*,*Lock*                                           |
| Empty Recycle Bin              | *Recycle Bin*,*Empty Recycle Bin*                               |
| Quit                           | *quit/exit/goodbye/bye/close*                                   |


### Footnotes
[^1]: You need to set your music directory in `data/user_profile.json`.
[^2]: You need to set your preferred website in `data/va_settings.json`.
[^3]: You need add your contacts in `data/user_profile.json`.
[^4]: You need to set your city in `data/va_settings.json`.
[^5]: **TODO** --> Add Medium Link For Generating Password.   