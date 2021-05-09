from rich import print
from rich.prompt import Prompt
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
         "[green bold]    _            _____         _    \n"
         " __| |_  __ _ _ |_   _|__  ___| |___\n"
         "|_ / ' \/ _` | '_|| |/ _ \/ _ \ (_-<\n"
         "/__|_||_\__,_|_|  |_|\___/\___/_/__/[/green bold]\n"         
         "\n"
         " [[green bold]1[/green bold]] [#eeeeee]Bruteforce[/#eeeeee]\n"
         " [[green bold]2[/green bold]] Phishing\n"
         " [[green bold]3[/green bold]] Help\n"
         "\n"
         " [[red bold]0[/red bold]] Exit\n"
         ""
      )

   def get_command(self):
        return self.prompt.ask(" [[green]*[/green]] Команда")

   def clear_terminal(self):
      if os.sys.platform == "nt":
         os.system("clear") # Unix система
      else:
         os.system("cls") # Windows система

   def command_not_found(self, command):
      self.clear_terminal() # Очищаем терминал

      # Сообщение об неправильности команды
      print(" [[red bold]-[/red bold]] Команда [red]'{0}'[/red] не найдено!\n".format(command))
      self.prompt.ask(" [[yellow]![/yellow]] Нажмите Enter")

      # Заново показываем меню
      self.menu()

   def exit_program(self):
      self.clear_terminal() # Очищаем терминал

      print(" [[yellow]![/yellow]] Выходим из программы[white]...[/white]\n")
      exit()

   def menu(self):
      self.banner()
      comm = self.get_command() # Запрашиваем у пользователя команду 

      if comm == "1": # Вход в раздел Брутфорс
         print("BruetForce")
      elif comm == "2": # Вход в раздел Фишинг
         print("Phishing")
      elif comm == "3": # Вход в раздел Помощь
         print("Help")
      elif comm == "0": 
         self.exit_program() # Выйти с программы
      else: 
         self.command_not_found(comm) # Выдает сообщение если команда неправильная

   def main(self):
      self.menu()

zharTools().main()