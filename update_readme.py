from generate_stats.lang_generator import get_languages
from generate_stats.stats_generator import get_editors_and_os
from generate_stats.info_generator import *
from generate_stats.waka_api import *


readme_page = (
    f'```go\n'
    f'{get_time_range()}\n'
	f'{get_daily_average(daily_average)}'
	f'{get_total_time(total_time)}\n\n'
	f'{get_languages(languages)}\n\n'
	f'{get_editors_and_os(editors, operating_systems, categories)}'
	f'```'
)


if __name__ == '__main__':
    start_marker = "<!--START_SECTION:waka-->"
    end_marker = "<!--END_SECTION:waka-->"

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start = content.find(start_marker)
    end = content.find(end_marker)

    if start == -1 or end == -1:
        raise ValueError("Markers not found in README.md")

    updated = (
        content[:start + len(start_marker)] +
        "\n\n" + readme_page + "\n\n" +
        content[end:]
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated)
