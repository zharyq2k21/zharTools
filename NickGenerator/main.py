#!.env/Scripts/python
from selenium import webdriver
from rich.prompt import Prompt, PromptBase
from rich import print
import fake_useragent
import pyfiglet
import pathlib
import os


BASE_DIR = pathlib.Path(__file__).resolve().parent # Путь до текущей директорий
FIREFOX_WEBDRIVER = os.path.join(BASE_DIR, "drivers\\firefox.exe") # Путь до вебдрайвера firefox
fake_ua = fake_useragent.UserAgent().random
PromptBase.illegal_choice_message = "[[bold yellow]![/bold yellow]] Пожалуйста, выберите один из доступных вариантов"

option = webdriver.FirefoxOptions() # Настройки firefox
option.set_preference("dom.webnotifications.enabled", False) # Уведомления отключены
option.set_preference("general.useragent.override", fake_ua) # Фейк юзер агент
option.set_preference("dom.webdriver.enabled", False) # Вебдрайвер отключен
option.set_preference("media.volume_scale", 0) # Звук 0%
option.headless = True # Будет работать в фоновом режиме

browser = webdriver.Firefox(executable_path=FIREFOX_WEBDRIVER, options=option) # Вебдрайвер firefox 
browser.get("https://nick-name.ru/generate/") # url адресс

def banner():
    os.system("cls")
    print( "[bold purple]" + pyfiglet.Figlet("slant").renderText("NickName") + "[/bold purple]", end="")
    
def nick_gen(): # Генерирование ников
    nicknames = [] # Список с никами

    while len(nicknames) <= 10:
        # Нажимаем на кнопку Generate
        generate_button_xpath = "/html/body/div/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input"
        browser.find_element_by_xpath(generate_button_xpath).click()

        # Получаем ник от url адреса
        nickname = browser.find_element_by_id("register").get_attribute("href")[37:] 

        nicknames.append(nickname) # Добавляем в список наши nick name-ы
        print("  [[bold purple]*[/bold purple]] Ник неймы: {}".format(nickname))

    # Ждем 
    return Prompt.ask("\n  [bold white][[bold yellow]![/bold yellow]][/bold white] Повторить", choices=["да", "нет"])

def main():
    banner()

    yes_no = nick_gen()

    if yes_no == "да":
        banner()
        nick_gen()
    else:
        print("[bold red]" + pyfiglet.Figlet("smslant").renderText("Exit") + "[/bold red]")
        exit()

try:
    main()
except KeyboardInterrupt:
    yes_no = Prompt.ask("\n  [bold white][[bold yellow]![/bold yellow]][/bold white] Покинуть", choices=["да", "нет"])

    if yes_no == "да":
        print("[bold red]" + pyfiglet.Figlet("smslant").renderText("Exit") + "[/bold red]")
        exit()
    else:
        main()
