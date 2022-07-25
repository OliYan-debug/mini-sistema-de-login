def saveData(user, password):
    with open("database.txt", "a+", encoding="utf-8") as database:
        database.writelines(f"\n{user};{password}")
