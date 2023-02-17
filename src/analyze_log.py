def most_requested_dish(data):
    '''f_dish === filtered dish'''
    f_dish = [line.split(",")[1] for line in data if line.startswith("maria")]
    count = {}
    most_requested = f_dish[0]

    for dish in f_dish:
        if dish in count:
            count[dish] += 1
        else:
            count[dish] = 1

    if count[dish] > count[most_requested]:
        most_requested = dish

    return most_requested


def hamburger_counter(data):
    dish = [line.split(",")[1] for line in data if line.startswith("arnaldo")]
    return dish.count("hamburguer")


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, "r") as file:
            data = file.readlines()
            most_requested_dish(data)
            hamburger_counter(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
