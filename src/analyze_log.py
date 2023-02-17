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


def unordered_food(data):
    menu = {line.split(",")[1] for line in data}
    requests_joao = {
        line.split(",")[1] for line in data if line.startswith("joao")
    }
    return menu.difference(requests_joao)


def unattended_days(data):
    days = {line.split(",")[2].replace('\n', '') for line in data}

    days_that_joao_did_not_attend = {
        line.split(",")[2].replace('\n', '')
        for line in data if line.startswith("joao")
    }
    return days.difference(days_that_joao_did_not_attend)


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, "r") as file:
            data = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    with open("data/mkt_campaign.txt", "w") as new_file:
        new_file.write(
            f"{most_requested_dish(data)}\n"
            f"{hamburger_counter(data)}\n"
            f"{unordered_food(data)}\n"
            f"{unattended_days(data)}"
        )
