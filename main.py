import pickle
import os
from pathlib import Path


class MoneyCounter:
    def __init__(self, money, minimum):
        self.money = money
        self.minimum = minimum

    def comparison(self):
        if self.money < self.minimum:
            first_string = f"Sie haben jetzt {self.money}€ aber für ihnen Minimum ist {self.minimum}€.\n"
            second_string = f"Sie brauchen noch {self.minimum - self.money}€ also weitere {self.money / self.minimum * 100}% zum Minimum."
            return first_string + second_string

        return f"Alles gut! Sie haben {self.money} und ihnen minimum ist {self.minimum}. Sie können weitere {self.money - self.minimum} ausgeben."

    def amount(self, a_money):
        self.money = a_money


def create_object():
    money = int(input("Geben Sie den Betrag ihres Geld ein: "))
    minimum = int(input("Geben Sie den Mindestbetrag an, den Sie pro Monat benötigen: "))
    with open(path_to_file, "wb") as file:
        pickle.dump(MoneyCounter(money, minimum), file)


def read_object():
    with open(path_to_file, "rb") as file:
        return pickle.load(file)


def dump_new_obj():
    with open(path_to_file, "wb") as file:
        pickle.dump(create_object(), file)


path_to_dir = r"/home/voldy/amount_money"
path_to_log = r"/home/voldy/amount_money/log"
path_to_file = r"/home/voldy/amount_money/log/log.bin"


if not Path(path_to_dir).is_dir():
    for dir in (path_to_dir, path_to_log):
        os.mkdir(dir)

    create_object()
elif not Path(path_to_log).is_dir():
    os.mkdir(path_to_log)
    create_object()
elif not Path(path_to_file).is_file():
    create_object()


created_object = read_object()

created_object.amount(400)
print(created_object.comparison())
