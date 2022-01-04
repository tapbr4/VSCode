from ast import literal_eval as make_tuple
from datetime import datetime
from time import sleep
import pyautogui


# Setup #
browsers = 2 #Enter the number of accounts/browsers here
name_list = [
    'browser_icon','address_bar',
    'play_now', 'connect_wallet',
    'metamask_icon','metamask_confirm',
    'treasure_hunt','menu_arrow',
    'heroes','character_list',
    'work','rest','close',
    'map','next_map','main_menu']
pos = []

# Read config.txt #
with open('config.txt') as f:
    lines = f.read().splitlines()

# Dict #
line = 0
for browser in range(1, browsers+1):
    pos.append(dict())
    count = 0
    for item in lines[line:(browser*16)]:
        t_item = make_tuple(item)
        pos[browser-1][name_list[count]] = t_item
        count += 1
    line += 16

# Auto #
## Opening Browser
for i in range(browsers):
    pyautogui.click(x=pos[i]['browser_icon'][0], y=pos[i]['browser_icon'][1])
sleep(3)

## Loop
while True:
    print('\n[STARTING LOOP]\nLOGGING INTO THE GAME [{}]'.format(str(datetime.now().hour) + ':' + str(datetime.now().minute)))
    ## Entering the Website
    for i in range(browsers):
        pyautogui.click(x=pos[i]['address_bar'][0], y=pos[i]['address_bar'][1])
        sleep(2)
        pyautogui.write('https://bombcrypto.io/')   
        pyautogui.press('enter')
        sleep(2)
        pyautogui.press('enter')
        sleep(2)

        ## Play / Metamask Confirmation
        pyautogui.click(x=pos[i]['play_now'][0], y=pos[i]['play_now'][1])
        sleep(5)
        pyautogui.hotkey('alt', 'tab')
        sleep(3)
        pyautogui.hotkey('ctrl', 'w')
        sleep(5)
        pyautogui.click(x=pos[i]['connect_wallet'][0], y=pos[i]['connect_wallet'][1])
        sleep(15)
        pyautogui.click(x=pos[i]['metamask_icon'][0], y=pos[i]['metamask_icon'][1], clicks=2, interval=0.25)
        sleep(5)
        pyautogui.click(x=pos[i]['metamask_confirm'][0], y=pos[i]['metamask_confirm'][1])
        sleep(5)

    ## In-game / Work
    print('PUTTING TO WORK [{}]'.format(str(datetime.now().hour) + ':' + str(datetime.now().minute)))
    for i in range(browsers):
        pyautogui.click(x=pos[i]['treasure_hunt'][0], y=pos[i]['treasure_hunt'][1])
        sleep(5)
        pyautogui.click(x=pos[i]['map'][0], y=pos[i]['map'][1], clicks=2, interval=0.5)
        sleep(5)
        pyautogui.click(x=pos[i]['menu_arrow'][0], y=pos[i]['menu_arrow'][1])
        sleep(5)
        pyautogui.click(x=pos[i]['heroes'][0], y=pos[i]['heroes'][1])
        sleep(5)
        pyautogui.click(x=pos[i]['character_list'][0], y=pos[i]['character_list'][1])
        sleep(3)
        for j in range(45):
            pyautogui.scroll(-1)
        sleep(3)
        for j in range(16):
            pyautogui.click(x=pos[i]['work'][0], y=pos[i]['work'][1])
            sleep(3)
        sleep(2)
        pyautogui.click(x=pos[i]['close'][0], y=pos[i]['close'][1], clicks=2, interval=1.5)
        sleep(5)
        pyautogui.click(x=pos[i]['map'][0], y=pos[i]['map'][1], clicks=2, interval=0.5)
        sleep(5)

    ## Working 1h (+Some sleep based on number of accounts)
    ## Click routine to go to the next map and avoid error messages.
    print('WORKING 1H [{}]'.format(str(datetime.now().hour) + ':' + str(datetime.now().minute)))
    for i in range(60):
        sleep(15)
        for j in range(browsers):
            pyautogui.click(x=pos[j]['next_map'][0], y=pos[j]['next_map'][1])
        sleep(15)
        for j in range(browsers):
            pyautogui.click(x=pos[j]['connect_wallet'][0], y=pos[j]['connect_wallet'][1])
        sleep(15)
        for j in range(browsers):
            pyautogui.click(x=pos[j]['metamask_icon'][0], y=pos[j]['metamask_icon'][1], clicks=2, interval=0.25)
            sleep(1)
            pyautogui.click(x=pos[j]['metamask_confirm'][0], y=pos[j]['metamask_confirm'][1], clicks=2, interval=0.25)
        sleep(15)
        for j in range(browsers):
            pyautogui.click(x=pos[j]['treasure_hunt'][0], y=pos[j]['treasure_hunt'][1])
        ### Prevents bombers from walking around without placing bombs.
        if(i%5==0 and i!=0): # Runs 11 times. (+1 minute and 6 seconds)
            sleep(2)
            for j in range(browsers):
                pyautogui.click(x=pos[j]['main_menu'][0], y=pos[j]['main_menu'][1])
            sleep(2)
            for j in range(browsers):
                pyautogui.click(x=pos[j]['treasure_hunt'][0], y=pos[j]['treasure_hunt'][1], clicks=2, interval=2)
    sleep(5)

    ## Rest
    print('PUTTING TO REST [{}]'.format(str(datetime.now().hour) + ':' + str(datetime.now().minute)))
    for i in range(browsers):
        pyautogui.click(x=pos[i]['menu_arrow'][0], y=pos[i]['menu_arrow'][1])
        sleep(5)
        pyautogui.click(x=pos[i]['heroes'][0], y=pos[i]['heroes'][1])
        sleep(5)
        pyautogui.click(x=pos[i]['character_list'][0], y=pos[i]['character_list'][1])
        sleep(3)
        for j in range(45):
            pyautogui.scroll(1)
        sleep(3)
        for j in range(16):
            pyautogui.click(x=pos[i]['rest'][0], y=pos[i]['rest'][1])
            sleep(3)
        sleep(2)
        pyautogui.click(x=pos[i]['close'][0], y=pos[i]['close'][1], clicks=2, interval=1.5)
        sleep(5)
        pyautogui.click(x=pos[i]['map'][0], y=pos[i]['map'][1], clicks=2, interval=0.5)
        sleep(5)
        
        ## Rest Confirmation
        pyautogui.click(x=pos[i]['main_menu'][0], y=pos[i]['main_menu'][1])
        sleep(3)
        pyautogui.click(x=pos[i]['treasure_hunt'][0], y=pos[i]['treasure_hunt'][1])
        sleep(3)

        ## Close Tab
        pyautogui.hotkey('ctrl', 't')
        sleep(3)
        pyautogui.hotkey('alt', 'tab')
        sleep(3)
        pyautogui.hotkey('ctrl', 'w')

    ## Resting 1h (+1h farm = 2h frequency)
    print('RESTING 1H [{}]'.format(str(datetime.now().hour) + ':' + str(datetime.now().minute)))
    sleep(3600-(85*browsers)) # 1h = 3600s | 85s = Total Sleep (Putting to Rest)