import platform
from clint.textui import colored
import subprocess
from Brute import face
from Brute import insta
from Brute import twitter
from Brute import snapchat
from banner import banner
import os
banner.brute19banner()

print(colored.red("\n[")+colored.green("*")+colored.red("]")+"https://github.com/AzizKpln")
choice=input(colored.red("\n\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
if choice=="2":
    banner.normal_banner()
    print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Mail Address/Phone Number")+colored.magenta("]"))
    mail_address=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
    print(" ")
    print(colored.red("-"*50))
    print(" ")
    print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Wordlist Path")+colored.magenta("]"))

    pw_path=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
    with open(pw_path,"r",encoding="utf-8") as passwords:
        pw=passwords.readlines()
    banner.normal_banner()
    face.fb_brute(mail_address,pw)
elif choice=="1":
    banner.normal_banner()
    print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Mail Address/Phone Number/Username")+colored.magenta("]"))
    mail_address=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
    print(" ")
    print(colored.red("-"*50))
    print(" ")
    print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Wordlist Path")+colored.magenta("]"))

    pw_path=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
    banner.normal_banner()
    with open(pw_path,"r",encoding="utf-8") as passwords:
        pw=passwords.readlines()
    insta.ig_brute(mail_address,pw)
elif choice=="3":
    banner.normal_banner()
    print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Mail Address/Phone Number")+colored.magenta("]"))
    mail_address=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
    print(" ")
    print(colored.red("-"*50))
    print(" ")
    print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Wordlist Path")+colored.magenta("]"))

    pw_path=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
    banner.normal_banner()
    with open(pw_path,"r",encoding="utf-8") as passwords:
        pw=passwords.readlines()
    twitter.tw_brute(mail_address,pw)