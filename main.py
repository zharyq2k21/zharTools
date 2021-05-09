from rich import print
from rich.prompt import Prompt
import time
import os

class zharTools(object):
   def __init__(self):
      # Путь до текущего файла
      # self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
      self.prompt = Prompt()

   def banner(self):
      self.clear_terminal() # Очищаем терминал перед показом баннера
      
      # Наш баннер и меню
      print(
         "[green bold]"
         "\t    _            _____         _    \n"
         "\t __| |_  __ _ _ |_   _|__  ___| |___\n"
         "\t|_ / ' \/ _` | '_|| |/ _ \/ _ \ (_-<\n"
         "\t/__|_||_\__,_|_|  |_|\___/\___/_/__/\n"
         "[/green bold]"
         "\t\n"
         "\t[[green bold]1[/green bold]] [#eeeeee]Bruteforce[/#eeeeee]\n"
         "\t[[green bold]2[/green bold]] Phishing\n"
         "\t[[green bold]3[/green bold]] Author\n"
         "\t\n"
         "\t[[red bold]0[/red bold]] Exit\n"
         "\t"
      )

   def get_command(self):
      # Спрашиваем команду и вернем ее в функцию 
      return self.prompt.ask("\t[[green]*[/green]] Command")

   def clear_terminal(self):
      if os.sys.platform == "nt":
         os.system("clear") # Unix система
      else:
         os.system("cls") # Windows система

   def command_not_found(self, command):
      self.clear_terminal() # Очищаем терминал

      # Сообщение об неправильности команды
      print(
         "\n[bold yellow]"
         "\t █████ █████     █████    █████ █████ \n"
         "\t░░███ ░░███    ███░░░███ ░░███ ░░███  \n"
         "\t ░███  ░███ █ ███   ░░███ ░███  ░███ █\n"
         "\t ░███████████░███    ░███ ░███████████\n"
         "\t ░░░░░░░███░█░███    ░███ ░░░░░░░███░█\n"
         "\t       ░███░ ░░███   ███        ░███░\n"
         "\t       █████  ░░░█████░         █████\n"
         "\t      ░░░░░     ░░░░░░         ░░░░░  \n"
         "[/bold yellow]"
      )
      print("\t[[red bold]-[/red bold]] Command [red]'{0}'[/red] not found!\n".format(command))
      self.prompt.ask("\t[[yellow]![/yellow]] Press Enter")

      # Заново показываем меню
      self.menu()

   def exit_program(self):
      self.clear_terminal() # Очищаем терминал

      print(
         "[bold red]"
         "\t ___     _ _    \n"   
         "\t| __|_ _(_) |_  \n" 
         "\t| _|\ \ / |  _| \n"
         "\t|___/_\_\_|\__| \n"
         "[/bold red]"
         "\n"
         "\t[[yellow]![/yellow]] Exit the program[white]...[/white]\n"
      )
      # Ждем 2 секунды и закрывем программу
      time.sleep(2)
      exit()

   def author(self):
      self.clear_terminal()
      print(
         "[bold blue]"
         "\t   _       _   _            \n"            
         "\t  /_\ _  _| |_| |_  ___ _ _ \n" 
         "\t / _ \ || |  _| ' \/ _ \ '_|\n"
         "\t/_/ \_\_,_|\__|_||_\___/_|  \n"
         "[/bold blue]\n"
         "\t[[bold blue]*[/bold blue]] Author: Maulen Azikulov\n"
         "\t[[bold blue]*[/bold blue]] Instagram: @zhar_yq\n"
         "\t[[bold blue]*[/bold blue]] Telegram: @zharyqtyq\n"
      )
      self.prompt.ask("\t[[green bold]*[/green bold]] Press Enter")
      
      # Вернемся к начальному меню
      self.menu()

   def menu(self):
      self.banner()
      comm = self.get_command() # Запрашиваем у пользователя команду 

      if comm == "1": # Вход в раздел Брутфорс
         print("BruetForce")
      elif comm == "2": # Вход в раздел Фишинг
         print("Phishing")
      elif comm == "3": # Вход в раздел Автор
         self.author()
      elif comm == "0": 
         self.exit_program() # Выйти с программы
      else: 
         self.command_not_found(comm) # Выдает сообщение если команда неправильная

   def main(self):
      self.menu()

zharTools().main()