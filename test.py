import pyautogui as pg
import time

leads = []
j = 0
time.sleep(5)
with open('text.txt', mode='r', encoding='utf-8') as file:
    j = 0
    while j < 200:
        i = 0
        while i < 4:
            line = file.readline().rstrip()
            leads.append(line)
            i+=1
        job = leads[3]
        try :
            name, un = leads[0].split()
        except ValueError:
            name = leads[0]

        file.readline()
        pg.click(790, 307)
        pg.hotkey('command', 'a')
        pg.write(leads[2])
        pg.click(548, 827)
        pg.click(535, 720)
        pg.click(346, 23)
        time.sleep(2)
        pg.click(99, 186)  
        pg.click(99, 186)  
        pg.click(99, 186)  
        pg.click(99, 186)    
        time.sleep(3)
        pg.write(leads[1])
        pg.hotkey('tab')
        pg.write("Subject")
        pg.hotkey('tab')
        text = f"Hi {name}\n\nThis is where you put the txt to be typed,\n\nBest Regards,\n{leads[2]}\n{job}"
        pg.write(text)
        pg.hotkey('enter')
        pg.click(132, 179)
        pg.sleep(3)
        pg.click(127, 27)
        pg.sleep(1)
        leads = []
        j+=1
        
