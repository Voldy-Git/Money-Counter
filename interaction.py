import pickle

support_path = "/log/log.bin"

def create_object(path, sclass):
    money = int(input("Geben Sie den Betrag ihres Geld ein: "))
    minimum = int(input("Geben Sie den Mindestbetrag an, den Sie pro Monat benötigen: "))
    with open(path + support_path, "wb") as file:
        pickle.dump(sclass(money, minimum), file)


def read_object(path):
    with open(path + support_path, "rb") as file:
        return pickle.load(file)


def dump_new_obj(path, sclass):
    with open(path, "wb") as file:
        pickle.dump(create_object(path, sclass), file)
