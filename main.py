import interaction
import os
from pathlib import Path
import pickle


class MoneyCounter:
    def __init__(self, money, minimum):
        self.money = money
        self.minimum = minimum

    def comparison(self):
        if self.money < self.minimum:
            first_string = f"Sie haben jetzt {self.money}€ aber für ihnen Minimum ist {self.minimum}€.\n"
            second_string = f"Sie brauchen noch {self.minimum - self.money}€ also weitere {self.money / self.minimum * 100}% zum Minimum."
            return first_string + second_string

        return f"Alles gut! Sie haben {self.money} und ihnen Minimum ist {self.minimum}. Sie können weitere {self.money - self.minimum} ausgeben."

    def amount(self, a_money):
        self.money = a_money


class User:
    def __init__(self):
        self.nickname = input("Geben Sie bitte ihre Name: ").rstrip()
        self.code_name = self.nickname.lower().replace(' ', '-')
        self.path_to_dir = r"/home/voldy/amount_money/users/"
        self.path = self.path_to_dir + self.code_name

    def authorization(self):
        if not Path(self.path).is_dir():
            return self.create_account()
        else:
            return self.account()

    def create_account(self):
        os.mkdir(self.path)
        password = input("Denken Sie an ihr Passwort: ")
        with open(self.path + '/password.bin', "wb") as file:
            pickle.dump(password, file)

        return f"Sie haben ein neues Konto erstellt, herzlichen Glückwunsch. Ihr Passwort lautet {password}.", True

    def account(self):
        with open(self.path + '/password.bin', "rb") as file:
            user_password = pickle.load(file)

        max_trying, trying = 5, 1
        while trying <= max_trying:
            password = input("Geben Sie ihr Passwort ein: ")

            if user_password == password:
                return "Passwort ist korrekt anmelden, einloggen...", True

            print(f"Falsches Passwort, versuchen Sie es erneut, Sie haben noch {max_trying - trying}.")
            trying += 1
        else:
            return "Sie haben alle ihre Versuche verbraucht, der Zugang zum System wird verweigert.", False


def check(path):
    path_to_log = path + r"/log"
    if not Path(path).is_dir():
        for dir in (path, path_to_log):
            os.mkdir(dir)

        interaction.create_object(path, MoneyCounter)
    elif not Path(path_to_log).is_dir():
        os.mkdir(path_to_log)
        interaction.create_object(path, MoneyCounter)
    elif not Path(path + path_to_log + "/log.bin").is_file():
        interaction.create_object(path, MoneyCounter)
    else:
        return False
    return True


user = User()
authorization = user.authorization()
print(authorization[0])

if authorization[1]:
    if check(user.path):
        user_object = interaction.read_object(user.path)
        print(user_object.comparison())
