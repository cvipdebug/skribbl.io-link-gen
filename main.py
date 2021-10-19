import requests,gratient
from os import system
import random
import string

def purple(text):
    system(""); faded = ""
    red = 35
    for character in text:
        red += 3
        if red > 255:
            red = 255
        faded += (f"\033[38;2;{red};0;220m{character}")
    return faded

linksshit = []
num = 0
working = 0
non_working = 0

system("cls && title Skribbl.io Link Gen")

banner = (gratient.purple("""
                                ┌─┐┬┌─┬─┐┬┌┐ ┌┐ ┬   ┬┌─┐  ┬  ┬┌┐┌┬┌─  ┌─┐┌─┐┌┐┌
                                └─┐├┴┐├┬┘│├┴┐├┴┐│   ││ │  │  ││││├┴┐  │ ┬├┤ │││
                                └─┘┴ ┴┴└─┴└─┘└─┘┴─┘o┴└─┘  ┴─┘┴┘└┘┴ ┴  └─┘└─┘┘└┘
                                                c       i
                                                    v       p
"""))

print(banner)
id = input(purple("Are you readt (y/n)"))
if id == "y":
    system("cls")
    print(banner)
    while True:
        IdGen = ('').join(random.choices(string.ascii_letters + string.digits, k=12))
        ID = f"{IdGen}"
        url = f"https://skribbl.io/?{ID}"
        r34 = requests.get(url)
        if r34.status_code == 200:
            working += 1
            num += 1
            system("title Skribbl.io Link Gen Working: " + str(working) + " Number Gen: " + str(num))
            print(gratient.green("Working Link : " + url))
            link = open("links.txt", "a")
            link.write(url + "\n")
        if r34.status_code == 404:
            non_working += 1
            system("title Skribbl.io Link Gen Working: " + str(working) + " Number Gen: " + str(num) + " Not Working Links: " + str(non_working))
            print(gratient.red("Not A Working Link : " + url))
if id == "n":
    system("cls")
    exit()
