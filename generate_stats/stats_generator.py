from .percentage_bar import format_bar


def format(data):
    name = f"{data['name']:<10}"
    if name.startswith("Unknown"):
        name = f"{'Unknown':<10}"
    elif name.startswith("Coding"):
        name = f"{data['name']:<14}"
    elif name.startswith("Writing"):
        name = f"{data['name']:<14}"

    time = f"{data['text']:<16}"
    bar = f"{format_bar(data['percent'], 14):<14}"
    percent = f"{data['percent']:>05.2f} %"
    return f"{name} {time} {bar} {percent}"


def get_editors_and_os(editors, operating_systems, categories):
    text = f'{"🪐 EDITORS":<57}{"⚙️ OPERATING SYSTEMS"}\n'
    ed_len, os_len, cat_len = len(editors), len(operating_systems), len(categories)
    cat = 0
    for i in range(max(ed_len, os_len + cat_len) + 2):
        left =  ""
        if i < ed_len:
            left = format(editors[i])

        right = ""
        if i < os_len:
            right = format(operating_systems[i])

        if i > os_len:
            if i == os_len + 1:
                right = f'{"🛠 CATEGORIES"}'
            else:
                right = format(categories[cat])
                cat += 1

        amount = 8 
        if i >= ed_len:
            amount = 58

        text += f'{left}{" " * amount}{right}\n'
    return text

