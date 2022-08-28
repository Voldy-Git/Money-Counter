import interaction
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

        return f"Alles gut! Sie haben {self.money} und ihnen Minimum ist {self.minimum}. Sie können weitere {self.money - self.minimum} ausgeben."

    def amount(self, a_money):
        self.money = a_money


if not Path(interaction.path_to_dir).is_dir():
    for dir in (interaction.path_to_dir, interaction.path_to_log):
        os.mkdir(dir)

    interaction.create_object()
elif not Path(interaction.path_to_log).is_dir():
    os.mkdir(interaction.path_to_log)
    interaction.create_object()
elif not Path(interaction.path_to_file).is_file():
    interaction.create_object()


created_object = interaction.read_object()

created_object.amount(int(input("Geben Sie den Betrag ihres Geld ein: ")))
print(created_object.comparison())
