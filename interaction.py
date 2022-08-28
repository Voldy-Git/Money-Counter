import pickle

path_to_dir = r"/home/voldy/amount_money"
path_to_log = r"/home/voldy/amount_money/log"
path_to_file = r"/home/voldy/amount_money/log/log.bin"


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
