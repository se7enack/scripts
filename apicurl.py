#!/usr/bin/env python3

# Stephen Burke 2020-Nov-28

from datetime import datetime
import re
import time
import requests

value1 = ""
value2 = ""
tzoffsetnum = ""
tzones = ["GMT(GMT+00:00)", "UTC(GMT+00:00)", "ECT(GMT+01:00)", "EET(GMT+02:00)", "ART(GMT+02:00)", "EAT(GMT+03:00)",
          "MET(GMT+03:30)", "NET(GMT+04:00)", \
          "PLT(GMT+05:00)", "IST(GMT+05:30)", "BST(GMT+06:00)", "VST(GMT+07:00)", "CTT(GMT+08:00)", "JST(GMT+09:00)",
          "ACT(GMT+09:30)", "AET(GMT+10:00)", \
          "SST(GMT+11:00)", "NST(GMT+12:00)", "MIT(GMT-11:00)", "HST(GMT-10:00)", "AST(GMT-09:00)", "PST(GMT-08:00)",
          "PNT(GMT-07:00)", "MST(GMT-07:00)", \
          "CST(GMT-06:00)", "EST(GMT-05:00)", "IET(GMT-05:00)", "PRT(GMT-04:00)", "CNT(GMT-03:30)", "AGT(GMT-03:00)",
          "BET(GMT-03:00)", "CAT(GMT-01:00)"]

def yorn(question, url):
    global response
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        try:
            r = requests.get(url)
            print(r.content)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        except requests.exceptions.ConnectionError as err:
            raise SystemExit(err)            
    if reply[0] == 'n':
        print("\nUser aborted, now exiting.")
        quit()
    else:
        yorn(question, url)

def validate(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        time.sleep(1)
    except:
        print(str(date_text) + " is invalid. Please use the following format: YYYY-M-D")
        print("For example, today would be " + datetime.today().strftime("%Y-%m-%d") + '.')
        print("\nPlease enter both dates again...\n")
        time.sleep(2)
        dates()

def settheenv():
    def opt_a():
        print("SERVER1")
        global server
        global apikey
        server = "server1"
        apikey = "API-Key_for_that_server"

    def opt_b():
        print("SERVER2")
        global server
        global apikey
        server = "server2"
        apikey = "API-Key_for_that_server"

    def opt_c():
        print("SERVER3")
        global server
        global apikey
        server = "server3"
        apikey = "API-Key_for_that_server"

    def opt_d():
        print("SERVER4")
        global server
        global apikey
        server = "server4"
        apikey = "API-Key_for_that_server"

    def opt_e():
        print("SERVER5")
        global server
        global apikey
        server = "server5"
        apikey = "API-Key_for_that_server"

    def opt_f():
        print("SERVER6")
        global server
        global apikey
        server = "server6"
        apikey = "API-Key_for_that_server"

    def opt_g():
        print("SERVER7")
        global server
        global apikey
        server = "server7"
        apikey = "API-Key_for_that_server"

    def invalid_opt():
        print("\nInvalid choice. Try again. Valid options are A-G.\n")
        settheenv()

    options = {"A": ["SERVER1", opt_a], "B": ["SERVER2", opt_b], "C": ["SERVER3", opt_c], "D": ["SERVER4", opt_d], \
               "E": ["SERVER5", opt_e], "F": ["SERVER6", opt_f], "G": ["SERVER7", opt_g]}
    for option in options:
        print(option + ") " + options.get(option)[0])
    choise = input("Please choose an environment: ").upper()
    val = options.get(choise)
    if val is not None:
        action = val[1]
        time.sleep(1)
    else:
        action = invalid_opt
        time.sleep(3)
    action()


def dates():
    global startdate
    global enddate
    print("\nDates should be entered in the following format:")
    print("2020-1-1 and 2020-12-31, i.e. YYYY-M-D")
    print("Do not pad month or day with leading 0's\n")
    startdate = input("Please enter START date: ")
    validate(startdate)
    enddate = input("Please enter END date: ")
    validate(enddate)


def timez():
    global tzoffsetnum
    for index in range(len(tzones)):
        print(str(index) + ") " + tzones[index])
    tzoffsetnum = input("Please choose a valid timezone number from 0 - " + str(len(tzones) - 1) + ": ")
    time.sleep(1)

settheenv()

try:
    dates()
except:
    print("Try again")
    dates()

while True:
    try:
        value1 = int(input("Please enter some integer value: "))
    except ValueError:
        print("\nYou've entered an invalid value. Try again.\n")
        continue
    else:
        break

while True:
    try:
        value2 = int(input("Please enter some other integer value: "))
    except ValueError:
        print("\nYou've entered an invalid value. Try again.\n")
        continue
    else:
        break

while True:
    try:
        timez()
        tzoffsetraw = tzones[int(tzoffsetnum)]
    except IndexError:
        print("\nYou've entered an invalid value. Try again.\n")
        continue
    else:
        break

if "+" in tzoffsetraw:
    prefix = '%2B'
else:
    prefix = '-'

tzoffsetnocolon = re.sub('\D', '', tzoffsetraw)
tzoffsetnopre = tzoffsetnocolon[:2] + ':' + tzoffsetnocolon[2:]
tzoffset = prefix + tzoffsetnopre
url = "https://" + server + ".getburke.com/api/v1/" + str(value1) + "/" + str(
    value2) + "?apikey=" + \
      apikey + "&start=" + startdate + "T00:00:00.000" + str(tzoffset) + "&end=" + enddate + "T00:00:00.000" + str(tzoffset)

print("\n" + url)
time.sleep(1)
yorn("\nDoes the generated URL look correct?", url)
     
