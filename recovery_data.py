def recoveryData():
    with open("database.txt", "r", encoding="utf-8") as database:
        lines = database.read().split("\n")
        password_array = [line.split(";") for line in lines]
        return password_array
