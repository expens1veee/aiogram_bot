import selenium.webdriver
from selenium.webdriver.common.by import By


lst = []
driver = selenium.webdriver.Chrome() # Firefox()

driver.get('https://rasp.rea.ru/?q=15.27д-мо02%2F23б#today')
driver.maximize_window()

all_cards = driver.find_elements(By.XPATH, '//*[@id="zoneTimetable"]/div')
str1 = ""
my_file = open("rasp.txt", "w+")
for row in all_cards:
    # my_file.write(row.text)
    str1+=row.text
# str1 = str1.replace("\n", " ")

rasp = str1
rasp = rasp.replace("\n", " ")
rasp = rasp.split()
pn = []
vt = []
sr = []
ch = []
pt = []
sub = []
last = 0
rasp1 = []
cf = ['1','2','3','4','5','6']
for i in range (len(rasp)):
    if rasp[i] == 'пара' and rasp[i+2] == 'пара':
        rasp1.append(rasp[i])
        rasp1.append('-')
    else:
        rasp1.append(rasp[i])
print(rasp1)

for i in range (len(rasp1)):
    if (rasp1[i] != 'ВТОРНИК,'):
        pn.append(rasp1[i])
        last = i +1
    else:
        break
for i in range (last, len(rasp1)):
    if (rasp1[i] != 'СРЕДА,'):
        vt.append(rasp1[i])
        last = i + 1
    else:
        break
for i in range (last, len(rasp1)):
    if (rasp1[i] != 'ЧЕТВЕРГ,'):
        sr.append(rasp1[i])
        last = i + 1
    else:
        break
for i in range (last, len(rasp1)):
    if (rasp1[i] != 'ПЯТНИЦА,'):
        ch.append(rasp1[i])
        last = i + 1
    else:
        break
for i in range (last, len(rasp1)):
    if (rasp1[i] != 'СУББОТА,'):
        pt.append(rasp1[i])
        last = i + 1
    else:
        break
for i in range (last, len(rasp1)):
        sub.append(rasp1[i])
        last = i + 1
# for i in range(last,len(rasp)):
#     while(rasp[i] != 'СРЕДА,'):
#         vt.append(rasp[i])
#         last = i






greet = "Привет, {name}, я бот️"
menu = "📍 Главное меню"
