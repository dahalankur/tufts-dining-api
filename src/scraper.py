from bs4 import BeautifulSoup
import requests
import json

def main():
    # todo: make it dynamic to support all dining halls, display date as well
    url = "http://menus.tufts.edu/FoodPro%203.1.NET/shortmenu.aspx?sName=TUFTS+DINING&locationNum=03&locationName=Kindlevan+Caf%26eacute%3b+&naFlag=1"
    website = requests.get(url)
    soup = BeautifulSoup(website.text, 'html.parser')

    div_list = soup.findAll("div")
    menu_date = None

    for div in div_list:
        try:
            if not menu_date:
                if div["class"][0] == "shortmenutitle":
                    menu_date = "".join(div.text.split(",")[-2:]).strip()
                    #date = str([date.strip() for date in menu_date])[1:]

            menu_type = div.text if div["class"][0] == "shortmenumeals" else None
            category = div.text if div["class"][0] == "shortmenucats" else None

            if menu_type:
                print(f"xxxxxxxxxxxxxxxxx{menu_type}xxxxxxxxxxxxxxxxx")
            if category:
                print(f"--------------------{category}------------------")
            if div["class"][0] == "shortmenurecipes":
                print(div.text)
        except:
            continue

    # print(menu_date)



if __name__ == "__main__":
    main()