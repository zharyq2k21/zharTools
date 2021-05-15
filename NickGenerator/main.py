from selenium import webdriver
from rich.prompt import Prompt, PromptBase
from rich import print
import fake_useragent
import pyfiglet
import pathlib
import os

class NickGen(object):
    BASE_DIR = pathlib.Path(__file__).resolve().parent                  # Путь до текущей директорий
    FIREFOX_WEBDRIVER = os.path.join(BASE_DIR, "drivers\\firefox.exe")  # Путь до вебдрайвера firefox
    fake_ua = fake_useragent.UserAgent().random                         # Рандомдый юзер агент
    PromptBase.illegal_choice_message = "  [[bold yellow]![/bold yellow]] Пожалуйста, выберите один из доступных вариантов"

    def __init__(self):
        option = webdriver.FirefoxOptions()                               # Настройки firefox
        option.set_preference("dom.webnotifications.enabled", False)      # Уведомления отключены
        option.set_preference("general.useragent.override", self.fake_ua) # Фейк юзер агент
        option.set_preference("dom.webdriver.enabled", False)             # Вебдрайвер отключен
        option.set_preference("media.volume_scale", 0)                    # Звук 0%
        option.headless = True                                            # Будет работать в фоновом режиме

        self.browser = webdriver.Firefox(executable_path=self.FIREFOX_WEBDRIVER, options=option) # Вебдрайвер firefox 
        self.browser.get("https://nick-name.ru/generate/")                                       # url адресс

    def clear_terminal(self):
        if os.sys.platform == "nt":
            os.system("clear")
        else:
            os.system("cls")

    def banner(self):
        self.clear_terminal() # Очищаем терминал
        print(
            "[bold purple]" + \
                pyfiglet.Figlet("slant").renderText("NickName") + \
            "[/bold purple]",
        end="")
    
    def nick_gen(self): # Генерирование ников
        self.banner()   # Показываем баннер

        nicknames = []  # Список с никами

        while len(nicknames) <= 10:
            # Нажимаем на кнопку Generate
            generate_button_xpath = "/html/body/div/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input"
            self.browser.find_element_by_xpath(generate_button_xpath).click()

            # Получаем ник от url адреса
            nickname = self.browser.find_element_by_id("register").get_attribute("href")[37:] 

            nicknames.append(nickname) # Добавляем в список наши nick name-ы
            print("  [[bold purple]*[/bold purple]] Ник неймы: {}".format(nickname))

        repeat = Prompt.ask(
            "\n  [bold white][[bold yellow]![/bold yellow]][/bold white] Повторить",
            choices=["да", "нет"]
        )
        return repeat

    def main(self):
        repeat = self.nick_gen() # Генерируем ники и показываем баннер

        if repeat == "да":
            self.main()          # Рекурсия
        else:
            print("[bold red]" + pyfiglet.Figlet("smslant").renderText("Exit") + "[/bold red]")
            exit()


if __name__ == "__main__":
    nickgen_obj = NickGen()

    try:
        nickgen_obj.main()
    except KeyboardInterrupt:
        quit_ = Prompt.ask("\n  [bold white][[bold yellow]![/bold yellow]][/bold white] Покинуть", choices=["да", "нет"])

        if quit_ == "да":
            print("[bold red]" + pyfiglet.Figlet("smslant").renderText("Exit") + "[/bold red]")
            exit()
        else:
            nickgen_obj.main()
