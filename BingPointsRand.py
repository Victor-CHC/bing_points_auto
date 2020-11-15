import webbrowser
import random
import time

"""
This program opens web browsers and makes random
Bing searches (from a set list) in each browser.
It will be a random sample so no duplicate searches.

For each desktop Bing search you get
3 Bing points provided you are logged in. Mobile searches
will require you to manually put the browser into mobile mode.

To make the searches seem a little more organic, there will be pauses
in between each search of random length between 0 and 1

Account logins will need to be done in advanced and stored/cached
on the individual browser.

This program is useful if you have multiple Outlook accounts.
"""

#list of searches to be used for the web browser
searches = ["lenovo","hp","razer","dell","laptops","ram prices","surface go",
            "surface pro","gaming laptops","gaming desktops","nvidia","amd",
            "gpu","ps plus","psn","microsoft","apple","sony",
            "python","r","matlab","neural nets","tensorflow","keras","big data",
            "gaming mice","gaming keyboards","intel","ram","motherboards",
            "acer","asus","omen","legion gaming","huawei","xiaomi","javascript",
            "switch","vita","ps4", 
            "3ds","data science jobs","web browsers","search engines","bing",
            "google","mozilla","firefox","waterfox","brave browser","vivaldi",
            "opera browser","edge","linux","windows","persona arena","bbctb",
            "bbtag","fifa", "nba 2k", "2k sports", "tekken", "street fighter",
            "soul calibur", "sega saturn mini", "4k gaming", "rtx 3090", 
            "rtx 3080", "rtx 3070", "rtx 3060", "rtx 3050", "budget gpus", 
            "steam sale","tech news","apple","mac mini","macbook","sonic", "yakuza 0",
            "yakuza 3", "yakuza 4", "yakuza 5", "mario", "dark souls", "xbox",
            "xbox series", "game pass", "game pass ultimate", "top games",
            "games deals", "ps5", "ps4 pro", 'nintendo switch', "hokuto no ken",
            "speakers", "motherboards", "heat sinks", "fans", "monitors", 
            "4k monitors", "ultrawide monitors", "1440p gaming", "1440p monitors",
            "psu", "corsair", "anker", "smart lights", "smart watch", "smart tv",
            "usb hubs", "smart speakers", "noise cancelling","anc headphones",
            "anc earphones", "gaming mouse mats", "gaming desk", "internet speed",
            "speed test", "1gbps", "usb-4"
            
            ]

# Register your browser programs
# NOTE 1: Change the path names if they are installed in a different location
# NOTE 2: Delete or add browsers as appropriate.
google_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('google', None,webbrowser.BackgroundBrowser(google_path),1)

firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path),1)

brave_path="C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
webbrowser.register('brave', None,webbrowser.BackgroundBrowser(brave_path),1)

opera_path="C:\\Program Files\\Opera\\launcher.exe"
webbrowser.register('opera', None,webbrowser.BackgroundBrowser(opera_path),1)

vivaldi_path="C:\\Program Files\\Vivaldi\\Application\\vivaldi.exe"
webbrowser.register('vivaldi', None,webbrowser.BackgroundBrowser(vivaldi_path),1)

#List the browsers you want to make searches in
#NOTE 3: Delete or add browsers as appropriate
browsers = ['google','firefox','brave','opera','vivaldi']

#Iterate through each browser opening a new tab for each Bing search item
for app in browsers:
    searchSample = random.sample(searches,40)
    for search in searchSample:
        webbrowser.get(app).open_new_tab("https://www.bing.com/search?q=" + search)

        #Short time lapse of random length between each search to appear organic
        time.sleep(random.random())




        
