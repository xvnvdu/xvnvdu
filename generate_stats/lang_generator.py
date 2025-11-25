from .percentage_bar import format_bar


def format_languages(data):
	name = f"{data['name']:<20}"
	time = f"{data['text']:<16}"
	bar = f"{format_bar(data['percent'], 40):<40}"
	percent = f"{data['percent']:>05.2f} %"
	return f'{name} {time} {bar} {percent}'

def get_languages(languages):
    text = '🤖 TOP 10 LANGUAGES I USE\n'
    for i in range(10):
        text += f'{format_languages(languages[i])}\n'
    return text
