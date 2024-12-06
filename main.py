from lxml import etree

xml_file = "music_albums.xml"
tree = etree.parse(xml_file)

html_xslt_file = "to_html.xslt"
html_output_file = "albums.html"

text_xslt_file = "to_text.xslt"
text_output_file = "albums.txt"

# XPath-запросы
def execute_xpath_queries(tree):
    print("\nРезультаты запросов:")

    # 1. Получить все альбомы указанного жанра (задается в запросе константой).
    pop_albums = tree.xpath('/albums/album[genres/genre="Pop"]/title/text()')
    print(f"Все альбомы жанра 'Pop': {pop_albums}")

    # 2. Получить все жанры, в которых работал указанный исполнитель (задается в запросе константой).
    genres_by_artist = tree.xpath('/albums/album[artists/artist="The Weeknd"]/genres/genre/text()')
    print(f"Жанры, в которых работал исполнитель 'The Weeknd': {set(genres_by_artist)}")
    # 3. Получить все альбомы, в которых есть композиции длиной более пяти минут.
    long_tracks_albums = tree.xpath(
        '/albums/album[tracks/track[number(translate(duration, ":", "")) > 500]]/title/text()')
    print(f"Альбомы, где есть треки длиной более 5 минут: {long_tracks_albums}")

    # 4. Сформировать список воспроизведения из заданного количества композиций. Композиции выбираются случайным образом.
    first_three_tracks = tree.xpath('/albums/album/tracks/track[position()<=3]/name/text()')
    print(f"Список воспроизведения из заданного количества композиций: {first_three_tracks}")

    # 5. Получить первые 3 трека из альбомов, где больше 3 треков
    top_tracks_from_large_albums = tree.xpath(
        '/albums/album[count(tracks/track) > 3]/tracks/track[position() <= 3]/name/text()'
    )
    print(f"Первые 3 трека из альбомов, где больше 3 треков: {top_tracks_from_large_albums}")

# XSLT-преобразование XML-документа
def xslt_transform(xml_file, xslt_file, output_file):
    try:
        xslt_tree = etree.parse(xslt_file)
        transform = etree.XSLT(xslt_tree)
        result = transform(etree.parse(xml_file))
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(str(result))
        print(f"Преобразование завершено. Результат сохранен в '{output_file}'")
    except Exception as e:
        print(f"Ошибка во время XSLT-преобразования: {e}")

if __name__ == "__main__":
    execute_xpath_queries(tree)     # Выполнение XPath-запросов
    xslt_transform(xml_file, text_xslt_file, text_output_file)    # Преобразование в текстовый файл
    xslt_transform(xml_file, html_xslt_file, html_output_file)    # Преобразование в HTML




