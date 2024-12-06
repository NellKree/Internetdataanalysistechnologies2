import json
import jmespath
from jinja2 import Template

json_file = "music_albums.json"
text_output_file = "albumsjson.txt"
html_output_file = "albumsjson.html"

def load_json_data(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)

def convert_to_seconds(duration):
    try:
        minutes, seconds = map(int, duration.split(':'))
        return minutes * 60 + seconds
    except ValueError:
        return 0

def convert_durations_to_seconds(data):
    for album in data.get("albums", []):
        for track in album.get("tracks", []):
            track["duration_seconds"] = convert_to_seconds(track["duration"])
    return data

def execute_jmespath_queries(data):
    print("\nРезультаты запросов:")

    # 1. Получить все альбомы указанного жанра (задается в запросе константой).
    pop_albums = jmespath.search('albums[?genres[?contains(@, `Pop`)]].title', data)
    print(f"Все альбомы жанра 'Pop': {pop_albums}")

    # 2. Получить все жанры, в которых работал указанный исполнитель (задается в запросе константой).
    genres_by_artist = jmespath.search('albums[?artists[?contains(@, `The Weeknd`)]].genres[]', data)
    print(f"Жанры, в которых работал исполнитель 'The Weeknd': {set(genres_by_artist)}")

    # 3. Получить все альбомы, в которых есть композиции длиной более пяти минут.
    long_tracks_albums = jmespath.search(
        'albums[?tracks[?duration_seconds > `300`]].title', data)
    print(f"Альбомы, где есть треки длиной более 5 минут: {long_tracks_albums}")

    # 4. Сформировать список воспроизведения из заданного количества композиций. Композиции выбираются случайным образом.
    first_three_tracks = jmespath.search('albums[].tracks[:3].name', data)
    print(f"Список воспроизведения из заданного количества композиций: {first_three_tracks}")

    # 5. Получить первые 3 трека из альбомов, где больше 3 треков
    top_tracks_from_large_albums = jmespath.search(
        'albums[?length(tracks) > `3`].tracks[:3].name', data)
    print(f"Первые 3 трека из альбомов, где больше 3 треков: {top_tracks_from_large_albums}")

# Преобразование JSON в txt
def transform_to_text(data, template_file, output_file):
    try:
        with open(template_file, "r", encoding="utf-8") as f:
            template = Template(f.read())

        output = template.render(data=data)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(output)

        print(f"Преобразование завершено. Результат сохранен в '{output_file}'")
    except Exception as e:
        print(f"Ошибка во время преобразования: {e}")

# Преобразование JSON в HTML
def transform_to_html(data, template_file, output_file):
    try:
        with open(template_file, "r", encoding="utf-8") as f:
            template = Template(f.read())

        output = template.render(data=data)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(output)

        print(f"Преобразование завершено. Результат сохранен в '{output_file}'")
    except Exception as e:
        print(f"Ошибка во время преобразования: {e}")

data = load_json_data(json_file)
data = convert_durations_to_seconds(data)
execute_jmespath_queries(data)      # Выполнение запросов JMESPath
transform_to_text(data, "to_text_template.txt", text_output_file)       # Преобразование в текст
transform_to_html(data, "to_html_template.html", html_output_file)      # Преобразование в HTML







