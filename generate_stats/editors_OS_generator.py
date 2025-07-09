from .percentage_bar import format_bar


def format_editors_and_os(data):
    name = f"{data['name']:<10}"
    if name == "Unknown Editor":
        name = f"{'Unknown':<10}"
    time = f"{data['text']:<16}"
    bar = f"{format_bar(data['percent'], 14):<14}"
    percent = f"{data['percent']:>05.2f} %"
    return f"{name} {time} {bar} {percent}"


def get_editors_and_os(editors, operating_systems):
    text = f'{"🪐 EDITORS":<57}{"⚙️ OPERATING SYSTEMS"}\n'
    for i in range(max(len(editors), len(operating_systems))):
        left = format_editors_and_os(editors[i]) if i < len(editors) else ""
        right = (
            format_editors_and_os(operating_systems[i])
            if i < len(operating_systems)
            else ""
        )
        text += f'{left}{" " * 8}{right}\n'
    return text

