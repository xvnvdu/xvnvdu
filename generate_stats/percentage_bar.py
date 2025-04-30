def format_bar(percent, width):
    filled = int(width * percent / 100)
    return '█' * filled + '░' * (width - filled)
